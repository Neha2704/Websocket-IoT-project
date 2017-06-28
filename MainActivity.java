public class MainActivity extends AppCompatActivity {

    private button start;
    private TextView output;
    private OkHttpClient client;
    
    private final class EchoWebSocketListener extends WebSocketListener {
        @Override
        public void onOpen (WebSocket websocket,Response response) {
            websocket.send ("Hello World!");
            websocket.send ("What's up");
            websocket.send (ByteString.decodeHex("Try it!"));
            websocket.close (NORMAL_CLOSURE_STATUS, "Goodbye!");
        }
        
        @Override
        public void onMessage (WebSocket websocket, String text) {
            output ("Recieved :" + text);
        }
        
        @Override
        public void onMessage (WebSocket websocket, ByteString bytes) {
            output ("Received bytes :" + bytes.hex());
        }
        
        @Override
        public void onClosing (WebSocket websocket, int code, String reason) {
            websocket.close (NORMAL_CLOSURE_STATUS, null);
            output ("Closing " + code + " / " + reason);
        }
        
        @Override
        public void onFailure (WebSocket websocket, Throwable t, Response response) {
            output ("Error: " + t.getMessage());
        }
    }
        
    @Override
    protected void onCreate (Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        start = (Button) findViewById (R.id.start);
        output = (TextView) findViewById (R.id.output);
        client = new OkHttpClient();
        
        start.onClickListener (new View.OnCLickListener() {
            @Override
            public void onClick (View view) {
                start();
            }
        });
    }
    
    private void start() {
        Request request = new Request.Builder().url("").build();
        EchoWebSocketListener listener = new EchoWebSocketListener();
        WebSocket ws = client.newWebSocket (request, listener);
        
        client.dispatcher().executorService().shutdown();
    
    private void output (final string txt) {
        runOnUiThread (new Runnable () {
            @Override
            public void run () {
                output.setText(output.getText().toString() + "\n\n" + txt);
            }
        });
    }
}        
