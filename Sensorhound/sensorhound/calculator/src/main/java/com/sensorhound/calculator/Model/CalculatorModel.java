package com.sensorhound.calculator.Model;

import java.io.*;
import java.util.*;

public class CalculatorModel {
	private int operand1;
	private int operand2;
	private String operation;
	private int result;
	
	public CalculatorModel() {

	}
	
	public CalculatorModel(int operand1, int operand2, String operation, int result) {
		super();
		this.operand1 = operand1;
		this.operand2 = operand2;
		this.operation = operation;
		this.result = result;
	}

	public String getOperation() {
		return operation;
	}

	public void setOperation(String operation) {
		this.operation = operation;
	}

	public int getOperand1() {
		return operand1;
	}
	
	public void setOperand1(int operand1) {
		this.operand1 = operand1;
	}
	
	public int getOperand2() {
		return operand2;
	}
	
	public void setOperand2(int operand2) {
		this.operand2 = operand2;
	}
	
	public int getResult() {
		return result;
	}
	
	public void setResult(int result) {
		this.result = result;
	}
	
	

}

