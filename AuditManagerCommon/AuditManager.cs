using System;
using System.Data.Entity;
using System.Linq;

namespace AuditManagerCommon
{
    public class AuditManager : DbContext
    {
        // Your context has been configured to use a 'AuditManager' connection string from your application's 
        // configuration file (App.config or Web.config). By default, this connection string targets the 
        // 'AuditManagerCommon.AuditManager' database on your LocalDb instance. 
        // 
        // If you wish to target a different database and/or database provider, modify the 'AuditManager' 
        // connection string in the application configuration file.
        public AuditManager()
            : base("name=AuditManager")
        {
        }

        // Add a DbSet for each entity type that you want to include in your model. For more information 
        // on configuring and using a Code First model, see http://go.microsoft.com/fwlink/?LinkId=390109.

         public virtual DbSet<Calendar_Item> Calendar_Items { get; set; }
    }

    //public class MyEntity
    //{
    //    public int Id { get; set; }
    //    public string Name { get; set; }
    //}
}