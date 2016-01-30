#include <my_global.h>
#include <mysql.h>

void finish_with_error(MYSQL *con)
{
  fprintf(stderr, "%s\n", mysql_error(con));
  mysql_close(con);
  exit(1);        
}

int main(int argc, char **argv)
{
  MYSQL *con = mysql_init(NULL);
  
  if (con == NULL) 
  {
      fprintf(stderr, "%s\n", mysql_error(con));
      exit(1);
  }  
    if (mysql_real_connect(con, "localhost", "root", "root", 
          "http2", 0, NULL, 0) == NULL) 
  {
      finish_with_error(con);
  }    
    char select_sql[256];

    char * test_uri ="0.0.0.0";
    printf("%s",test_uri);

    snprintf(select_sql,256,"select * from result where uri = '%s'",test_uri);
    
    printf("%s",select_sql);
    if(mysql_query(con,select_sql)){
      finish_with_error(con);
    }

    MYSQL_RES *confres = mysql_store_result(con);
    int totalrows = mysql_num_rows(confres);

    printf("%d",totalrows);



  
  if (mysql_query(con, "DROP TABLE IF EXISTS Cars")) {
      finish_with_error(con);
  }
  
  if (mysql_query(con, "CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")) {      
      finish_with_error(con);
  }


  

  mysql_close(con);
  exit(0);
}
