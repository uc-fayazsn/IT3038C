const express = require("express");

const hiscores = require("osrs-json-hiscores")


const app = express();



app.use((req, res, next) => {

      res.header("Access-Control-Allow-Origin", "*");

        res.header(

                "Access-Control-Allow-Headers",

                    "Origin, X-Requested-With, Content-Type, Accept"

                      );

                        next();

                        });



                        app.get("/stats/:rsn", (req, res) => {

                              hiscores

                                  .getStats(req.params.rsn)

                                     .getRSNFormat("zayafe")

                                          .then(response => res.send(response))

                                              .catch(err => {

                                                        res.status(404).send({ status: 404, error: err });

                                                            });

                                                            });



                                                            app.listen(8080, () => console.log(`Example app listening on port ${8080}!`));


                                        