);

Const H=60; W=30; D=5;

Begin
  Write('Password: ');
  Readln(password);

  secret_string := 'lifeisnotaproblemtobesolved';

  if length(password) <> 21 then
  begin
    Writeln('I am very sorry :-(');
    Readln;
    exit;
  end;

  for i := 1 to length(password) do
  begin
    if byte(password[i]) xor byte(secret_string[i]) <> passwords[85][i] then
    begin
      Writeln('I am sorry :-(');
      Readln;
      exit;
    end
  end;

  ClrScr;

  Gd:=VGA;
  Gm:=VGAHi;
  InitGraph(Gd,Gm,driver);
  Gr:=GraphResult;

  ClearDevice;
  SetBkColor(Black);
  SetColor(LightGreen);
  SetLineStyle(SolidLn,0,ThickWidth);

