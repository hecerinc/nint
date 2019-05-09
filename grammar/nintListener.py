# Generated from nint.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .nintParser import nintParser
else:
    from nintParser import nintParser

import sys
sys.path.append("C:/dev/compiler")
from nintCompiler import nintCompiler
from symbols.Types import DType


# This class defines a complete listener for a parse tree produced by nintParser.
class nintListener(ParseTreeListener):

    # Enter a parse tree produced by nintParser#prog.
    def enterProg(self, ctx:nintParser.ProgContext):
        pass

    # Exit a parse tree produced by nintParser#prog.
    def exitProg(self, ctx:nintParser.ProgContext):
        pass


    # Enter a parse tree produced by nintParser#primary.
    def enterPrimary(self, ctx:nintParser.PrimaryContext):
        pass

    # Exit a parse tree produced by nintParser#primary.
    def exitPrimary(self, ctx:nintParser.PrimaryContext):
        pass


    # Enter a parse tree produced by nintParser#block.
    def enterBlock(self, ctx:nintParser.BlockContext):
        pass

    # Exit a parse tree produced by nintParser#block.
    def exitBlock(self, ctx:nintParser.BlockContext):
        pass


    # Enter a parse tree produced by nintParser#statement.
    def enterStatement(self, ctx:nintParser.StatementContext):
        pass

    # Exit a parse tree produced by nintParser#statement.
    def exitStatement(self, ctx:nintParser.StatementContext):
        pass


    # Enter a parse tree produced by nintParser#expression.
    def enterExpression(self, ctx:nintParser.ExpressionContext):
        pass

    # Exit a parse tree produced by nintParser#expression.
    def exitExpression(self, ctx:nintParser.ExpressionContext):
        pass


    # Enter a parse tree produced by nintParser#assignment.
    def enterAssignment(self, ctx:nintParser.AssignmentContext):
        pass

    # Exit a parse tree produced by nintParser#assignment.
    def exitAssignment(self, ctx:nintParser.AssignmentContext):
        pass


    # Enter a parse tree produced by nintParser#lhs.
    def enterLhs(self, ctx:nintParser.LhsContext):
        pass

    # Exit a parse tree produced by nintParser#lhs.
    def exitLhs(self, ctx:nintParser.LhsContext):
        pass


    # Enter a parse tree produced by nintParser#arrayAccess.
    def enterArrayAccess(self, ctx:nintParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by nintParser#arrayAccess.
    def exitArrayAccess(self, ctx:nintParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by nintParser#exp.
    def enterExp(self, ctx:nintParser.ExpContext):
        pass

    # Exit a parse tree produced by nintParser#exp.
    def exitExp(self, ctx:nintParser.ExpContext):
        pass


    # Enter a parse tree produced by nintParser#term.
    def enterTerm(self, ctx:nintParser.TermContext):
        pass

    # Exit a parse tree produced by nintParser#term.
    def exitTerm(self, ctx:nintParser.TermContext):
        pass


    # Enter a parse tree produced by nintParser#factor.
    def enterFactor(self, ctx:nintParser.FactorContext):
        pass

    # Exit a parse tree produced by nintParser#factor.
    def exitFactor(self, ctx:nintParser.FactorContext):
        pass


    # Enter a parse tree produced by nintParser#expressionList.
    def enterExpressionList(self, ctx:nintParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by nintParser#expressionList.
    def exitExpressionList(self, ctx:nintParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by nintParser#literal.
    def enterLiteral(self, ctx:nintParser.LiteralContext):
        pass

    # Exit a parse tree produced by nintParser#literal.
    def exitLiteral(self, ctx:nintParser.LiteralContext):
        pass


    # Enter a parse tree produced by nintParser#forInit.
    def enterForInit(self, ctx:nintParser.ForInitContext):
        pass

    # Exit a parse tree produced by nintParser#forInit.
    def exitForInit(self, ctx:nintParser.ForInitContext):
        pass


    # Enter a parse tree produced by nintParser#declaration.
    def enterDeclaration(self, ctx:nintParser.DeclarationContext):
        pass

    # Exit a parse tree produced by nintParser#declaration.
    def exitDeclaration(self, ctx:nintParser.DeclarationContext):
        pass


    # Enter a parse tree produced by nintParser#initializer.
    def enterInitializer(self, ctx:nintParser.InitializerContext):
        pass

    # Exit a parse tree produced by nintParser#initializer.
    def exitInitializer(self, ctx:nintParser.InitializerContext):
        pass


    # Enter a parse tree produced by nintParser#vectorInitializer.
    def enterVectorInitializer(self, ctx:nintParser.VectorInitializerContext):
        pass

    # Exit a parse tree produced by nintParser#vectorInitializer.
    def exitVectorInitializer(self, ctx:nintParser.VectorInitializerContext):
        pass


    # Enter a parse tree produced by nintParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:nintParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by nintParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:nintParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by nintParser#parameterList.
    def enterParameterList(self, ctx:nintParser.ParameterListContext):
        pass

    # Exit a parse tree produced by nintParser#parameterList.
    def exitParameterList(self, ctx:nintParser.ParameterListContext):
        pass


    # Enter a parse tree produced by nintParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:nintParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by nintParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:nintParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by nintParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:nintParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by nintParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:nintParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by nintParser#functionCall.
    def enterFunctionCall(self, ctx:nintParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by nintParser#functionCall.
    def exitFunctionCall(self, ctx:nintParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by nintParser#callArgs.
    def enterCallArgs(self, ctx:nintParser.CallArgsContext):
        pass

    # Exit a parse tree produced by nintParser#callArgs.
    def exitCallArgs(self, ctx:nintParser.CallArgsContext):
        pass


    # Enter a parse tree produced by nintParser#pipeStmt.
    def enterPipeStmt(self, ctx:nintParser.PipeStmtContext):
        pass

    # Exit a parse tree produced by nintParser#pipeStmt.
    def exitPipeStmt(self, ctx:nintParser.PipeStmtContext):
        pass


