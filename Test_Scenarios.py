# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:49:21 2017

@author: gracejenkins

The purpose of this file is to run different scenarios of the simulations
"""

from Scheduling_Simulation import *

def compare_holding(static_parameters, dynamic_parameters):
    # inputs
    inputs = {}
    inputs['Daily Appointments Available'] = 10
    inputs['Days to run'] = 300
    inputs['Warm up period'] = 30
    inputs['Urgent rate'] = 4
    inputs['Non-urgent rate'] = 6
    inputs['Non-urgent threshold method'] = 'Dynamic'
    inputs['Non-urgent threshold inputs'] = {}
    inputs['Non-urgent threshold inputs']['Dynamic'] = 14
    
    total_demand = create_total_demand(inputs)
    
    inputs['Hold for urgent method'] = 'Static'
    inputs['Hold for urgent inputs'] = {}
    
    for parameter in static_parameters:
        # number of appointments to hold in the case of static holding 
        inputs['Hold for urgent inputs']['Static'] = parameter
        run_simulation("Milk Carton", inputs, total_demand)
        plot_results("Milk Carton: Static ("+str(parameter)+")", inputs, total_demand)
        print("Milk Carton: Static ("+str(parameter)+")")
        results = summarize_results(inputs, total_demand)
    
    
    inputs['Hold for urgent method'] = 'Dynamic'
    for parameters in dynamic_parameters:
        
        inputs['Hold for urgent inputs']['Dynamic'] = parameters 
    
    
        run_simulation("Milk Carton", inputs, total_demand)
        plot_results("Milk Carton: Dynamic ("+str(parameters)+")", inputs, total_demand)
        print("Milk Carton: Dynamic ("+str(parameters)+")")
        results = summarize_results(inputs, total_demand)

def compare_simulations(arrival_rates):
    
    inputs = {}
    inputs['Daily Appointments Available'] = 10
    inputs['Days to run'] = 100
    inputs['Warm up period'] = 30
    inputs['Non-urgent threshold method'] = 'Dynamic'
    inputs['Non-urgent threshold inputs'] = {}
    inputs['Non-urgent threshold inputs']['Dynamic'] = 7
    inputs['Hold for urgent method'] = 'Dynamic'
    inputs['Hold for urgent inputs'] = {}
    inputs['Hold for urgent inputs']['Static'] = 4
    inputs['Hold for urgent inputs']['Dynamic'] = [.1,.1] # [p,c,m,q,d]
    
    
    for arrival_rate in arrival_rates:
        
        inputs['Urgent rate'] = arrival_rate[0]
        inputs['Non-urgent rate'] = arrival_rate[1]
        
            
        total_demand = create_total_demand(inputs)
        
        # Run classic, first come first serve simulation
        run_simulation("Classic", inputs, total_demand)
        plot_results("Classic (" + str(arrival_rate) + ")", inputs, total_demand)
        print("Classic (" + str(arrival_rate) + ")")
        classic_results = summarize_results(inputs, total_demand)
    
        # Run rolling horizon threshold simulation 
        run_simulation("Rolling Horizon", inputs, total_demand)
        plot_results("Rolling Horizon (" + str(arrival_rate) + ")", inputs, total_demand)
        print("Rolling Horizon (" + str(arrival_rate) + ")")
        rolling_results = summarize_results(inputs, total_demand)
    
        # Run milk carton threshold simulation
        run_simulation("Milk Carton", inputs, total_demand)
        plot_results("Milk Carton (" + str(arrival_rate) + ")", inputs, total_demand)
        print("Milk Carton (" + str(arrival_rate) + ")")
        milk_results = summarize_results(inputs, total_demand)
        
def compare_thresholding(thresholds):
    
    inputs = {}
    inputs['Daily Appointments Available'] = 10
    inputs['Days to run'] = 300
    inputs['Warm up period'] = 30
    inputs['Urgent rate'] = 7
    inputs['Non-urgent rate'] = 3
    inputs['Hold for urgent method'] = 'Dynamic'
    inputs['Hold for urgent inputs'] = {}
    inputs['Hold for urgent inputs']['Dynamic'] = [.1,.1] 
    
    total_demand = create_total_demand(inputs)
    
    inputs['Non-urgent threshold inputs'] = {}

    for threshold in thresholds: 
        
        inputs['Non-urgent threshold inputs']['Static'] = threshold
        inputs['Non-urgent threshold inputs']['Dynamic'] = threshold
        
        inputs['Non-urgent threshold method'] = 'Static'
        run_simulation("Milk Carton",inputs, total_demand)
        plot_results("Milk Carton (Static " + str(threshold) + ")", inputs, total_demand)
        print("Milk Carton (Static " + str(threshold) + ")")
        milk_results = summarize_results(inputs, total_demand)
        
        inputs['Non-urgent threshold method'] = 'Dynamic'
        run_simulation("Milk Carton",inputs, total_demand)
        plot_results("Milk Carton (Dynamic " + str(threshold) + ")", inputs, total_demand)
        print("Milk Carton (Dynamic " + str(threshold) + ")")
        milk_results = summarize_results(inputs, total_demand)


### COMPARE SIMULATIONS ###
#arrival_rates = [[5,5],[3,7],[7,3],[5,6],[3,8],[8,3],[4,5],[3,6],[6,3]]
#compare_simulations(arrival_rates)


### COMPARE HOLDING METHODS ###
#static_parameters = [0,1,2,3,4,5]
#dynamic_parameters = [[.05,.1],[.05,.15],[.05,.2],[.01,.1],[.05,.05],[.1,.1]]
#compare_holding(static_parameters, dynamic_parameters)

### COMPARE THRESHOLDING METHODS ###
thresholds = [7,10,14,20,30]
compare_thresholding(thresholds)

    