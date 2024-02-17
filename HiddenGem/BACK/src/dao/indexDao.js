const { pool } = require("../../config/database");

// 로그인 (회원검증)
exports.isValidUsers = async function (connection, userID, password) {
  const Query = `SELECT userIdx, nickname FROM Users where userID = ? and password = ? and status = 'A';`;
  const Params = [userID, password];

  const rows = await connection.query(Query, Params);

  return rows;
};

// 회원가입
exports.insertUsers = async function (connection, userID, password, nickname) {
  const Query = `insert into Users(userID, password, nickname) values (?,?,?);`;
  const Params = [userID, password, nickname];

  const rows = await connection.query(Query, Params);

  return rows;
};

exports.selectRestaurants = async function (connection, category) {
  const selectAllRestaurantsQuery = `SELECT title, address, category, videoUrl From Restaurants where status = 'A' ;`;
  const selectCategorizedRestaurantsQuery = `SELECT title, address, category, videoUrl From Restaurants where status = 'A' and category = ?;`;

  const Params = [category];

  const Query = category ? selectCategorizedRestaurantsQuery : selectAllRestaurantsQuery;

  const rows = await connection.query(Query, Params);

  return rows;
}


exports.exampleDao = async function (connection) {
  const Query = `SELECT * FROM Students;`;
  const Params = [];

  const rows = await connection.query(Query, Params);

  return rows;
};



