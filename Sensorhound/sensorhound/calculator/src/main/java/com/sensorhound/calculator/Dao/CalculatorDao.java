package com.sensorhound.calculator.Dao;

import java.io.*;
import java.util.*;

import org.springframework.stereotype.Repository;

import com.sensorhound.calculator.Model.CalculatorModel;

@Repository
public class CalculatorDao {

private static List<CalculatorModel> calc;
	
	static{
		
		calc = new ArrayList<> ( Arrays.asList(
			
				new CalculatorModel(1,2,"add", 3)
				,new CalculatorModel(2,2,"sub", 0),
				new CalculatorModel(4,2,"div", 2)
			)); 
		
	}
	
	public Collection<CalculatorModel> getAllResults(){
		return this.calc;
	}
	
	public void insertAdd(CalculatorModel c){
		this.calc.add(c);
	}
}

