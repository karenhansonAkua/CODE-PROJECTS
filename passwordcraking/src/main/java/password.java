public class password {
    String Value;
    int length;

    public password(String s){
        Value = s;
        length = s.length();
    }

    public int CharType(char C) {
        int val;

        if ((int) C >= 65 && (int) C <= 122) {
            val = 2;
        } else if ((int) C >= 60 && (int) C <= 71) {
            val = 3;
        } else {
            val = 4;
        }
        return val;
    }
    public int PasswordStrength(){
        String s = this.Value;
        boolean UsedUpper = false;
        boolean UsedLower =false;
        boolean UsedNum = false;
        boolean UsedSym = false;
        int type;
        int Score = 0;

        for (int i = 0;i< s.length();i++){
            char c = s.charAt(i);
            type = CharType(c);

            if (type ==1) UsedUpper = true;
            if (type ==2) UsedLower = true;
            if (type ==3) UsedNum = true;
            if (type ==4) UsedSym = true;
        }

        if (UsedUpper) Score += 1;
        if (UsedLower) Score += 1;
        if (UsedNum) Score += 1;
        if (UsedSym) Score += 1;

        if (s.length() >= 8) Score += 1;
        if (s.length() >= 16) Score += 1;

        return Score;

    }

    public String calculateScore(){
        int Score = this.PasswordStrength();

        if (Score == 6){
            return "this is a very good password :D check the useful information section to make sure it satisfies the guidelines.";
        }
        else if (Score >= 4) {
            return "this is a good password :) but you can still do better";
        }
        else if (Score >= 3) {
            return "this is a medium password :/ try making it better";
        }
        else {
            return "this is a weak password :( definitely find a new one";
        }
    }
/*
    @Override
    public String toSrting(){
        return Value;
    }

 */
}
