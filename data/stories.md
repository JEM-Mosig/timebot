## happy path
* greet
  - utter_greet
  - action_tell_time
* inform_city{"city": "San Francisco"}
  - action_tell_time
* thank
  - utter_youarewelcome
* bye
  - utter_goodbye

## happy path 2
* ask_time
  - action_tell_time
* inform_city{"city": "Stockholm"}
  - action_tell_time
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## happy path 3
* greet
  - utter_greet
* ask_time
  - action_tell_time
* deny
* inform_city{"city": "San Francisco"}
  - action_tell_time
* goodbye
  - utter_goodbye

## happy path 4
* greet
  - utter_greet
* inform_city{"city": "Berlin"}
  - action_tell_time
* goodbye
  - utter_goodbye

## happy path 5
* inform_city{"city": "Dunedin"}
  - action_tell_time
* thank
  - utter_youarewelcome
* inform_city{"city": "Dunedin"}
  - action_tell_time
* thank
  - utter_youarewelcome
* goodbye
  - utter_goodbye
