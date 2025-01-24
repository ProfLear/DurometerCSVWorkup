import marimo

__generated_with = "0.10.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    from codechembook.quickPlots import quickScatter
    from plotly.subplots import make_subplots
    import numpy as np
    from scipy.odr import ODR, Model, RealData

    # Define the linear model
    def linear_model(params, x):
        m, c = params  # Slope (m) and intercept (c)
        return m * x + c

    model = Model(linear_model)
    return (
        Model,
        ODR,
        RealData,
        linear_model,
        make_subplots,
        mo,
        model,
        np,
        quickScatter,
    )


@app.cell
def _(np):
    #import data

    # read in data
    data = np.genfromtxt(r"G:/My Drive/PennState/Research/Manuscripts/2025/Anthony Physical Properties/Hardness_Soxhlet Data - 2025 CB-PDMS Mechanical Paper .csv",
                         delimiter = ",",
                         unpack = True,
                         skip_header = 1,
                         #usecols = [1],
                         )

    # Shore hardness
    LRO_hardness = data[1][~np.isnan(data[1])]
    LRO_hardness_error = data[2][~np.isnan(data[2])]
    LRO_density = data[3][~np.isnan(data[3])]
    LRO_density_error = data[4][~np.isnan(data[4])]

    RLO_hardness = data[5][~np.isnan(data[5])]
    RLO_hardness_error = data[6][~np.isnan(data[6])]
    RLO_density = data[7][~np.isnan(data[7])]
    RLO_density_error = data[8][~np.isnan(data[8])]

    # cross link density
    LRO_xlink = data[9][~np.isnan(data[9])]
    LRO_xlink_error = data[10][~np.isnan(data[10])]
    RLO_xlink = data[11][~np.isnan(data[11])]
    RLO_xlink_error = data[12][~np.isnan(data[12])]

    # cross gel fraction
    LRO_gel = data[13][~np.isnan(data[13])]
    LRO_gel_error = data[14][~np.isnan(data[14])]
    RLO_gel = data[15][~np.isnan(data[15])]
    RLO_gel_error = data[16][~np.isnan(data[16])]

    # cross Young's modulous
    LRO_youngs = data[17][~np.isnan(data[17])]
    LRO_youngs_error = data[18][~np.isnan(data[18])]
    RLO_youngs = data[19][~np.isnan(data[19])]
    RLO_youngs_error = data[20][~np.isnan(data[20])]

    #%
    all_hardness = np.append(LRO_hardness, RLO_hardness)
    all_hardness_error = np.append(LRO_hardness_error, RLO_hardness_error)
    all_density = np.append(LRO_density, RLO_density)
    all_density_error = np.append(LRO_density_error, RLO_density_error)
    return (
        LRO_density,
        LRO_density_error,
        LRO_gel,
        LRO_gel_error,
        LRO_hardness,
        LRO_hardness_error,
        LRO_xlink,
        LRO_xlink_error,
        LRO_youngs,
        LRO_youngs_error,
        RLO_density,
        RLO_density_error,
        RLO_gel,
        RLO_gel_error,
        RLO_hardness,
        RLO_hardness_error,
        RLO_xlink,
        RLO_xlink_error,
        RLO_youngs,
        RLO_youngs_error,
        all_density,
        all_density_error,
        all_hardness,
        all_hardness_error,
        data,
    )


@app.cell
def _():
    # plot variables

    LRO_color = f"rgba(211, 96, 39, 1)"
    LRO_fill_color = f"rgba(211, 96, 39, 0.2)"
    RLO_color = f"rgba(162, 55, 104, 1)"
    RLO_fill_color = f"rgba(162, 55, 104, 0.2)"

    tick_labels = ["bowl", "inner-lip", "lip", "bulk"]
    return LRO_color, LRO_fill_color, RLO_color, RLO_fill_color, tick_labels


@app.cell
def _(
    LRO_color,
    LRO_density,
    LRO_density_error,
    RLO_color,
    RLO_density,
    RLO_density_error,
    make_subplots,
    tick_labels,
):
    # plot of density

    density_plot = make_subplots()

    density_plot.add_scatter(x = [2, 3, 4, 5], y = RLO_density-RLO_density_error, mode = "lines", 
                             line = dict(width = 0),
                             showlegend = False)
    density_plot.add_scatter(x = [2, 3, 4, 5], y = RLO_density+RLO_density_error, mode = "lines", 
                             fill='tonexty', 
                             fillcolor = "rgba(162, 55, 104, 0.2)",
                             line = dict(width = 0),
                             showlegend = False)
    density_plot.add_scatter(x = [2, 3, 4, 5], y = RLO_density,
                             marker = dict(size = 10, symbol = "diamond", color = RLO_color),
                             line = dict(dash = "dash", color = RLO_color),
                             showlegend = False)


    density_plot.add_scatter(x = [2, 3, 4, 5], y = LRO_density-LRO_density_error, mode = "lines", 
                             line = dict(width = 0),
                             showlegend = False)
    density_plot.add_scatter(x = [2, 3, 4, 5], y = LRO_density+LRO_density_error, mode = "lines", 
                             fill='tonexty', 
                             fillcolor = "rgba(211, 96, 39, 0.2)",
                             line = dict(width = 0),
                             showlegend = False)
    density_plot.add_scatter(x = [2, 3, 4, 5], y = LRO_density,
                             marker = dict(size = 10, symbol = "circle", color = LRO_color),
                             line = dict(dash = "dashdot", color = LRO_color),
                             showlegend = False)

    density_plot.add_annotation(text = "LRO", font=dict(color = LRO_color),
                                x = 1.95, y = LRO_density[0],
                                xanchor = "right",
                                showarrow = False)
    density_plot.add_annotation(text = "RLO", font=dict(color = RLO_color),
                                x = 1.95, y = RLO_density[0],
                                xanchor = "right",
                                showarrow = False)


    density_plot.update_xaxes(title = "position", 
                              tickvals = [2, 3, 4, 5], 
                              ticktext = tick_labels)
    density_plot.update_yaxes(title = "density /g/mL",
                              nticks = 4)
    density_plot.update_layout(template = "simple_white", width = 3.3*300, height = 2*300)
    density_plot.show("png")
    return (density_plot,)


@app.cell
def _(
    LRO_color,
    LRO_gel,
    LRO_gel_error,
    LRO_xlink,
    LRO_xlink_error,
    RLO_color,
    RLO_gel,
    RLO_gel_error,
    RLO_xlink,
    RLO_xlink_error,
    make_subplots,
    tick_labels,
):
    # plot of swell test things

    sohxlet_plot = make_subplots(rows = 2, cols = 1)

    # gel fraction
    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = RLO_gel,
                             marker = dict(size = 10, symbol = "diamond", color = RLO_color),
                             line = dict(dash = "dash", color = RLO_color),
                             showlegend = False,
                          row = 1, col = 1)
    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = RLO_gel-RLO_gel_error, mode = "lines", 
                             line = dict(width = 0),
                             showlegend = False,
                          row = 1, col = 1)
    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = RLO_gel+RLO_gel_error, mode = "lines", 
                             fill='tonexty', 
                             fillcolor = "rgba(162, 55, 104, 0.2)",
                             line = dict(width = 0),
                             showlegend = False,
                          row = 1, col = 1)

    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = LRO_gel,
                             marker = dict(size = 10, symbol = "circle", color = LRO_color),
                             line = dict(dash = "dashdot", color = LRO_color),
                             showlegend = False,
                          row = 1, col = 1)
    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = LRO_gel-LRO_gel_error, mode = "lines", 
                             line = dict(width = 0),
                             showlegend = False,
                          row = 1, col = 1)
    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = LRO_gel+LRO_gel_error, mode = "lines", 
                             fill='tonexty', 
                             fillcolor = "rgba(211, 96, 39, 0.2)",
                             line = dict(width = 0),
                             showlegend = False,
                          row = 1, col = 1)

    sohxlet_plot.add_annotation(text = "LRO", font=dict(color = LRO_color),
                                x = 1.95, y = LRO_gel[0],
                                xanchor = "right",
                                showarrow = False,
                             row = 1, col = 1)
    sohxlet_plot.add_annotation(text = "RLO", font=dict(color = RLO_color),
                                x = 1.95, y = RLO_gel[0],
                                xanchor = "right",
                                showarrow = False,
                             row = 1, col = 1)

    sohxlet_plot.update_yaxes(title = "gel fraction / w/w",
                              nticks = 4,
                           row = 1, col = 1)

    sohxlet_plot.update_xaxes(title = "position", 
                              tickvals = [2, 3, 4, 5], 
                              ticktext = tick_labels)


    #cross link density
    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = RLO_xlink,
                             marker = dict(size = 10, symbol = "diamond", color = RLO_color),
                             line = dict(dash = "dash", color = RLO_color),
                             showlegend = False,
                          row = 2, col = 1)
    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = RLO_xlink-RLO_xlink_error, mode = "lines", 
                             line = dict(width = 0),
                             showlegend = False,
                          row = 2, col = 1)
    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = RLO_xlink+RLO_xlink_error, mode = "lines", 
                             fill='tonexty', 
                             fillcolor = "rgba(162, 55, 104, 0.2)",
                             line = dict(width = 0),
                             showlegend = False,
                          row = 2, col = 1)

    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = LRO_xlink,
                             marker = dict(size = 10, symbol = "circle", color = LRO_color),
                             line = dict(dash = "dashdot", color = LRO_color),
                             showlegend = False,
                          row = 2, col = 1)
    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = LRO_xlink-LRO_xlink_error, mode = "lines", 
                             line = dict(width = 0),
                             showlegend = False,
                          row = 2, col = 1)
    sohxlet_plot.add_scatter(x = [2, 3, 4, 5], y = LRO_xlink+LRO_xlink_error, mode = "lines", 
                             fill='tonexty', 
                             fillcolor = "rgba(211, 96, 39, 0.2)",
                             line = dict(width = 0),
                             showlegend = False,
                          row = 2, col = 1)

    sohxlet_plot.add_annotation(text = "LRO", font=dict(color = LRO_color),
                                x = 1.95, y = LRO_xlink[0],
                                xanchor = "right",
                                showarrow = False,
                             row = 2, col = 1)
    sohxlet_plot.add_annotation(text = "RLO", font=dict(color = RLO_color),
                                x = 1.95, y = RLO_xlink[0],
                                xanchor = "right",
                                showarrow = False,
                             row = 2, col = 1)

    sohxlet_plot.update_yaxes(title = "cross link density / mmol/mL<sup>-1</sup>",
                              nticks = 4,
                           row = 2, col = 1)

    sohxlet_plot.update_xaxes(title = "position", 
                              tickvals = [2, 3, 4, 5], 
                              ticktext = tick_labels)



    sohxlet_plot.update_layout(template = "simple_white", width = 3.3*300, height = 3*300)
    sohxlet_plot.show("png")
    return (sohxlet_plot,)


@app.cell
def _(
    LRO_density,
    LRO_density_error,
    LRO_gel,
    LRO_gel_error,
    LRO_hardness,
    LRO_hardness_error,
    LRO_xlink,
    LRO_xlink_error,
    ODR,
    RLO_density,
    RLO_density_error,
    RLO_gel,
    RLO_gel_error,
    RLO_hardness,
    RLO_hardness_error,
    RLO_xlink,
    RLO_xlink_error,
    RealData,
    model,
    np,
):
    # hardness vs density
    def orthogonal_fit (LRO, RLO, xname, yname):
        '''
        Accept two disctionaries
        '''
        # Create RealData object with errors
        LRO_data_to_fit = RealData(
            LRO["x data"], 
            LRO["y data"], 
            sx=LRO["x data error"], 
            sy=LRO["y data error"]
            )
        RLO_data_to_fit = RealData(
            RLO["x data"], 
            RLO["y data"], 
            sx=RLO["x data error"], 
            sy=RLO["y data error"]
            )
        all_data_to_fit = RealData(
            np.append(LRO["x data"], RLO["x data"]), 
            np.append(LRO["y data"], RLO["y data"]), 
            sx=np.append(LRO["x data error"], RLO["x data error"]), 
            sy=np.append(LRO["y data error"], RLO["y data error"])
            )

        slope_estimate = (LRO["y data"][0] - LRO["y data"][-1])/(LRO["x data"][0] - LRO["x data"][-1])
        intercept_estimate = LRO["y data"][0] - slope_estimate*LRO["x data"][0]

        # Set up ODR with the model and data
        LRO_odr = ODR(LRO_data_to_fit, model, beta0=[slope_estimate, intercept_estimate])
        RLO_odr = ODR(RLO_data_to_fit, model, beta0=[slope_estimate, intercept_estimate])
        all_odr = ODR(all_data_to_fit, model, beta0=[slope_estimate, intercept_estimate])  # Initial guess for slope and intercept

        # Run the regression
        LRO_output = LRO_odr.run()
        RLO_output = RLO_odr.run()
        all_output = all_odr.run()

        # Extract the results
        LRO_m, LRO_c = LRO_output.beta  # Fitted slope and intercept
        LRO_m_err, LRO_c_err = np.sqrt(np.diag(LRO_output.cov_beta))

        RLO_m, RLO_c = RLO_output.beta  # Fitted slope and intercept
        RLO_m_err, RLO_c_err = np.sqrt(np.diag(RLO_output.cov_beta))

        all_m, all_c = all_output.beta  # Fitted slope and intercept
        all_m_err, all_c_err = np.sqrt(np.diag(all_output.cov_beta))  # Standard errors

        LRO_result = {}
        LRO_result["x data"] = LRO["x data"]
        LRO_result["x data error"] = LRO["x data error"]
        LRO_result["y data"] = LRO["y data"]
        LRO_result["y data error"] = LRO["y data error"]
        LRO_result["slope"] = LRO_m
        LRO_result["intercept"] = LRO_c
        LRO_result["slope error"] = LRO_m_err
        LRO_result["intercept error"] = LRO_c_err
        

        RLO_result = {}
        RLO_result["x data"] = RLO["x data"]
        RLO_result["x data error"] = RLO["x data error"]
        RLO_result["y data"] = RLO["y data"]
        RLO_result["y data error"] = RLO["y data error"]
        RLO_result["slope"] = RLO_m
        RLO_result["intercept"] = RLO_c
        RLO_result["slope error"] = RLO_m_err
        RLO_result["intercept error"] = RLO_c_err

        all_result = {}
        all_result["x data"] = np.append(LRO["x data"], RLO["x data"])
        all_result["x data error"] = np.append(LRO["x data error"], RLO["x data error"])
        all_result["y data"] = np.append(LRO["y data"], RLO["y data"])
        all_result["y data error"] = np.append(LRO["y data error"], RLO["y data error"])
        all_result["slope"] = all_m
        all_result["intercept"] = all_c
        all_result["slope error"] = all_m_err
        all_result["intercept error"] = all_c_err

        # Compute R^2 for LRO
        LRO_y_pred = LRO_m * np.array(LRO["x data"]) + LRO_c
        LRO_y_mean = np.mean(LRO["y data"])
        SS_tot_LRO = np.sum((LRO["y data"] - LRO_y_mean) ** 2)
        SS_res_LRO = np.sum((LRO["y data"] - LRO_y_pred) ** 2)
        LRO_R2 = 1 - (SS_res_LRO / SS_tot_LRO)
        LRO_result["R^2"] = LRO_R2

        # Compute R^2 for RLO
        RLO_y_pred = RLO_m * np.array(RLO["x data"]) + RLO_c
        RLO_y_mean = np.mean(RLO["y data"])
        SS_tot_RLO = np.sum((RLO["y data"] - RLO_y_mean) ** 2)
        SS_res_RLO = np.sum((RLO["y data"] - RLO_y_pred) ** 2)
        RLO_R2 = 1 - (SS_res_RLO / SS_tot_RLO)
        RLO_result["R^2"] = RLO_R2

        # Compute R^2 for all data
        all_y_pred = all_m * np.array(all_result["x data"]) + all_c
        all_y_mean = np.mean(all_result["y data"])
        SS_tot_all = np.sum((all_result["y data"] - all_y_mean) ** 2)
        SS_res_all = np.sum((all_result["y data"] - all_y_pred) ** 2)
        all_R2 = 1 - (SS_res_all / SS_tot_all)
        all_result["R^2"] = all_R2


        return {"LRO result": LRO_result, "RLO result": RLO_result, "all result": all_result, "axes": {"x name": xname, "y name": yname}}


    # perform the fit

    density_v_hardness_results = orthogonal_fit(
        {"x data" : LRO_density, "y data" : LRO_hardness, "x data error" : LRO_density_error, "y data error" : LRO_hardness_error},
        {"x data" : RLO_density, "y data" : RLO_hardness, "x data error" : RLO_density_error, "y data error" : RLO_hardness_error},
        "density",
        "hardness"
        )

    crosslink_v_hardness_results = orthogonal_fit(
        {"x data" : LRO_xlink, "y data" : LRO_hardness, "x data error" : LRO_xlink_error, "y data error" : LRO_hardness_error},
        {"x data" : RLO_xlink, "y data" : RLO_hardness, "x data error" : RLO_xlink_error, "y data error" : RLO_hardness_error},
        "cross link density",
        "hardness"
        )

    gel_v_hardness_results = orthogonal_fit(
        {"x data" : LRO_gel, "y data" : LRO_hardness, "x data error" : LRO_gel_error, "y data error" : LRO_hardness_error},
        {"x data" : RLO_gel, "y data" : RLO_hardness, "x data error" : RLO_gel_error, "y data error" : RLO_hardness_error},
        "gel fraction",
        "hardness"
        )

    crosslink_v_density_results = orthogonal_fit(
        {"x data" : LRO_xlink, "y data" : LRO_density, "x data error" : LRO_xlink_error, "y data error" : LRO_density_error},
        {"x data" : RLO_xlink, "y data" : RLO_density, "x data error" : RLO_xlink_error, "y data error" : RLO_density_error},
        "cross link density",
        "density"
        )
    return (
        crosslink_v_density_results,
        crosslink_v_hardness_results,
        density_v_hardness_results,
        gel_v_hardness_results,
        orthogonal_fit,
    )


@app.cell
def _(
    LRO_color,
    RLO_color,
    crosslink_v_density_results,
    crosslink_v_hardness_results,
    density_v_hardness_results,
    gel_v_hardness_results,
    make_subplots,
    np,
):
    for result in [density_v_hardness_results, crosslink_v_hardness_results, gel_v_hardness_results, crosslink_v_density_results]:
        fitplot = make_subplots()
        fitplot.add_scatter(x = result["LRO result"]["x data"], 
                            y = result["LRO result"]["y data"], 
                            mode = "markers",
                            marker = dict(symbol = "circle", color = LRO_color, size = 10),
                            error_x=dict(
                                type='data',
                                array=result["LRO result"]["x data error"],
                                visible=True  # Show error bars
                                ),
                            error_y=dict(
                                type='data',
                                array=result["LRO result"]["y data error"],
                                visible=True  # Show error bars
                                ),
                            showlegend = False)
        fitplot.add_scatter(x = result["RLO result"]["x data"], 
                            y = result["RLO result"]["y data"], 
                            mode = "markers",
                            marker = dict(symbol = "circle", color = RLO_color, size = 10),
                            error_x=dict(
                                type='data',
                                array=result["RLO result"]["x data error"],
                                visible=True  # Show error bars
                                ),
                            error_y=dict(
                                type='data',
                                array=result["RLO result"]["y data error"],
                                visible=True  # Show error bars
                                ),
                            showlegend = False)

        # now the fit...
        simx = np.array([
            min(np.min(result["LRO result"]["x data"]), np.min(result["RLO result"]["x data"])),
            max(np.max(result["LRO result"]["x data"]), np.max(result["RLO result"]["x data"]))
            ])

        LRO_y = result["LRO result"]["slope"]*simx + result["LRO result"]["intercept"]
        RLO_y = result["RLO result"]["slope"]*simx + result["RLO result"]["intercept"]
        all_y = result["all result"]["slope"]*simx + result["all result"]["intercept"]

        fitplot.add_scatter(x = simx, 
                            y = LRO_y,
                            mode = "lines",
                            line = dict(dash = "dashdot", color = LRO_color),
                            showlegend = False)
        fitplot.add_scatter(x = simx, 
                            y = RLO_y,
                            mode = "lines",
                            line = dict(dash = "dash", color = RLO_color), 
                            showlegend = False)
        fitplot.add_scatter(x = simx, 
                            y = all_y, 
                            mode = "lines",
                            line = dict(color = "black"), 
                            showlegend = False)

        # now annotate
        fitplot.add_annotation(text = f"slope = {int(result["LRO result"]["slope"])} +- {int(result["LRO result"]["slope error"])}<br>R<sup>2</sup>={result["LRO result"]["R^2"]:.3f}", 
                            x = simx[-1] + abs(simx[-1] - simx[0])*0.05, 
                            y = LRO_y[-1], 
                               xanchor = "left",
                                showarrow = False, 
                                font = dict(color = LRO_color)
                            )
        fitplot.add_annotation(text = f"slope = {int(result["RLO result"]["slope"])} +- {int(result["RLO result"]["slope error"])}<br>R<sup>2</sup>={result["RLO result"]["R^2"]:.3f}", 
                               x = simx[-1] + abs(simx[-1] - simx[0])*0.05, 
                               y = RLO_y[-1], 
                               xanchor = "left",
                               showarrow = False, 
                               font = dict(color = RLO_color)
                              )
        fitplot.add_annotation(text = f"slope = {int(result["all result"]["slope"])} +- {int(result["all result"]["slope error"])}<br>R<sup>2</sup>={result["all result"]["R^2"]:.3f}", 
                               x = simx[-1] + abs(simx[-1] - simx[0])*0.05, 
                               y = all_y[-1], 
                               xanchor = "left",
                               showarrow = False, 
                               font = dict(color = "black")
                              )

        fitplot.update_xaxes(title = f"{result["axes"]["x name"]}")
        fitplot.update_yaxes(title = f"{result["axes"]["y name"]}")
        fitplot.update_layout(width = 3.3*300, height = 2*300, template = "simple_white")
        fitplot.show("png")
    return LRO_y, RLO_y, all_y, fitplot, result, simx


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
