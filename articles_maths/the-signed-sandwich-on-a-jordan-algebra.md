# __The Signed Sandwich on a Jordan Algebra__

## Introduction

A two-sided operator dresses an element between a left and a right factor. For an associative algebra the sandwich is $x\mapsto axb$, and with a grade involution $\alpha$ of order two available it can be twisted in the middle to $x\mapsto a\,\alpha(x)\,b$; this is the **signed sandwich**, and its theory for a ring — the composition law $S_{a,b}S_{c,d} = S_{ac,db}$, the twisted law $S^{\alpha}_{a,b}S^{\alpha}_{c,d} = S^{\alpha}_{a\alpha(c),b\alpha(d)}$, and the criterion for the diagonal $r_u = S^{\alpha}_{u,u^{-1}}$ to be an involution — belongs to *The Signed Sandwich on a Ring*. The product of a Jordan algebra is not associative, so the expression $axb$ has no intrinsic meaning; it exists only when the Jordan algebra is **special**, $J = A^+$ for an associative algebra $A$, in which case $axb$ is an operator on the underlying module of $J$ and the intrinsic Jordan two-sided operator is its symmetrisation, the **quadratic representation** $U_{a,b}$ of *The Left and Right Multiplication Operators on a Jordan Algebra*.

This article carries the two-sided operators to the Jordan setting. It defines the unsigned sandwich as an operator on a special Jordan algebra, proves that its symmetrisation is the quadratic representation, and shows that the symmetrised operators are exactly the two-sided operators that live in the multiplication algebra. It then defines the signed sandwich $S^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b$ and its symmetrisation $\Sigma^{\alpha}_{a,b} = U_{a,b}\circ\alpha$, and it isolates the **failure** of the ring composition law: the composition of two symmetrised signed sandwiches is a product $U_{a,b}U_{c,d}$ of quadratic representations, which is not in general a quadratic representation, so the monoid law of the ring case does not survive the symmetrisation. The diagonal signed sandwich $r_u = S^{\alpha}_{u,u^{-1}}$ is the signed conjugation $x \mapsto u\alpha(x)u^{-1}$, and its square is the conjugation by $u\alpha(u)$; it is an involution, a **reflection**, exactly when $u\alpha(u)$ is central. The reflection correspondence is developed in *Reflections as Signed Two-Sided Operators on a Jordan Algebra*, next in this group.

The article assumes *The Signed Sandwich on a Ring* for the definitions of the grade involution, the unsigned and the signed sandwich on a ring and their composition laws (used, not reproved), *The Left and Right Multiplication Operators on a Jordan Algebra* for the quadratic representation and the fundamental formula, *Jordan Algebras* for the special Jordan algebra $A^+$, and *The Polarisation Operator* for the polarised form $U_{a,b} = \tfrac12(U_{a+b}-U_a-U_b)$. Throughout, $J = A^+$ is a special unital Jordan algebra over a commutative ring $R$, $\alpha$ is a grade involution of the associative algebra $A$ (an automorphism of order two, hence an automorphism of $J$), and $S_{a,b}$, $S^{\alpha}_{a,b}$ denote the operators on the underlying module $J$ defined below. No norm, form or distance occurs; the "reflection" is an operator of order two, without any geometric reading, and the symmetric-space theory of reflections is met in Part IV.

## The Unsigned Sandwich on a Special Jordan Algebra

### Definition

**Definition.** For $a, b \in J = A^+$ the **unsigned sandwich** is the operator

$$
S_{a,b} : J \longrightarrow J, \qquad S_{a,b}(x) = a\,x\,b ,
$$

the product being taken in the associative algebra $A$ whose underlying module is $J$. It is additive, it is $R$-linear in each of $a$, $b$ and $x$, and $S_{a,b} = L^A_aR^A_b$ is the product of a left and a right multiplication of $A$.

The sandwich is an operator on the module $J$; it is not in general an operator of the Jordan structure. It need not commute with the Jordan product, and it need not lie in the multiplication algebra $\operatorname{Mult}(J)$ of *The Jordan Multiplication Operators*.

### The Symmetrisation is the Quadratic Representation

**Theorem.** For all $a, b \in J$,

$$
\tfrac12\bigl(S_{a,b} + S_{b,a}\bigr) = U_{a,b} ,
$$

the quadratic representation of *The Left and Right Multiplication Operators on a Jordan Algebra*; in particular the symmetrisation of the sandwiches is an operator of the Jordan structure, and it lies in $\operatorname{Mult}(J)$.

*Proof.* For $x \in J$ one has $\tfrac12(S_{a,b}+S_{b,a})(x) = \tfrac12(axb+bxa)$, and the special form of the quadratic representation is $U_{a,b}(x) = \tfrac12(axb+bxa)$. That $U_{a,b}$ lies in $\operatorname{Mult}(J)$ is its definition, $U_{a,b} = L_aL_b+L_bL_a-L_{a\bullet b}$. $\square$

**Corollary.** The antisymmetrisation $\tfrac12(S_{a,b}-S_{b,a})$ is nonzero exactly when the sandwich does not commute with the transposition of its parameters; it equals $\tfrac12(axb-bxa)$ and is the operator that the Jordan structure discards. The Jordan two-sided operator is the part of $S_{a,b}$ that is symmetric in $a$ and $b$, and the discarded part measures the failure of the Jordan product to see the order of the factors.

**Remark.** The unsigned sandwich and the quadratic representation agree in the associative case: if $A$ is commutative, $S_{a,b} = U_{a,b} = L_{ab}$. They differ already for $A = M_2(k)$, where $S_{a,b}(x)$ need not be symmetric in the parameters while $U_{a,b}(x) = \tfrac12(axb+bxa)$ always is.

## The Graded Structure and the Twist

### The Grade Involution

**Definition.** A **grade involution** of the associative algebra $A$ is an automorphism $\alpha \in \operatorname{Aut}(A)$ with $\alpha^2 = \mathrm{id}$; it is the **trivial** one when $\alpha = \mathrm{id}$. The decomposition

$$
A = A_{\bar 0} \oplus A_{\bar 1}, \qquad A_{\bar 0} = \{x : \alpha(x) = x\}, \qquad A_{\bar 1} = \{x : \alpha(x) = -x\},
$$

makes $A$ a $\mathbb{Z}/2$-graded algebra, with $A_iA_j \subseteq A_{i+j}$; this is the graded structure of *The Signed Sandwich on a Ring*, and $\alpha$ is an automorphism of the special Jordan algebra $J = A^+$, since $\alpha(x\bullet y) = \alpha(x)\bullet\alpha(y)$ for the halved product.

**Proposition.** $\alpha$ is a grade involution of the Jordan algebra $J$, that is, an automorphism of $J$ with $\alpha^2 = \mathrm{id}$, and the Jordan product respects the induced grading, $J_i\bullet J_j \subseteq J_{i+j}$ with $J_i = A_i$; the commutativity of $\bullet$ is not disturbed, and the only new datum is the sign rule that an odd element carries.

*Proof.* $\alpha$ preserves the associative product, hence the halved product, hence is an automorphism of $J$; $\alpha^2 = \mathrm{id}$ is assumed; the grading statement is the multiplicativity of $\alpha$ read on the decomposition. $\square$

### The Signed Sandwich

**Definition.** For $a, b \in J$ the **signed sandwich** is the operator

$$
S^{\alpha}_{a,b} : J \longrightarrow J, \qquad S^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b .
$$

It is additive, $R$-linear in $a$ and $b$, and it is the unsigned sandwich precomposed with the grade involution,

$$
S^{\alpha}_{a,b} = S_{a,b}\circ\alpha .
$$

**Theorem (the signed sandwich is the unsigned sandwich at $\alpha$).** For all $a, b \in J$,

$$
S^{\alpha}_{a,b} = S_{a,b}\circ\alpha, \qquad S^{\alpha}_{a,b}(x) = S_{a,b}(\alpha(x)) \ \text{ for all } x ,
$$

and the two coincide exactly when $\alpha = \mathrm{id}$.

*Proof.* $S_{a,b}(\alpha(x)) = a\alpha(x)b = S^{\alpha}_{a,b}(x)$, by the definitions. If $\alpha = \mathrm{id}$ the two formulas are identical; conversely if $S^{\alpha}_{a,b} = S_{a,b}$ for all $a,b$ then $\alpha(x) = x$ for all $x$ by choosing $a, b$ with $a\alpha(x)b \ne axb$ unless $\alpha(x) = x$. $\square$

**Proposition (the symmetrisation of the signed sandwich).** For all $a, b \in J$,

$$
\tfrac12\bigl(S^{\alpha}_{a,b} + S^{\alpha}_{b,a}\bigr) = U_{a,b}\circ\alpha ,
$$

and the operator on the right lies in $\operatorname{Mult}(J)$; write it $\Sigma^{\alpha}_{a,b} = U_{a,b}\circ\alpha$ and call it the **symmetrised signed sandwich**. The symmetrisation is exactly the twist of the quadratic representation by the grade involution, and it is the signed two-sided operator of the Jordan structure.

*Proof.* $\tfrac12(S^{\alpha}_{a,b}+S^{\alpha}_{b,a})(x) = \tfrac12(a\alpha(x)b+b\alpha(x)a) = U_{a,b}(\alpha(x)) = (U_{a,b}\circ\alpha)(x)$, using the special form of $U_{a,b}$. $\square$

## Composition and the Failure of the Ring Law

### The Unsymmetrised Case

The unsigned and signed sandwiches themselves obey the ring laws, since they are products of one-sided multiplications of $A$: by *The Signed Sandwich on a Ring*, $S_{a,b}S_{c,d} = S_{ac,db}$ and

$$
S^{\alpha}_{a,b}S^{\alpha}_{c,d} = S^{\alpha}_{a\alpha(c),\,b\alpha(d)} .
$$

These two laws are used here and not reproved. They are laws of operators on the module $J$, and the second inserts the grade involution into the parameters, which is the sign rule of the grading.

### The Symmetrised Case

**Theorem (the failed law).** For all $a, b, c, d \in J$,

$$
\Sigma^{\alpha}_{a,b}\,\Sigma^{\alpha}_{c,d} = U_{a,b}\,U_{\alpha(c),\alpha(d)} ,
$$

a product of two quadratic representations. This product is **not** in general of the form $\Sigma^{\alpha}_{e,f}$; indeed it lies in the span of the $U_{e,f}$ only when $U_{a,b}U_{\alpha(c),\alpha(d)}$ is itself a quadratic representation, which is the exception and not the rule. Hence the monoid law of the ring case does not survive the symmetrisation.

*Proof.* From $\Sigma^{\alpha}_{a,b} = U_{a,b}\alpha$ and $\alpha U_{c,d} = U_{\alpha(c),\alpha(d)}\alpha$ (the equivariance of the quadratic representation under the automorphism $\alpha$), the composite is $U_{a,b}\alpha U_{c,d}\alpha = U_{a,b}U_{\alpha(c),\alpha(d)}\alpha^2 = U_{a,b}U_{\alpha(c),\alpha(d)}$. For the failure of the Jordan form, take $\alpha = \mathrm{id}$, $A = M_2(k)$, $a = b = E_{12}$ and $c = d = E_{21}$. Then $U_{a,a}(x) = E_{12}xE_{12} = r\,E_{12}$ and $U_{c,c}(x) = E_{21}xE_{21} = q\,E_{21}$, where $x = \bigl(\begin{smallmatrix}p&q\\ r&s\end{smallmatrix}\bigr)$, so

$$
U_{a,a}U_{c,c}(x) = E_{12}\,(qE_{21})\,E_{12} = q\,E_{12} .
$$

This operator is the $(1,2)$-coordinate functional times the matrix unit $E_{12}$. Suppose it were a quadratic representation $U_{e,f}$ with $e = \bigl(\begin{smallmatrix}a&b\\ c&d\end{smallmatrix}\bigr)$, $f = \bigl(\begin{smallmatrix}p&q_1\\ r&s\end{smallmatrix}\bigr)$. Evaluating at $x = E_{12}$ gives $U_{e,f}(E_{12}) = E_{12}$, whose $(1,2)$-entry is the $(1,2)$-entry of $\tfrac12(eE_{12}f+fE_{12}e)$, namely $\tfrac12(bq_1+q_1b) = bq_1$; hence $bq_1 = 1$. Evaluating at $x = E_{21}$ gives $U_{e,f}(E_{21}) = 0$, whose $(1,2)$-entry is $\tfrac12(bq_1+q_1b) = bq_1$ again; hence $bq_1 = 0$, a contradiction. So the composite is not a quadratic representation. $\square$

**Corollary.** The set $\{\Sigma^{\alpha}_{a,b} : a, b \in J\}$ generates an algebra under composition, but it is not a monoid, and the composition law of the ring case is replaced by the multiplication in the algebra of quadratic representations. The **one-sided** signed operator $x\mapsto a\,\alpha(x)$ of *The Signed Left Multiplication on a Jordan Algebra*, which is linear in a single parameter, is the element from which the symmetrised signed sandwiches are rebuilt in the next articles of this group.

## Reflections Realised by the Signed Sandwich

### The Diagonal Signed Sandwich

**Definition.** For a unit $u \in A^\times$ the **diagonal signed sandwich** is

$$
r_u = S^{\alpha}_{u,u^{-1}} : J \to J, \qquad r_u(x) = u\,\alpha(x)\,u^{-1} .
$$

It is the **signed conjugation** by $u$, and it is an operator of the Jordan structure when it is the twist of the conjugation $U_{u,u^{-1}}$.

**Theorem.** Let $u \in A^\times$. Then

$$
r_u^2 = \operatorname{conj}_{u\alpha(u)} , \qquad r_u^2(x) = u\alpha(u)\,x\,(u\alpha(u))^{-1} .
$$

Hence $r_u$ is an involution, a **reflection**, exactly when $u\,\alpha(u)$ is central in $A$; it is then the inner automorphism of $J$ by $u\alpha(u)$, of order two.

*Proof.* The square is computed from the ring law $S^{\alpha}_{a,b}S^{\alpha}_{c,d} = S^{\alpha}_{a\alpha(c),b\alpha(d)}$ with $a = c = u$ and $b = d = u^{-1}$: $r_u^2 = S^{\alpha}_{u\alpha(u),\,u^{-1}\alpha(u^{-1})}$, and $u^{-1}\alpha(u^{-1}) = (u\alpha(u))^{-1}$ because $\alpha(u^{-1}) = \alpha(u)^{-1}$. The conjugation by an element is the identity exactly when that element is central. $\square$

**Corollary (parity).** If $u$ is fixed by $\alpha$ then $u\alpha(u) = u^2$, and $r_u$ is an involution exactly when $u^2$ is central; if $u$ is negated by $\alpha$ then $u\alpha(u) = -u^2$, central exactly when $u^2$ is central. In particular $u^2 \in Z(A)$ makes $r_u$ an involution whatever the parity of $u$, and this is the criterion inherited from *The Signed Sandwich on a Ring*.

### The Reflection and the Quadratic Representation

**Proposition.** The a symmetrised diagonal signed sandwich is

$$
\Sigma^{\alpha}_{u,u^{-1}} = U_{u,u^{-1}}\circ\alpha , \qquad \Sigma^{\alpha}_{u,u^{-1}}(x) = \tfrac12\bigl(u\alpha(x)u^{-1} + u^{-1}\alpha(x)u\bigr) ,
$$

and it is an element of $\operatorname{Mult}(J)$. It is an involution when $U_{u,u^{-1}}$ commutes with the twist in the appropriate sense; the exact statement and the correspondence between reflections and the elements acting by an involution — with its failure in the degenerate case of a non-central $u\alpha(u)$ — is the subject of *Reflections as Signed Two-Sided Operators on a Jordan Algebra*, next in this group.

*Proof.* The formula is the symmetrisation of $r_u$, together with the identification $\tfrac12(S^{\alpha}_{u,u^{-1}}+S^{\alpha}_{u^{-1},u}) = U_{u,u^{-1}}\alpha$ proved above. $\square$

## A Worked Example

**Example (the matrix Jordan algebra).** Let $A = M_2(k)$ over a field $k$ of characteristic not two, let $\alpha$ be the conjugation $X \mapsto JXJ^{-1}$ with $J = \operatorname{diag}(1,-1)$, a grade involution whose even part is the diagonal matrices and whose odd part the off-diagonal ones, and let $J = M_2(k)^+$ be the special Jordan algebra with the halved product. Take the unit $u = E_{12}+E_{21}$, so that $\alpha(u) = -u$ and $u^{-1} = u$. Then $u\alpha(u) = -u^2 = -I$ is central, so $r_u$ is an involution:

$$
r_u(x) = u\,\alpha(x)\,u^{-1} = u\,\alpha(x)\,u , \qquad r_u^2(x) = (-I)\,x\,(-I)^{-1} = x .
$$

The reflection $r_u$ acts on the Jordan algebra $J$ by the signed conjugation, and its symmetrisation $\Sigma^{\alpha}_{u,u} = U_{u,u}\circ\alpha$ lies in the multiplication algebra. The operator $r_u$ itself does not lie in the multiplication algebra, since $U_{u,u}(x) = uxu$ while $r_u(x) = u\alpha(x)u$ and $\alpha \ne \mathrm{id}$.

**Example (a degenerate sandwich).** With $A = M_2(k)$, $\alpha = \mathrm{id}$ and $u = I + E_{12}$, one has $\alpha(u) = u$ and $u^2 = I + 2E_{12}$, which is not central; $r_u = \operatorname{conj}_u$ has $r_u^2 = \operatorname{conj}_{u^2} \ne \mathrm{id}$, so the sandwich is an automorphism of infinite order and not a reflection. The failure is exactly the non-centrality of $u\alpha(u)$, and it is the degenerate case that the reflection correspondence must exclude.

## Summary

On a special Jordan algebra $J = A^+$ the **unsigned sandwich** is $S_{a,b}(x) = axb$ and the **signed sandwich** is $S^{\alpha}_{a,b}(x) = a\alpha(x)b$, with $S^{\alpha}_{a,b} = S_{a,b}\circ\alpha$; both are operators on the underlying module and obey the ring laws $S_{a,b}S_{c,d} = S_{ac,db}$ and $S^{\alpha}_{a,b}S^{\alpha}_{c,d} = S^{\alpha}_{a\alpha(c),b\alpha(d)}$. The **Jordan two-sided operator** is the symmetrisation: $\tfrac12(S_{a,b}+S_{b,a}) = U_{a,b}$ is the quadratic representation, and $\tfrac12(S^{\alpha}_{a,b}+S^{\alpha}_{b,a}) = U_{a,b}\circ\alpha = \Sigma^{\alpha}_{a,b}$ is the symmetrised signed sandwich, the two being elements of $\operatorname{Mult}(J)$. The ring composition law does **not** survive the symmetrisation: $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d} = U_{a,b}U_{\alpha(c),\alpha(d)}$, a product of quadratic representations that is not itself one in general. The diagonal signed sandwich $r_u = S^{\alpha}_{u,u^{-1}}$ is the signed conjugation $x\mapsto u\alpha(x)u^{-1}$; its square is the conjugation by $u\alpha(u)$, so it is a reflection exactly when $u\alpha(u)$ is central, with the parity corollary that $u^2$ central suffices. The reflection correspondence, with its degenerate cases, is *Reflections as Signed Two-Sided Operators on a Jordan Algebra*; the unsymmetrised signed one-sided operator is *The Signed Left Multiplication on a Jordan Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J = A^+$ | Special unital Jordan algebra with halved product |
| $A$ | The associative algebra whose symmetrisation is $J$ |
| $\alpha$ | Grade involution, an automorphism with $\alpha^2 = \mathrm{id}$ |
| $A_{\bar 0}, A_{\bar 1}$ | Even and odd parts, $J_i = A_i$ |
| $S_{a,b}(x) = axb$ | Unsigned sandwich |
| $U_{a,b} = \tfrac12(S_{a,b}+S_{b,a})$ | Quadratic representation as symmetrised sandwich |
| $S^{\alpha}_{a,b}(x) = a\alpha(x)b$ | Signed sandwich |
| $S^{\alpha}_{a,b} = S_{a,b}\circ\alpha$ | Signed sandwich is the unsigned at $\alpha$ |
| $\Sigma^{\alpha}_{a,b} = U_{a,b}\circ\alpha$ | Symmetrised signed sandwich |
| $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d} = U_{a,b}U_{\alpha(c),\alpha(d)}$ | Failed composition law |
| $r_u = S^{\alpha}_{u,u^{-1}}(x) = u\alpha(x)u^{-1}$ | Diagonal signed sandwich |
| $r_u^2 = \operatorname{conj}_{u\alpha(u)}$ | Reflection iff $u\alpha(u) \in Z(A)$ |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the quadratic representation, the structure group and the inner automorphisms of a Jordan algebra.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the special Jordan algebra $A^+$, sandwiches and the structure group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the grade involution, the two-sided operators built from it and the reflections they realise.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for one-sided and two-sided multiplications in a nonassociative algebra.
- Ottmar Loos, *Symmetric Spaces I: General Theory* (Benjamin, 1969), for the Jordan-theoretic sandwich, the quadratic representation and the order-two elements.
