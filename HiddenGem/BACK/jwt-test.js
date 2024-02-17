const jwt = require("jsonwebtoken");

const secret = "this is my secret"

const token = jwt.sign(
  { user:100, nickname : "박승주" }, // payload 정의
  secret // 서버 비밀키
);

console.log(token);


const verifiedToken = jwt.verify(token, secret);

console.log(verifiedToken)