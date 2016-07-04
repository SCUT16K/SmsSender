package info.liuliqiang.smssender;

import android.os.Bundle;
import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.telephony.SmsManager;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private Button btnStart, btnStop;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnStart = (Button) findViewById(R.id.btnStart);
        btnStart.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                if (android.os.Build.VERSION.SDK_INT > 9) {
                    StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                    StrictMode.setThreadPolicy(policy);
                }
                Log.v("tag", "Hehe");
                while (true) {
                    String cnt = queryUrl();
                    processRepsonse(cnt);
                    try {
                        Thread.sleep(10 * 1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                        Log.e("Thread", "sleep error");
                    }
                }
            }
        });
    }

    private String queryUrl() {
        try {
            URL url = new URL("http://120.24.214.86:5555/");
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            try {
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
                StringBuilder stringBuilder = new StringBuilder();
                String line;
                while ((line = bufferedReader.readLine()) != null) {
                    stringBuilder.append(line).append("\n");
                }
                bufferedReader.close();
                // Log.v("url_content", stringBuilder.toString());
                return stringBuilder.toString();
            }
            finally{
                urlConnection.disconnect();
            }
        }
        catch(Exception e) {
            Log.e("ERROR", e.getMessage(), e);
            return null;
        }
    }

    private void processRepsonse(String response) {
        try {
            JSONObject jsonObj = new JSONObject(response);

            // Getting JSON Array node
            JSONObject data = jsonObj.getJSONObject("data");
            String type = data.getString("type");
            Log.v("type", type);
            if (type.equals("sendSms")) {
                JSONObject content = data.getJSONObject("info");
                String phone = content.getString("phone");
                String msg = content.getString("msg");
                Log.i("Sms-phone", phone);
                Log.i("Sms-msg", msg);
                sendSms(phone, msg);
            }
            else {
                Log.d("no", "no sms to send");
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    private void sendSms(String phone, String message) {
        // 移动运营商允许每次发送的字节数据有限，我们可以使用Android给我们提供 的短信工具。
        if (message != null) {
            SmsManager sms = SmsManager.getDefault();
            // 如果短信没有超过限制长度，则返回一个长度的List。
            List<String> texts = sms.divideMessage(message);
            for (String text : texts) {
                Log.i("send sms", text);
                sms.sendTextMessage(phone, null, text, null, null);
            }
        }
    }
}
