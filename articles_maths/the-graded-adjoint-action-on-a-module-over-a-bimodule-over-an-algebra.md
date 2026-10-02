
# __The Graded Adjoint Action on a Module over a Bimodule over an Algebra__

## Introduction

The graded action of a graded algebra on a graded module is even, and the Koszul sign rule governs every exchange of two homogeneous things. This article is about the **adjoint action**, the transpose of the graded action with respect to an $\alpha$-invariant pairing: the operator $L_a$ has adjoint $L_{\sigma(a)}$, so the algebra acts on the module a second time by $a\triangleright x=\sigma(a)x$; the article computes this action, shows that it is compatible with the grading, and derives the sign rule for the adjoint of a graded commutator.

The article is the seventh and last of the `* Operator Theory` group of this category. It assumes the graded action and the Koszul sign rule of *The Graded Action on a Module over a Bimodule over an Algebra*, the one-sided adjoints of *The Signed Adjoint of the Left Multiplication on a Module over an Algebra* and *The Signed Adjoint of the Sandwich on a Bimodule over an Algebra*, and the involution and unitarity of *Module Operators with an Involution*. The grading itself, superalgebras and their morphisms belong to *Superalgebras and Graded Structures*. The article stays inside Part I: no distance, norm, form with a norm, positivity, topology or limit. Throughout, $R$ is a commutative ring with $1 \neq 0$ in which $2$ is invertible, $(A,\sigma)$ is a graded involutive $R$-algebra with graded involution ($\sigma(A_i)\subseteq A_i$) and grade involution $\alpha$ commuting with $\sigma$, $\beta=\alpha\sigma$, ${}_A M_A$ is a graded bimodule with the Koszul right action and an $\alpha$-invariant balanced $\sigma$-sesquilinear pairing, and $L_a$, $L^{\alpha}_a$ are the one-sided operators.

## The Adjoint Action

### The transpose of the left action

**Definition.** The **adjoint action** of $A$ on $M$ is

$$
a \triangleright x = \sigma(a)\,x \qquad (a \in A,\ x \in M),
$$

the one-sided operator adjoint read as an action: since $(L_a)^{*}=L_{\sigma(a)}$, the adjoint of the left multiplication by $a$ is the left multiplication by $\sigma(a)$.

**Proposition.** The adjoint action is a right action of $A$ on $M$,

$$
(a b)\triangleright x = b\triangleright(a\triangleright x),
$$

and it satisfies $a\triangleright x = L_a^{*}(x)$; the original left action is recovered from the adjoint action by $a x=\sigma(a)\triangleright x$.

*Proof.* $(ab)\triangleright x=\sigma(ab)x=\sigma(b)\sigma(a)x=b\triangleright(\sigma(a)x)=b\triangleright(a\triangleright x)$, so it is a right action; the last two clauses are the definitions and $\sigma^{2}=\mathrm{id}$. $\square$

The pairing converts the left action of $A$ into the right adjoint action of $A$; the two actions together are the module-level form of the statement that the adjoint reverses the order, the content of $(L_{ab})^{*}=(L_b)^{*}(L_a)^{*}$.

### Evenness of the adjoint action

**Proposition.** If the involution $\sigma$ is graded, $\sigma(A_i)\subseteq A_i$, then the adjoint action is even:

$$
a \in A_i \implies a\triangleright M_j \subseteq M_{i+j}, \qquad \deg(a\triangleright x)=\deg a+\deg x \quad (a,x \text{ homogeneous}).
$$

*Proof.* $a\triangleright M_j=\sigma(a)M_j$, and $\deg\sigma(a)=\deg a$ because $\sigma$ is graded, so $a\triangleright M_j\subseteq M_{i+j}$. $\square$

**Corollary.** The operator $L_a^{*}=L_{\sigma(a)}$ has the same parity as $L_a$, and the adjoint operation preserves the $\mathbb{Z}/2$-degree of every homogeneous one-sided operator:

$$
\deg L_a^{*}=\deg L_a=\deg a .
$$

*Proof.* $L_a$ has parity $\deg a$ by the evenness of the action, and $\deg\sigma(a)=\deg a$, so $L_{\sigma(a)}$ has the same parity. $\square$

The adjoint is therefore not only additive and anti-multiplicative but **graded**: it maps operators of parity $i$ to operators of parity $i$, so no sign appears in the parity alone.

## The Sign Rule

### The Koszul sign of the operators

**Proposition.** For homogeneous $a$ and for every homogeneous operator $T$ of parity $\deg T$ the grade involution acts on the operators by the Koszul sign:

$$
\alpha\,L_a\,\alpha^{-1}=(-1)^{\deg a}L_a, \qquad \alpha\,T\,\alpha^{-1}=(-1)^{\deg T}T .
$$

*Proof.* This is the sign rule of *The Graded Action on a Module over a Bimodule over an Algebra*. $\square$

**Corollary.** The sign rule is compatible with the adjoint: for homogeneous $T$,

$$
\alpha\,T^{*}\,\alpha^{-1}=(-1)^{\deg T}T^{*}.
$$

*Proof.* $T^{*}$ has the same parity as $T$ by the gradedness of the adjoint, so applying the sign rule to $T^{*}$ gives the identity. $\square$

Conjugation by the grade involution, the adjoint, and the grading are therefore mutually compatible: both operations multiply a homogeneous operator by the same sign $(-1)^{\deg T}$.

### The graded commutator

**Definition.** For homogeneous operators $S$ and $T$ the **graded commutator** is

$$
[S,T]_{\epsilon}=ST-\epsilon\,TS, \qquad \epsilon=(-1)^{\deg S\,\deg T}.
$$

When $\epsilon=1$ it is the ordinary commutator; when $\epsilon=-1$, the case of two odd operators, it is the ordinary **anticommutator**.

**Proposition.** The graded commutator of the left multiplications is a left multiplication,

$$
[L_a,L_b]_{\epsilon}=L_{ab-\epsilon\,ba}, \qquad \epsilon=(-1)^{\deg a\,\deg b},
$$

and it vanishes exactly when $L_{ab-\epsilon ba}=0$, that is, when $ab-\epsilon ba$ annihilates $M$.

*Proof.* $L_aL_b-L_bL_a\cdot\epsilon=\ldots$: since $L_aL_b=L_{ab}$, the expression is $L_{ab}-\epsilon L_{ba}=L_{ab-\epsilon ba}$; the last clause is the kernel statement for $L$. $\square$

The graded commutator is the graded version of the commutator, and the sign $\epsilon$ is the Koszul sign attached to the exchange of $a$ and $b$.

## The Adjoint of the Graded Commutator

### The sign rule for the bracket

**Theorem.** For homogeneous $a$ and a homogeneous operator $T$, with $\epsilon=(-1)^{\deg a\,\deg T}$,

$$
[L_a,T]_{\epsilon}^{*}=-\epsilon\,\bigl[L_{\sigma(a)},T^{*}\bigr]_{\epsilon}.
$$

Thus the adjoint of the graded commutator is the graded commutator of the adjoints, up to the sign $-\epsilon$: the ordinary sign $-1$ for the commutator ($\epsilon=1$) and the sign $+1$ for the anticommutator ($\epsilon=-1$).

*Proof.* By the laws of the adjoint, $(L_aT)^{*}=T^{*}L_{\sigma(a)}$ and $(TL_a)^{*}=L_{\sigma(a)}T^{*}$, and $T^{*}$ has parity $\deg T$; hence

$$
[L_a,T]_{\epsilon}^{*}=T^{*}L_{\sigma(a)}-\epsilon\,L_{\sigma(a)}T^{*}=-\epsilon\bigl(L_{\sigma(a)}T^{*}-\epsilon\,T^{*}L_{\sigma(a)}\bigr)=-\epsilon\,[L_{\sigma(a)},T^{*}]_{\epsilon}. \qquad\square
$$

**Corollary.** For two homogeneous left multiplications,

$$
[L_a,L_b]_{\epsilon}^{*}=L_{\sigma(ab-\epsilon ba)}=-\epsilon\,[L_{\sigma(a)},L_{\sigma(b)}]_{\epsilon}.
$$

*Proof.* Apply the theorem with $T=L_b$, $T^{*}=L_{\sigma(b)}$, and use $[L_a,L_b]_\epsilon=L_{ab-\epsilon ba}$ and $\sigma(ab-\epsilon ba)=\sigma(b)\sigma(a)-\epsilon\,\sigma(a)\sigma(b)$. $\square$

The theorem is the sign rule the grading imposes on the adjoint action: for two odd operators the anticommutator has a self-adjoint bracket, $[L_a,T]_{-1}^{*}=[L_{\sigma(a)},T^{*}]_{-1}$, while for the ordinary commutator a sign is required. It is the graded refinement of the elementary fact that the adjoint of a composite reverses the order.

### The sign rule for the sandwich

**Proposition.** The adjoint action on the signed sandwiches is compatible with the grading:

$$
\bigl(S^{\alpha}_{a,b}\bigr)^{*}=S^{\alpha}_{\beta(a),\beta(b)}, \qquad \bigl(S_{a,b}\bigr)^{*}=S_{\sigma(a),\sigma(b)},
$$

and it sends operators of parity $i$ to operators of parity $i$: the adjoint action preserves the degree and the sign rule of the graded operators.

*Proof.* This is *The Signed Adjoint of the Sandwich on a Bimodule over an Algebra*; the parity statement follows because $\sigma$ and $\alpha$ are graded and their composite $\beta$ is graded, so both parameters keep their degrees. $\square$

## The Adjoint Action on the Operators

### The action of the adjoint action

**Proposition.** The adjoint action of $A$ on $M$ induces an action on the operators by

$$
a \cdot T = L_{\sigma(a)}\,T, \qquad a \cdot T = T\,L_{\sigma(a)} ,
$$

the left and right regular actions of $A$ composed with the adjoint action, and the adjoint of $a\cdot T$ is computed by the rules above; in particular

$$
(L_a T)^{*}=T^{*}L_{\sigma(a)}, \qquad (T L_a)^{*}=L_{\sigma(a)}T^{*} .
$$

*Proof.* The two formulas are the anti-multiplicativity of the adjoint with $(L_a)^{*}=L_{\sigma(a)}$. $\square$

**Corollary.** The adjoint action intertwines the involution of the algebra with the involution of the operators: the algebra element $a$ acts through $L_{\sigma(a)}$, so the adjoint action is the original action precomposed with $\sigma$, and applying the operator involution to an action applies $\sigma$ to the algebra element.

*Proof.* $L_a^{*}=L_{\sigma(a)}$ is the identity defining the adjoint action; the rest is its restatement. $\square$

### Self-adjointness under the adjoint action

**Proposition.** Let $T$ be homogeneous and let $a$ be homogeneous with $\sigma(a)=a$. Then $T$ is self-adjoint if and only if the graded commutator $[L_a,T]_{\epsilon}$ is skew with respect to the adjoint in the graded sense,

$$
T^{*}=T \implies [L_a,T]_{\epsilon}^{*}=-\epsilon\,[L_a,T]_{\epsilon},
$$

and conversely $T^{*}=T$ follows when this holds for a separating family of such $a$.

*Proof.* By the theorem $[L_a,T]_{\epsilon}^{*}=-\epsilon[L_a,T^{*}]_{\epsilon}$, and with $\sigma(a)=a$ this is $-\epsilon[L_a,T^{*}]_{\epsilon}$. If $T^{*}=T$ it equals $-\epsilon[L_a,T]_{\epsilon}$, which is the displayed skewness. Conversely, if the skewness holds then $[L_a,T^{*}]_{\epsilon}=[L_a,T]_{\epsilon}$ for the family, that is $L_{a(T^{*}-T)-\epsilon(T^{*}-T)a}=0$, and for a separating family this forces $T^{*}=T$. $\square$

## Examples

**(a) The trivial grading.** For $\alpha=\mathrm{id}$ the sign rule is vacuous, the graded commutator is the ordinary one, and the theorem reads $[L_a,T]^{*}=-[L_{\sigma(a)},T^{*}]$, the classical rule for the commutator with a left multiplication.

**(b) The trivial involution.** For $\sigma=\mathrm{id}$ the adjoint action is the original action, $a\triangleright x=ax$, and every operator is graded: the sign rule reduces to the graded action of *The Graded Action on a Module over a Bimodule over an Algebra*.

**(c) The Clifford algebra.** For a Clifford algebra with its canonical involution $\sigma$ and grade involution $\alpha$, the graded commutator $[L_a,L_b]_\epsilon=L_{ab-\epsilon ba}$ is the algebra bracket, and the theorem computes its adjoint with the Koszul sign; the anticommutator of two odd vectors is even and self-adjoint under the adjoint action.

**(d) The exterior algebra.** For $A=\Lambda(V)$ with the graded-commutative product, the graded commutator of two odd elements is the anticommutator, and its adjoint is the anticommutator of the adjoints with the sign $+1$, in agreement with the theorem.

**(e) The matrix algebra with a diagonal grading.** For $A=M_n(k)$ with the transpose involution and a diagonal grading by parity of the index, $\sigma$ is graded, and the adjoint action is $a\triangleright X=a^{\mathsf{T}}X$; the graded commutator's adjoint acquires the sign $-\epsilon$.

## Summary

For a graded module over a graded involutive algebra with an $\alpha$-invariant balanced pairing, the transpose of the left action $L_a$ is the left multiplication by $\sigma(a)$, so the algebra acts on the module a second time by the adjoint action $a\triangleright x=\sigma(a)x$, which is a right action and is even when the involution is graded. The adjoint operation preserves the parity of every homogeneous operator, and it is compatible with the Koszul sign rule: both the grade involution and the adjoint multiply a homogeneous operator by $(-1)^{\deg T}$. The graded commutator $[S,T]_\epsilon=ST-\epsilon TS$ has adjoint $[L_a,T]_\epsilon^{*}=-\epsilon[L_{\sigma(a)},T^*]_\epsilon$, so the adjoint of the ordinary commutator is minus the commutator of the adjoints and the adjoint of the anticommutator is the anticommutator of the adjoints; for two left multiplications the bracket is again a left multiplication and the formula reads $[L_a,L_b]_\epsilon^{*}=L_{\sigma(ab-\epsilon ba)}$. The adjoint action on the signed sandwiches is $(S^{\alpha}_{a,b})^{*}=S^{\alpha}_{\beta(a),\beta(b)}$ with $\beta=\alpha\sigma$, and it preserves the degree and the sign rule. Nothing in the article uses a norm or a topology; the sign rule is the Koszul sign of the grading, and the adjoint action is the transpose of the graded action with respect to the pairing.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $(A,\sigma)$ | base ring, graded involutive $R$-algebra, graded involution |
| $\alpha$, $\beta=\alpha\sigma$ | grade involution, commuting with $\sigma$, and the composite |
| $M$ | graded bimodule with α-invariant balanced σ-sesquilinear pairing |
| $a\triangleright x=\sigma(a)x$ | the adjoint action, a right action |
| $L_a^{*}=L_{\sigma(a)}$ | the adjoint of the left multiplication |
| $(-1)^{\deg T}$ | the Koszul sign of the operator $T$ |
| $\alpha T\alpha^{-1}=(-1)^{\deg T}T$ | the sign rule |
| $[S,T]_\epsilon=ST-\epsilon TS$ | the graded commutator, $\epsilon=(-1)^{\deg S\deg T}$ |
| $[L_a,T]_\epsilon^{*}=-\epsilon[L_{\sigma(a)},T^{*}]_\epsilon$ | the sign rule for the adjoint of the bracket |
| $(S^{\alpha}_{a,b})^{*}=S^{\alpha}_{\beta(a),\beta(b)}$ | the adjoint action on the signed sandwich |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for graded algebras, involutions and sesquilinear forms.
- Pierre Deligne and John W. Morgan, *Notes on Supersymmetry*, in *Quantum Fields and Strings: A Course for Mathematicians* (American Mathematical Society, 1999), for the Koszul sign rule and graded operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for graded involutions and their adjoints.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the grade involution, the graded commutator and the adjoint action.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for one-sided operators, their adjoints and the graded bookkeeping over rings.
