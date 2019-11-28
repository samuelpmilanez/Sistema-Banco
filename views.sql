USE `null_bank`;

CREATE VIEW `view_telefone` AS select * from telefone;

CREATE VIEW `view_transação` AS
    SELECT 
        *
    FROM
        transacao;

create view `view_cliente_conta` AS
select * 
FROM
	cliente AS cl,
	conta AS co,
	cliente_tem_conta AS ctc
WHERE
	cl.cpf = ctc.cliente_cpf
	AND co.id_conta = ctc.conta_id_conta
	AND co.agencia_id_agencia = ctc.conta_agencia_id_agencia
    ;

USE `null_bank`;

CREATE VIEW `contas_do_gerente` AS 
	select * 
	from funcionario as f, view_cliente_conta as c
    where f.matricula = c.gerente_matricula
    ;
select * from view_cliente_conta;