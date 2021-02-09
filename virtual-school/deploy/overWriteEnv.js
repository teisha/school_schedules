const fs = require("fs");

const getArg = (variableName) => {
  process.argv.forEach((val, index) => {
    console.log(`${index}: ${val}`);
  });
  const entry = process.argv.find((field) => field.startsWith(variableName));
  if (entry) {
    return entry.split("=")[1];
  } else {
    return null;
  }
};

const readBackendOutputs = () => {
  const outputs = JSON.parse(
    fs.readFileSync("./outputs.json").toString()
  );
  console.log(outputs)
  const backendOutputs = {};
  backendOutputs["ENVIRONMENT"] = getArg("ENVIRONMENT")
    ? getArg("ENVIRONMENT")
    : "development";
  backendOutputs["ISPROD"] =
    backendOutputs["ENVIRONMENT"] === "production" ||
    backendOutputs["ENVIRONMENT"] === "prod";
  outputs.forEach((o) => {
    console.log(`KEY: ${o.OutputKey}, VALUE: ${o.OutputValue}  `);
    backendOutputs[o.OutputKey.toUpperCase()] = o.OutputValue;
  });
  console.log("Outputs read: ", backendOutputs);
  return backendOutputs;
};

const performSubstitutions = (beforeText, backendOutputs) => {
  const substitutionRegex = /\${(.+)}/gi;
  const pattern = /\${([A-Z_]+)}/gi
  let replaceFunc = (match) => {
    let updatedString = match
    const matches = match.match(pattern)
    console.log(`${updatedString} ===> ${JSON.stringify(matches)}`)
    if (matches && matches.length === 1) {
      updatedString = backendOutputs[matches[0].replace(/^\${/, "").replace(/}$/, "").trim()]
      console.log(updatedString)
      return updatedString;
    }
    matches.forEach(matched => {
      let cfOutputKey = matched.replace(/^\${/, "").replace(/}$/, "").trim();
      // console.log(Object.keys(backendOutputs).includes(cfOutputKey) )
      console.log(`FIND KEY: ${cfOutputKey}, derived from ${matched} is: ${backendOutputs[cfOutputKey]} `);
      updatedString = updatedString.replace(matched, backendOutputs[cfOutputKey]);
      console.log(`UPDATED STRING IS:: ${updatedString} `)
    })
    return updatedString;
  };
  return beforeText.replace(substitutionRegex, replaceFunc);
};

const handler = () => {
  console.log(
    "READ BACKEND OUTPUTS FROM FILE AND CREATE FRONTEND environments.json"
  );
  const outputs = readBackendOutputs();

  let environment = { before: {}, after: null };
  environment.before = fs.readFileSync(
    "environment.cf.txt",
    "utf-8"
  );


  environment.after = performSubstitutions(environment.before, outputs);
  console.log("BEFORE:")
  console.log(JSON.stringify(environment.before, null, 2));
  console.log("AFTER:")
  console.log(JSON.stringify(environment.after, null, 2));

  fs.writeFileSync(
    `../environment/config.js`,
    environment.after
  );
};

handler();
