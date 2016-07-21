int PIEZOPIN = 5;

// One octave of notes between A4 and A5
int note_C3 = 131;
int note_D3 = 147;
int note_E3 = 165;
int note_G3 = 196;
int note_C4 = 262;
int note_D4 = 294;
int note_E4 = 330;
int note_F4 = 349;
int note_G4 = 392;
int note_A4 = 440;
int note_B4 = 494;
int note_C5 = 523;
int note_D5 = 587;
int note_E5 = 659;
int note_F5 = 698;
int note_G5 = 784;
int note_A5 = note_A4 * 2;
int note_B5 = note_B4 * 2;

// note lengths defined here
long whole_note = 1600; // change tempo by changing duration of one measure
long half_note = whole_note / 2;
long quarter_note = whole_note / 4;
long eighth_note = whole_note / 8;
long sixteenth_note = whole_note / 16;

// WRITE YOUR SONG HERE

  
// if you want there to be silence between notes,
//   staccato should be true
//song list
int song[42][2] = {
  {note_C4, eighth_note}, {note_C5, eighth_note}, {note_C4, eighth_note}, {note_C5, eighth_note}, {note_B4, eighth_note}, {note_C4, eighth_note}, 
  {note_B4, eighth_note}, {note_G4, half_note + quarter_note}, {note_E4, quarter_note}, {note_D4, eighth_note}, {note_C4, eighth_note}, {note_C5, eighth_note}, {note_C4, eighth_note}, 
  {note_C5, eighth_note}, {note_B4, eighth_note}, {note_C4, eighth_note}, {note_B4, eighth_note}, {note_G4, eighth_note + quarter_note}, {note_C4, eighth_note}, {note_G4, eighth_note}, 
  {note_C4, eighth_note}, {note_E4, eighth_note}, {note_F4, eighth_note}, {note_E4, eighth_note}, {note_C4, eighth_note}, {note_C5, eighth_note}, {note_C4, eighth_note}, 
  {note_C5, eighth_note}, {note_B4, eighth_note}, {note_C4, eighth_note}, {note_B4, eighth_note}, {note_G4, quarter_note +half_note}, {note_E4, quarter_note}, {note_D4, eighth_note}, 
  {note_C4, eighth_note}, {note_E4, eighth_note}, {note_D4, eighth_note}, {note_C4, eighth_note}, {note_D4, eighth_note}, {note_C4, eighth_note}, {note_G4,quarter_note + half_note}, 
  {note_D4, quarter_note}};
      
//  {note_G3, eighth_note}, {note_G3, eighth_note}, {note_G3, eighth_note}, {note_G3, quarter_note}, {note_D3, quarter_note}, {note_D3, half_note}, 
//  {note_E3, quarter_note}, {note_D3, quarter_note}, {note_D3, quarter_note}, {note_E3, eighth_note}, {note_D3, eighth_note}, {note_D3, eighth_note}, {note_D3, eighth_note}, 
//  {note_C3, eighth_note}, {note_E3, quarter_note}, {note_C3, quarter_note + eighth_note}};


void setup() {
  pinMode(PIEZOPIN, OUTPUT);
}

void loop() {  
  //PLAY YOUR SONG HERE  
  for(int i = 0; i < 41; i++) {
    tone(PIEZOPIN, song[i][0], song[i][1]);
    delay(song[i][1]);
  }
  delay(1000);
}

