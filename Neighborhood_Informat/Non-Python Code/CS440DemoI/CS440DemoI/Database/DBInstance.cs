using System;
using System.Collections.Generic;
using System.Data;
using System.Data.OleDb;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS440DemoI.Database
{
    class DBInstance
    {
        private string crimesDB = @"Database\CrimesDB4Months.csv";
        private string censusDataDB = @"Database\CensusData.csv";
        private string tifDataDB = @"Database\TIFData.csv";

        private DataSet odcDataSet;
        public DataSet ODCDataSet
        {
            get { return this.odcDataSet; }
        }

        public DBInstance()
        {
            odcDataSet = new DataSet("ODCDataSet");

            DataTable crimesDataTable = CreateDataTableFromCSV("CrimesDataTable", crimesDB, true);
            odcDataSet.Tables.Add(crimesDataTable);

            DataTable censusDataTable = CreateDataTableFromCSV("CensusDataTable", censusDataDB, true);
            odcDataSet.Tables.Add(censusDataTable);

            DataTable tifDataTable = CreateDataTableFromCSV("TIFDataTable", tifDataDB, true);
            odcDataSet.Tables.Add(tifDataTable);
        }

        private DataTable CreateDataTableFromCSV(string DataTableName, string FilePath, bool ContainsHeaderRow)
        {
            DataTable dataTable = new DataTable(DataTableName);
            string header = ContainsHeaderRow ? "Yes" : "No";
            string pathOnly = Path.GetDirectoryName(FilePath);
            string fileName = Path.GetFileName(FilePath);
            string sql = @"SELECT * FROM [" + fileName + "]";
            using (OleDbConnection connection = new OleDbConnection(@"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + pathOnly + ";Extended Properties=\"Text;HDR=" + header + "\""))
            using (OleDbCommand command = new OleDbCommand(sql, connection))
            using (OleDbDataAdapter adapter = new OleDbDataAdapter(command))
            {
                adapter.Fill(dataTable);
            }
            return dataTable;
        }

        // This method basically populates the communities in the search selection drop down box.
        public EnumerableRowCollection<CommunityArea> GetCommunityAreasFromDataTable(Constants.DataTables DesiredDataTable)
        {
            var results =
                from row in ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable()
                orderby row.ItemArray[1] ascending
                select new CommunityArea() {
                    CommunityName = row.Field<string>("COMMUNITY AREA NAME"),
                    CommunityID = row.Field<int?>("Community Area Number") == null ? 0 : row.Field<int>("Community Area Number")
                };
            return results;
        }

        // This method basically populates the block names in the search selection drop down box.
        public IEnumerable<string> GetBlocksFromDataTable(Constants.DataTables DesiredDataTable)
        {
            IEnumerable<string> results =
                (from myRow in ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable()
                 select myRow.Field<string>("Block").Substring(myRow.Field<string>("Block").IndexOf(" ") + 3).ToUpper()).Distinct();
            results = results.OrderBy(block => block.ToString());
            return results;
        }

        // This method get all crime data for a specific community ID number.
        public IEnumerable<CrimeType> GetCommunityCrimeDataFromDataTable(Constants.DataTables DesiredDataTable, int CommunityID)
        {
            var results =
                from myRow in ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable()
                where myRow.Field<int?>("Community Area") == CommunityID
                select myRow;
            Console.WriteLine("Total community crimes: " + results.Count());
            Console.WriteLine("Total crimes: " + ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable().Count());
            float temp = (results.Count() / (float)ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable().Count());
            Console.WriteLine("Total neighborhood crime %: " + temp * 100 + "%");
            var groups =
                from grow in results
                group grow by grow.Field<string>("Primary Type") into g
                select new CrimeType() { CrimeName = g.Key, CrimeCount = g.Count(), Percentage = (g.Count() / (float)results.Count() * 100),
                                         TotalCommCrimes = results.Count(),
                                         TotalCrimes = ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable().Count(),
                                         TotalCrimePercentage = (results.Count() / (float)ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable().Count())};
            foreach (CrimeType ct in groups)
            {
                Console.WriteLine(ct.CrimeName + ": " + ct.CrimeCount.ToString() + "[" + ct.Percentage + "]");
            }
            return groups;
        }

        // This method get the per caipta income for a specific community ID number.
        public IEnumerable<int?> GetPerCapitaIncome(Constants.DataTables DesiredDataTable, int CommunityID)
        {
            IEnumerable<int?> results =
                from myRow in ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable()
                where myRow.Field<int?>("Community Area Number") == CommunityID
                select myRow.Field<int?>("PER CAPITA INCOME ");
            //Console.WriteLine("Per Capita Income: " + results.First().ToString());
            return results;
        }

        // This method gets the hardship index of a specific community ID number.
        public IEnumerable<int?> GetHardshipIndex(Constants.DataTables DesiredDataTable, int CommunityID)
        {
            IEnumerable<int?> results =
                from myRow in ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable()
                where myRow.Field<int?>("Community Area Number") == CommunityID
                select myRow.Field<int?>("HARDSHIP INDEX");
            Console.WriteLine("Hardship Index: " + results.First().ToString());
            return results;
        }

        public IEnumerable<decimal?> GetTIFBalance(Constants.DataTables DesiredDataTable, string block)
        {
            block = block.Substring(0, block.IndexOf(" "));
            IEnumerable<decimal?> results =
                from myRow in ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable()
                where myRow.Field<string>("TIF NAME").ToUpper().Contains(block)
                && myRow.Field<string>("DESCRIPTION") == "Beginning of year"
                select myRow.Field<decimal?>("AMOUNT");

            Console.WriteLine("TIF at the beginning of the year: $" + results.First().ToString() + ".00");
            return results;
        }

        public float GetCommunityCrimeDataPercentage(Constants.DataTables DesiredDataTable, int CommunityID)
        {
            var results =
                from myRow in ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable()
                where myRow.Field<int?>("Community Area") == CommunityID
                select myRow;

            float percentage = (results.Count() / (float)ODCDataSet.Tables[(int)DesiredDataTable].AsEnumerable().Count());
            Console.WriteLine("Total neighborhood crime %: " + percentage * 100 + "%");
            return percentage * 100;
        }
    }
}
