//________________________________________________________________
// Traffic Light Simulator wusing Sequential Logic 
// Author: Dawson Ash CS1400 Team 5 (Alex, Sam, Dawson)
//________________________________________________________________
import java.util.Map;
import java.util.HashMap;
import java.util.Timer;
import java.util.TimerTask;



public class App {


//declaring our map on our broadest class so its contents are always accessible
Map <String, String> color = new HashMap<>();
//initializing a default state for each direction
        public App(){
        color.put("NorthSouth", "Green");
        color.put("EastWest", "Red");
        color.put("NorthToEast+SouthToWest", "Red");
        color.put("NorthToWest+SouthToEast", "Red");

        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TrafficLightTask(), 0, 2000);
        }
 
//Method that controls the logic of the system, works one step at a time
public void stateChange(){
    System.out.println(color);
        if (color.get("NorthSouth").equals("Green")) {
                color.put("NorthSouth", "Yellow");
            } else if (color.get("NorthSouth").equals("Yellow")) {
                color.put("NorthSouth", "Red");
                color.put("EastWest", "Green");
            } else if (color.get("EastWest").equals("Green")) {
                color.put("EastWest", "Yellow");
            } else if (color.get("EastWest").equals("Yellow")) {
                color.put("EastWest", "Red");
            } else if (color.get("EastWest").equals("Red") && color.get("NorthSouth").equals("Red")){
                color.put("NorthToEast+SouthToWest", "Green");
            } else if (color.get("NorthToEast+SouthToWest").equals("Green")){
                color.put("NorthToEast+SouthToWest", "Yellow");
            } else if (color.get("NorthToEast+SouthToWest").equals("Yellow")){
                color.put("NorthToEast+SouthToWest", "Red");
                color.put("NorthToWest+SouthToEast", "Green");
            } else if (color.get("NorthToWest+SouthToEast").equals("Green")){
                color.put("NorthSouth", "Green");
            }
            System.out.println(color);
}



private class TrafficLightTask extends TimerTask {
        @Override
        public void run() {
            stateChange();
        }
        }


         

    public static void main(String[] args) throws Exception {
        new App();
        }//main 

    }// app class
