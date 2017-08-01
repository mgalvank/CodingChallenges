package com.sensorhound.calculator.Service;

import java.io.*;
import java.util.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.sensorhound.calculator.Dao.CalculatorDao;
import com.sensorhound.calculator.Model.CalculatorModel;

@Service
public class CalculatorService {

	
	@Autowired
	private CalculatorDao calcDao;
	
	public Collection<CalculatorModel> getAllResults(){
		return this.calcDao.getAllResults();
	}
	
	public void insertResult(CalculatorModel c){
		calcDao.insertAdd(c);
	}
	
	
}

