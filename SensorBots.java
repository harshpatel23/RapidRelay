import java.util.*;
import java.sql.Timestamp;
import org.json.simple.JSONObject;
import java.net.*;
import java.io.*;
// import java.io.OutputStreamWriter;

class Location{
	String city;
	String suburb;

	public Location(String city, String suburb){
		this.city = city;
		this.suburb = suburb;
	}

	public String toString(){
		return "City : " + this.city + "Suburb: " + this.suburb;
	}
}

class WeatherSensor implements Runnable{
	int node_id;
	Date date;
	Timestamp ts;
	String city;
	String suburb;
	double humidity;
	double temperature;
	double pressure;
	long message_no;
	JSONObject data;
	String type;
	URL url;
	String path = "data/read";

	// Socket socket;
	// BufferedWriter socketWr;

	public WeatherSensor(int id,Location location){
		this.node_id = id;
		this.message_no = 0;
		this.city = location.city;
		this.suburb = location.suburb;
		this.type = "weather";
		try{
			this.url = new URL("http://127.0.0.1:5000/" + path);
		}catch(Exception e){
			System.out.println(e);
		}
		// try{
		// 	socket = new Socket("127.0.0.1", 3000);
		// 	socketWr = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
		// }catch(Exception e){
		// 	System.out.println(e);
		// }
	}

	public void run(){
		while(true){
			try{
				this.date = new Date();
				this.ts = new Timestamp(date.getTime());
				// System.out.println("Message " + message_no + " from Sensor " + this.node_id + "at timestamp: " + ts);
				this.humidity = 60 + Math.random() * (80 - 60);
				this.temperature = 20 + Math.random() * (30 - 20);
				this.pressure = 1000 + Math.random() * (1020 - 1000);
				this.message_no++;
				this.createJson();
				this.sendHttpPacket();
				Thread.sleep(500);
			}
			catch(Exception e){
				System.out.println("Error............................................");
			}
		}
	}

	public void createJson(){
		this.data = new JSONObject();	
		this.data.put("type", this.type);
		this.data.put("time", this.ts.toString());
		this.data.put("city", this.city);
		this.data.put("suburb", this.suburb);
		this.data.put("humidity", this.humidity);
		this.data.put("temperature", this.temperature);
		this.data.put("pressure", this.pressure);

		System.out.println(data);
		System.out.println();
	}

	// public void sendHttpPacket() throws Exception{
	// 	String path = "/data/read";
	// 	String sendData = this.data.toString();
	// 	// System.out.println(data);

	// 	StringBuffer sb = new StringBuffer();
	// 	sb.append("POST " + path + " HTTP/1.1\r\n");
	// 	// sb.append("Host: http://127.0.0.1\r\n");
	//     sb.append("Content-Length: " + this.sendData.length() + "\r\n");
	//     sb.append("Content-Type: application/json\r\n");
	//     sb.append("\r\n");

	//     sb.append(this.sendData);

	//     socketWr.write(sb.toString());

	//     System.out.println(sb);
	//     socketWr.flush();
	// }

	public void sendHttpPacket() throws Exception{
		HttpURLConnection con = (HttpURLConnection)url.openConnection();
		con.setRequestMethod("POST");
		con.setRequestProperty("Content-Type", "application/json; utf-8");
		con.setRequestProperty("Accept", "application/json");
		con.setDoOutput(true);
		String jsonInputString = this.data.toString();
		System.out.println(jsonInputString);
		try(OutputStream os = con.getOutputStream()){
    		byte[] input = jsonInputString.getBytes("utf-8");
    		os.write(input, 0, input.length);           
		}catch(Exception e){
			System.out.println(e);
		}

		try(BufferedReader br = new BufferedReader(
 			new InputStreamReader(con.getInputStream(), "utf-8"))) {
    		StringBuilder response = new StringBuilder();
    		String responseLine = null;
    		while ((responseLine = br.readLine()) != null) {
       			response.append(responseLine.trim());
    		}
    		System.out.println(response.toString());
		}catch(Exception e){
			System.out.println(e);
		}
	}

}

class AgricultureSensor implements Runnable{
	int node_id;
	Date date;
	Timestamp ts;
	int greenhouse_id;
	double humidity;
	double temperature;
	double moisture;
	long message_no;
	JSONObject data;
	String type;
	URL url;
	String path = "data/read";

	public AgricultureSensor(int id,int greenhouse_id){
		this.node_id = id;
		this.message_no = 0;
		this.greenhouse_id = greenhouse_id;
		this.type = "agriculture";
		try{
			this.url = new URL("http://127.0.0.1:5000/" + path);
		}catch(Exception e){
			System.out.println(e);
		}
	}

	public void run(){
		while(true){
			try{
				this.date = new Date();
				this.ts = new Timestamp(date.getTime());
				// System.out.println("Message " + message_no + " from Sensor " + this.node_id + "at timestamp: " + ts);
				this.humidity = 60 + Math.random() * (80 - 60);
				this.temperature = 20 + Math.random() * (30 - 20);
				this.moisture = 40 + Math.random() * (80-40);
				this.message_no++;
				this.createJson();
				this.sendHttpPacket();
				Thread.sleep(500);
			}
			catch(Exception e){
				System.out.println("Error............................................");
			}
		}
	}

	public void createJson(){
		this.data = new JSONObject();
		this.data.put("type", this.type);
		this.data.put("time", this.ts.toString);
		this.data.put("greenhouse_id", this.greenhouse_id);
		this.data.put("humidity", this.humidity);
		this.data.put("temperature", this.temperature);
		this.data.put("moisture", this.moisture);

		System.out.println(data);
		System.out.println();
	}

	public void sendHttpPacket() throws Exception{
		HttpURLConnection con = (HttpURLConnection)url.openConnection();
		con.setRequestMethod("POST");
		con.setRequestProperty("Content-Type", "application/json; utf-8");
		con.setRequestProperty("Accept", "application/json");
		con.setDoOutput(true);
		String jsonInputString = this.data.toString();
		System.out.println(jsonInputString);
		try(OutputStream os = con.getOutputStream()){
    		byte[] input = jsonInputString.getBytes("utf-8");
    		os.write(input, 0, input.length);           
		}catch(Exception e){
			System.out.println(e);
		}

		try(BufferedReader br = new BufferedReader(
 			new InputStreamReader(con.getInputStream(), "utf-8"))) {
    		StringBuilder response = new StringBuilder();
    		String responseLine = null;
    		while ((responseLine = br.readLine()) != null) {
       			response.append(responseLine.trim());
    		}
    		System.out.println(response.toString());
		}catch(Exception e){
			System.out.println(e);
		}
	}

}

class AirSensor implements Runnable{
	int node_id;
	Date date;
	Timestamp ts;
	String city;
	String suburb;
	double so2;
	double no2;
	double o3;
	long message_no;
	JSONObject data;
	String type;
	URL url;
	String path = "data/read";

	public AirSensor(int id,Location location){
		this.node_id = id;
		this.message_no = 0;
		this.city = location.city;
		this.suburb = location.suburb;
		this.type = "air";
		try{
			this.url = new URL("http://127.0.0.1:5000/" + path);
		}catch(Exception e){
			System.out.println(e);
		}
	}

	public void run(){
		while(true){
			try{
				this.date = new Date();
				this.ts = new Timestamp(date.getTime());
				// System.out.println("Message " + message_no + " from Sensor " + this.node_id + "at timestamp: " + ts);
				this.so2 = 0.00001 + Math.random() * (0.00002 - 0.00001);
				this.no2 = 0.000002 + Math.random() * (0.000004 - 0.000002);
				this.o3 = 0.0008 + Math.random() * (0.0020 - 0.0008);
				this.message_no++;
				this.createJson();
				this.sendHttpPacket();
				Thread.sleep(500);
			}
			catch(Exception e){
				System.out.println("Error............................................");
			}
		}
	}

	public void createJson(){
		this.data = new JSONObject();
		this.data.put("type", this.type);
		this.data.put("time", this.ts.toString());
		this.data.put("city", this.city);
		this.data.put("suburb", this.suburb);
		this.data.put("so2", this.so2);
		this.data.put("no2", this.no2);
		this.data.put("o3", this.o3);

		System.out.println(data);
		System.out.println();
	}

	public void sendHttpPacket() throws Exception{
		HttpURLConnection con = (HttpURLConnection)url.openConnection();
		con.setRequestMethod("POST");
		con.setRequestProperty("Content-Type", "application/json; utf-8");
		con.setRequestProperty("Accept", "application/json");
		con.setDoOutput(true);
		String jsonInputString = this.data.toString();
		System.out.println(jsonInputString);
		try(OutputStream os = con.getOutputStream()){
    		byte[] input = jsonInputString.getBytes("utf-8");
    		os.write(input, 0, input.length);           
		}catch(Exception e){
			System.out.println(e);
		}

		try(BufferedReader br = new BufferedReader(
 			new InputStreamReader(con.getInputStream(), "utf-8"))) {
    		StringBuilder response = new StringBuilder();
    		String responseLine = null;
    		while ((responseLine = br.readLine()) != null) {
       			response.append(responseLine.trim());
    		}
    		System.out.println(response.toString());
		}catch(Exception e){
			System.out.println(e);
		}
	}

}

class SensorBots{
	public static void main(String[] args) throws InterruptedException{

		int agriculture_bot = 10;
		int weather_bot = 20;
		int air_bot = 20;

		ArrayList<Location> locations = new ArrayList<Location>();

		locations.add(new Location("Mumbai","Andheri"));
		locations.add(new Location("Mumbai","Dadar"));
		locations.add(new Location("Mumbai","Bandra"));
		locations.add(new Location("Mumbai","Ghatkopar"));
		locations.add(new Location("Mumbai","Borivali"));

		locations.add(new Location("Bangalore","Malleswaram"));
		locations.add(new Location("Bangalore","Koramangala"));
		locations.add(new Location("Bangalore","Hebbal"));
		locations.add(new Location("Bangalore","Jayanagar"));
		locations.add(new Location("Bangalore","Banashankari"));

		locations.add(new Location("Delhi", "Saket"));
		locations.add(new Location("Delhi", "Nehru Place"));
		locations.add(new Location("Delhi", "Cyber City"));
		locations.add(new Location("Delhi", "Vasant Kunj"));
		locations.add(new Location("Delhi", "Sector 21"));

		locations.add(new Location("Pune", "Baner"));
		locations.add(new Location("Pune", "Undri"));
		locations.add(new Location("Pune", "Dhanori"));
		locations.add(new Location("Pune", "Kharadi"));
		locations.add(new Location("Pune", "Pune-Satara Road"));

		for(int i=1;i<=agriculture_bot;i++){
			Thread t = new Thread(new AgricultureSensor(i,1000+i));
			t.start();
		}

		for(int i=1;i<=air_bot;i++){
			Thread t = new Thread(new AirSensor(i,locations.get(i-1)));
			t.start();
		}

		for(int i=1;i<=weather_bot;i++){
			Thread t = new Thread(new WeatherSensor(i,locations.get(i-1)));
			t.start();
		}

	}
}