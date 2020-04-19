# Zoo Monitoring System

## Main Zoo Monitoring System Java Code
```
package ZooMonitoringSystem;

import java.io.FileNotFoundException;
import java.util.Scanner;


public class ZooMonitoringSystem {
    static String mainMenu = "Select Monitoring Option:\n"
            + "1. Animal\n"
            + "2. Habitat\n"
            + "3. Exit";
    // options for entering each menu selection
    static String MENU_OPTION_ANIMAL = "1. Animal";
    static String MENU_OPTION_HABITAT = "2. Habitat";
    static String MENU_OPTION_EXIT = "3. Exit";
    
    // validate user input against menu options
    public static String validSelection (String userMenuSelection) {
        Scanner scnr;
        scnr = new Scanner(System.in);
        //Error message for when user enters incorrect selections
        while (!mainMenu.contains(userMenuSelection)) { 
            System.out.println("Error: Selection not found");
            System.out.println();
            System.out.println(mainMenu); //request and read in new input from user
            userMenuSelection = scnr.nextLine(); 
        }
        return userMenuSelection;
    }
    
    // convert user input to title case
    public static String titleCase (String userInput) {
        if (userInput == null) {
        return userInput;
        }
        StringBuilder converted = new StringBuilder();
        boolean convertNext = true;
        for (char ch : userInput.toCharArray()) {
            if (Character.isSpaceChar(ch)) {
                convertNext = true;
            } else if (convertNext) {
                ch = Character.toTitleCase(ch);
                convertNext = false;
            } else {
                ch = Character.toLowerCase(ch);
            }
            converted.append(ch);
        }
    return converted.toString();
    }
    /**
     *
     * @param arg
     * @throws FileNotFoundException
     */
    public static void main (String arg[]) throws FileNotFoundException {
        Scanner scnr;
        scnr = new Scanner(System.in);

        
        System.out.println("Welcome to the Zoo Monitoring System\n");
        
        System.out.println(mainMenu);
        String userMenuSelection = scnr.nextLine(); 
        
        // convert user input to title case
        userMenuSelection = titleCase(userMenuSelection);        
        // validate user input against menu options
        userMenuSelection = validSelection(userMenuSelection);
        
        while (!MENU_OPTION_EXIT.contains(userMenuSelection)) {
            //animal monitoring system
            if (MENU_OPTION_ANIMAL.contains(userMenuSelection)) {
                MonitorAnimal animalSystem;
                animalSystem = new MonitorAnimal();
                String animalSelection; //outputs menu of options for animals from file
                animalSelection = animalSystem.getMenu();
                if (!animalSelection.contains("00")) { // checks if user selected to 'go back'
                    animalSelection = animalSystem.validCheck(animalSelection); //checks input against file to ensure validity
                    animalSelection = titleCase(animalSelection);
                    animalSystem.getData(animalSelection); // outputs data on selected animal from file
                }
                
                                              
            }
            //habitat monitoring system
            else if (MENU_OPTION_HABITAT.contains(userMenuSelection)) {
                MonitorHabitat habitatSystem = new MonitorHabitat();
                String habitatSelection = habitatSystem.getMenu(); //outputs menu of options for habitats from file
                if (!habitatSelection.contains("00")) { // checks if user selected to 'go back'
                    habitatSelection = habitatSystem.validCheck(habitatSelection); //checks input against file to ensure validity
                    habitatSelection = titleCase(habitatSelection);
                    habitatSystem.getData(habitatSelection); //outputs data on selected animal from file
                }
            } 
            System.out.println(mainMenu); //output menu to allow user to select new option
            userMenuSelection = scnr.nextLine();
            userMenuSelection = titleCase(userMenuSelection);
            userMenuSelection = validSelection(userMenuSelection);
        }
        if (MENU_OPTION_EXIT.contains(userMenuSelection)) {
            //only executes when Exit is entered.
            System.out.println("Goodbye"); //exit message is displayed
        } 
    }
}
```

## Animal Monitoring System Java Code
```
package ZooMonitoringSystem;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class MonitorAnimal {
    
    static File ANIMAL_DATA = new File("src\\ZooMonitoringSystem\\animals.txt");
    
    public String getMenu () throws FileNotFoundException {         
        String animalSelection;
        Scanner scnrAnimalInfo;
        try (Scanner menu = new Scanner(ANIMAL_DATA) //used to read in file menu
        ) {
            scnrAnimalInfo = new Scanner(System.in); //used to read in user input
            System.out.println("Please select an animal to monitor:\n");
            String currLine;
            while (menu.hasNextLine()) {
                //outputs first lines of .txt file for menu selection
                currLine = menu.nextLine();
                if (currLine.contains("Details")) {
                    System.out.println(currLine);
                }
            }
            System.out.println("Enter 00 to Go Back to Main Menu\n");
        }
        
        animalSelection = scnrAnimalInfo.nextLine(); //save user input to a variable
        
        return animalSelection;
    }
    
    public String validCheck (String animalSelection) throws FileNotFoundException {
        String currLine;
        Scanner scnrAnimalInfo = new Scanner(System.in); //used to read in user input
        boolean ckNum;
        ckNum = false;
        
        while (!ckNum) {
            try (Scanner check = new Scanner(ANIMAL_DATA) //used to check animal selction against file
            ) {
                while (check.hasNextLine()) {
                    currLine = check.nextLine();
                    if (currLine.contains(animalSelection)) {
                        ckNum = true;
                    }
                }   
                if (!ckNum) {
                    //if animalSelection is not found, then error is output and user must enter selection again.
                    System.out.println("Error: Selection not found. Please try again\n");
                    animalSelection = scnrAnimalInfo.nextLine();
                }
            }
        }
        return animalSelection;
    }        
                  
    public void getData (String animalSelection) throws FileNotFoundException {
        try (Scanner data = new Scanner(ANIMAL_DATA) //create new scanner to parse again
        ) {
            int i = 4;
            String currLine;
            
            while (data.hasNextLine()) {
                currLine = data.nextLine();
                if (currLine.contains(animalSelection)) {
                    System.out.println(currLine);
                    while (i > 0) { //gets lines after user input is located
                        currLine = data.nextLine();
                        if (currLine.contains("*")) {
                            currLine = currLine.replace("*", "");
                            System.out.println("ALERT! " + currLine);
                            DialogBox box = new DialogBox();
                            box.dialogBoxAnimal(currLine);
                        }
                        else {
                            System.out.println(currLine);
                        }
                        --i;
                    }
                }
            }
            System.out.println();
        }
    }        
}
```
### Animal Text File
```
Details on lion
Details on tiger
Details on bear
Details on giraffe
Details on monkey
Details on elephant
Details on turtle
Details on snake
Details on bird

Animal - Lion
Name: Leo
Age: 5
*****Health concerns: Cut on left front paw
Feeding schedule: Twice daily

Animal - Tiger
Name: Maj
Age: 15
Health concerns: None
Feeding schedule: 3x daily

Animal - Bear
Name: Baloo
Age: 1
Health concerns: None
*****Feeding schedule: None on record

Animal - Giraffe
Name: Spots
Age: 12
Health concerns: None
Feeding schedule: Grazing

Animal - Monkey
Name: Cody
Age: 2
Health concerns: None
Feeding schedule: 2x daily

Animal - Monkey
Name: Anna
Age: 3
Health concerns: None
Feeding schedule: 2x daily

Animal - Elephant
Name: Jumbo
Age: 16
Health concerns: None
Feeding Schedule: Evening Feedings Daily

Animal - Turtle
Name: Tim
Age: 4
*****Health concerns: Minor Infection, on Antibiotics
Feeding schedule: Morning Feedings Daily

Animal - Snake
Name: Lucy
Age: 7
Health concerns: None
Feeding Schedule: 1x every other day

Animal - Bird
Name: Paul
Age: 9
Health concerns: None
Feeding Schedule: Food provided by environment
```

## Habitat Monitoring System Java Code
```
package ZooMonitoringSystem;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class MonitorHabitat {
    
    static File HABITAT_DATA = new File("src\\ZooMonitoringSystem\\habitats.txt");
    
    public String getMenu () throws FileNotFoundException {              
        String habitatSelection;
        Scanner scnrHabitatInfo;
        try (Scanner menu = new Scanner(HABITAT_DATA) //used to read in file menu
        ) {
            scnrHabitatInfo = new Scanner(System.in); //used to read in user input
            System.out.println("Please select an habitat to monitor:\n");
            String currLine;
            while (menu.hasNextLine()) {
                //outputs first lines of .txt file for menu selection
                currLine = menu.nextLine();
                if (currLine.contains("Details")) {
                    System.out.println(currLine);
                }
            }
            System.out.println("Enter 00 to Go Back to Main Menu\n");
        } 
        
        habitatSelection = scnrHabitatInfo.nextLine(); //save user input to a variable
        
        return habitatSelection;
    }
    
    public String validCheck (String habitatSelection) throws FileNotFoundException {
        String currLine;
        Scanner scnrHabitatInfo = new Scanner(System.in); //used to read in user input
        boolean ckNum;
        ckNum = false;
        
        while (!ckNum) {
            try (Scanner check = new Scanner(HABITAT_DATA) //used to check animal selction against file
            ) {
                while (check.hasNextLine()) {
                    currLine = check.nextLine();
                    if (currLine.contains(habitatSelection)) {
                        ckNum = true;
                    }
                }   
                if (!ckNum) {
                    //if habitatSelection is not found, then error is output and user must enter selection again.
                    System.out.println("Error: Selection not found. Please try again");
                    habitatSelection = scnrHabitatInfo.nextLine();
                }
            }
        }
        return habitatSelection;
    }        
                
    
    public void getData (String habitatSelection) throws FileNotFoundException {
        try (Scanner data = new Scanner(HABITAT_DATA) //create new scanner to parse again
        ) {
            int i = 4;
            String currLine;
            
            while (data.hasNextLine()) {
                currLine = data.nextLine();
                if (currLine.contains(habitatSelection)) {
                    System.out.println(currLine);
                    while (i > 0) { //gets lines after user input is located
                        currLine = data.nextLine();
                        if (currLine.contains("*")) {
                            currLine = currLine.replace("*", "");
                            System.out.println("ALERT! " + currLine);
                            DialogBox box = new DialogBox();
                            box.dialogBoxHabitat(currLine);
                        }
                        else {
                            System.out.println(currLine);
                        }
                        --i;
                    }
                }
            }
            System.out.println();
        }
    }        
}
```
### Habitat Text File
```
Details on penguin habitat
Details on bird house
Details on aquarium
Details on lion habitat
Details on snake habitat

Habitat - Penguin
Temperature: Freezing
*****Food source: Fish in water running low
Cleanliness: Passed

Habitat - Bird
Temperature: Moderate
Food source: Natural from environment
Cleanliness: Passed

Habitat - Aquarium
Temperature: Varies with output temperature
Food source: Added daily
*****Cleanliness: Needs cleaning from algae

Habitat - Lion
Temperature: Moderate
Food source: Added daily
Cleanliness: Passed

Habitat - Snake
Temperature: Warm
Food source: Added every other day
Cleanliness: Passed
```

## Dialog Box Java Code
```
package ZooMonitoringSystem;


import javax.swing.*;

public class DialogBox { 
    public void dialogBoxAnimal(String alertMessage) {
        //alertMessage = " "; //variable to hold required messages containing *****
        JOptionPane.showMessageDialog(null, alertMessage, "Animal Alert", JOptionPane.INFORMATION_MESSAGE);
        
    }
    
    public void dialogBoxHabitat(String alertMessage) {
        //alertMessage = " "; //variable to hold required messages containing *****
        JOptionPane.showMessageDialog(null, alertMessage, "Habitat Alert", JOptionPane.INFORMATION_MESSAGE);
    }
}
```


