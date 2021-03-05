/**
 *  --------------------------------------------------------
 *      goal: to  a function in ceaser n+shift => encrypted text\
 * 
 *      author cryptograghi
 * 
 */




// declares not to be changed 
// letters is our string of letters
// map is a dictionaty map
// map shift is a new dictionary with the shift applied
// shift is the shift we want to use on our letters 


// these are the settting for the program 
// inmutable varibles 
const LETTERS = GetTable(false);
const MAP = MapKeys(LETTERS);
const SHIFT = 13;
const MAPSHIFT = MapShift(MAP, SHIFT);

 /**
  *  function: GetTable
  *  purpose: to get all ascii characters 
  *  parms: one bool filter if true will only show character a-z A-z 0-9
  *  false with show symbols etc..``  * 
  *
  */

function GetTable(filter)
{

    string  = ''; 

    if (filter === true)
    {
        for (var i = 32; i <= 126; i++)
        {
            // returns filtered list based on the char code
             if(i >= 65 && i <= 90)
            {
                string += String.fromCharCode(i);
            } 
            else if( i >= 97 && i <= 122)
            {
                string += String.fromCharCode(i);
            } else {

            }
        
        }
            // return strings from ascii codes 
    } else {
            for(var i = 32; i <= 126; i++)
            {
            string += String.fromCharCode(i);
            }
        // return strings from ascii codes 
    }
        return string;
}

// tests 
//GetTable(true);
//GetTable(false);
/*
 *  function: map function 
 * 
 *  purpose: to create a dictionary map that 
 *  we will use later [a] = a
 *  output: [a] = a [b] = b etc....
 * 
 */ 

function MapKeys(input)
{
    // create object that kill contain the keys
    var map =   { };

    for (let i = 0; i < input.length; i++)
    {
            map[input[i]] = input[i];
      
    }
    return map;
} 

// tests 

//console.log(MapKeys(GetTable(true)));

/* output:
  A: 'A',
  B: 'B',
  C: 'C',
  D: 'D',
  E: 'E',
  F: 'F',
  G: 'G',
  H: 'H',
  I: 'I',
  J: 'J',
  K: 'K',
  L: 'L',
  M: 'M',
  N: 'N',
  O: 'O',
  P: 'P',
  Q: 'Q',
  R: 'R',
  S: 'S',
  T: 'T',
  U: 'U',
  V: 'V',
  W: 'W',
  X: 'X',
  Y: 'Y',
  Z: 'Z',
  a: 'a',
  b: 'b',
  c: 'c',
  d: 'd',
  e: 'e',
  f: 'f',
  g: 'g',
  h: 'h',
  i: 'i',
  j: 'j',
  k: 'k',
  l: 'l',
  m: 'm',
  n: 'n',
  o: 'o',
  p: 'p',
  q: 'q',
  r: 'r',
  s: 's',
  t: 't',
  u: 'u',
  v: 'v',
  w: 'w',
  x: 'x',
  y: 'y',
  z: 'z' */

/**
 * 
 * FUNCTION MAPSHIFT
 * PURPOSE: TO use a the letter object we created with MAP KEYS
 * AND CREATE A NEW DICTIONARY WILL RECPECTED SHIFT A = C 
 * BUT WILL ONLY NEED THE ORGINAL
 */

function MapShift(currentMap, shift)
{
    // lets create a new map of the new dictonarys now 

    for (keys in currentMap)
    {
        // check if the keys are actually valid

         if (currentMap.hasOwnProperty(keys) == true)
         { 
             let ASCII = keys.charCodeAt(keys);
              // apply the shift 
              if (ASCII >= 65 && ASCII <= 90)
              {
                  // apply shift 
                  let SHIFTASCII = ASCII + shift;
                  // check number
                  if (SHIFTASCII > 90)
                  {
                      // dont change just minus the alphebet
                      SHIFTASCII = SHIFTASCII - 26;
                      currentMap[keys] = String.fromCharCode(SHIFTASCII);
                  } else {
                      // add shift to our map 
                      currentMap[keys] = String.fromCharCode(SHIFTASCII);
                  }  
              } 
                else if (ASCII >= 97 && ASCII <= 122)
                {
                    // apply shift for next squence of characters 
                   let SHIFTASCII = ASCII + shift;
                   // trigger 
                   if (SHIFTASCII > 122)
                   {
                       // above our thresehold 
                       SHIFTASCII = SHIFTASCII - 26;
                       currentMap[keys] = String.fromCharCode(SHIFTASCII);
                   }
                   else
                   {
                        currentMap[keys] = String.fromCharCode(SHIFTASCII);
                   }

                }      
            
         }
    }
    return currentMap;
}
// TESTS
//console.log(MapShift(MAP, SHIFT));


/*
output:
  '0': '0',
  '1': '1',
  '2': '2',
  '3': '3',
  '4': '4',
  '5': '5',
  '6': '6',
  '7': '7',
  '8': '8',
  '9': '9',
  ' ': ' ',
  '!': '!',
  '"': '"',
  '#': '#',
  '$': '$',
  '%': '%',
  '&': '&',
  "'": "'",
  '(': '(',
  ')': ')',
  '*': '*',
  '+': '+',
  ',': ',',
  '-': '-',
  '.': '.',
  '/': '/',
  ':': ':',
  ';': ';',
  '<': '<',
  '=': '=',
  '>': '>',
  '?': '?',
  '@': '@',
  A: 'N',
  B: 'O',
  C: 'P',
  D: 'Q',
  E: 'R',
  F: 'S',
  G: 'T',
  H: 'U',
  I: 'V',
  J: 'W',
  K: 'X',
  L: 'Y',
  M: 'Z',
  N: 'A',
  O: 'B',
  P: 'C',
  Q: 'D',
  R: 'E',
  S: 'F',
  T: 'G',
  U: 'H',
  V: 'I',
  W: 'J',
  X: 'K',
  Y: 'L',
  Z: 'M',
  '[': '[',
  '\\': '\\',
  ']': ']',
  '^': '^',
  _: '_',
  '`': '`',
  a: 'n',
  b: 'o',
  c: 'p',
  d: 'q',
  e: 'r',
  f: 's',
  g: 't',
  h: 'u',
  i: 'v',
  j: 'w',
  k: 'x',
  l: 'y',
  m: 'z',
  n: 'a',
  o: 'b',
  p: 'c',
  q: 'd',
  r: 'e',
  s: 'f',
  t: 'g',
  u: 'h',
  v: 'i',
  w: 'j',
  x: 'k',
  y: 'l',
  z: 'm',
  '{': '{',
  '|': '|',
  '}': '}',
  '~': '~'

*/
/**
 * 
 * function: to pack the input => the data to encrypt
 * 
 * purpose: to pack the function to encrypt the message based on the shift level ie level of N
*/


function Pack(input, MAPSHIFT)
{
    // ENCRYPT DATA AND PUSH ENCRYPTED STRING TO VAR SEED 

    SEED = ""
    for (let i = 0; i <= input.length; i++)
    {

        for (letters in MAPSHIFT)
        {
            // check if our object name matches the letters 
            // push into seed if there is a match 
            if (letters === input[i])
            {
             SEED += MAPSHIFT[letters];
            }

        }
    }
    
  return SEED;
}
// TESTS
//console.log(Pack("TST", MAPSHIFT));


// output => GFG

/*
    function: unPACK
    purpose: to decrypt the data 
    input => is an encrypted string 
    MAPSHIFT => is the SHIFT APPLIED TO encrypted data

*/




function unPack(input, MAPSHIFT)
{
    /// varible to push decrypted string into 
    UNPACKED_SEED = "";
    for (let x = 0; x < input.length; x++)
    {
        // MAPSHIFT CONTAINER OUR DICTIONARY OF LETTERS
        // DECLARE ARE AT TOP OF FILE
        for (letters in MAPSHIFT)
        {
        // search though all the letters 
            if (MAPSHIFT[letters] == input[x])
            {
                UNPACKED_SEED += letters;
            }
        }
    }
    return UNPACKED_SEED;
}


//var test = Pack("STRINGS", MAPSHIFT);
//console.log(test);
//console.log(unPack(test, MAPSHIFT));

/*
    output:
 test =>   FGEVATF
 test put into unpack function =>   STRINGS
*/


/**
 *  function:  boomboom
 *  purpose: to crack the encryption using all possible matches
 *  
 */



function BoomBoom(data, shift_limit)
{
    
    console.log("starting the cracking:......................");
    var list =  [];
    for (let i = 0; i < shift_limit; i++)
    {
        // call the map
       const BOOM = MapShift(MAP, i);
       console.log("------------------------------------------");
       console.log("Starting attempt:", i);
       Guess = unPack(data, BOOM);
       list.push(Guess);
       console.log(Guess);
       console.log("Finished attempted:", i)
       console.log("-------------------------------------------");
    }

    console.log("Possible Matches: ")
    for (let x = 0; x < list.length; x++)
    {
        if (list[x] != "")
        {
        console.log("try: ", x, list[x]);
        }
    }
    return "FINISHED!";
}

// tests
 test = Pack("my super secret string", MAPSHIFT);
 BoomBoom(test, 26);

 /*
  output:

 Possible Matches:
try:  0 zl fhcre frperg fgevat
try:  1 yk egbqd eqodqf efduzs
try:  2 xj dfapc dpncpe dectyr
try:  3 wi cezob combod cdbsxq
try:  4 vh bdyna bnlanc bcarwp
try:  5 ug acxmz amkzmb abzqvo
try:  6 tf zbwly zljyla zaypun
try:  7 se yavkx ykixkz yzxotm
try:  8 rd xzujw xjhwjy xywnsl
try:  9 qc wytiv wigvix wxvmrk
try:  10 pb vxshu vhfuhw vwulqj
try:  11 oa uwrgt ugetgv uvtkpi
try:  12 nz tvqfs tfdsfu tusjoh
try:  13 my super secret string  bingo :)
try:  14 lx rtodq rdbqds rsqhmf
try:  15 kw qsncp qcapcr qrpgle
try:  16 jv prmbo pbzobq pqofkd
try:  17 iu oqlan oaynap opnejc
try:  18 ht npkzm nzxmzo nomdib
try:  19 gs mojyl mywlyn mnlcha
try:  20 fr lnixk lxvkxm lmkbgz
try:  21 eq kmhwj kwujwl kljafy
try:  22 dp jlgvi jvtivk jkizex
try:  23 co ikfuh iushuj ijhydw
try:  24 bn hjetg htrgti higxcv
try:  25 am gidsf gsqfsh ghfwbu
 */


 // enjoy
