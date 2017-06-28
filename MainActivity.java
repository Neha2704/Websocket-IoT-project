public class MainActivity extends AppCompatActivity {

    private button start;
    private TextView output;
    private OkHttpClient client;
    
    private final class EchoWebSocketListener extends WebSocketListener {
        @Override
        public void onOpen (WebSocket webSocket,Response response) {
            webSocket.send ("Hello World!");
            webSocket.send ("What's up");
            webSocket.send ("What's up");
