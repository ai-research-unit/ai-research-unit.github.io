
# __Left and Right Multiplication of a Module__

## Introduction

An action of an algebra on a module is a rule, and a rule is an operator: the element $a$ acts on the module as the map $m \mapsto am$. This article isolates that operator — the **left multiplication** by an element — together with its mirror, the **right multiplication** by an element acting on the other side. It computes how the two compose, when they commute, and the representation of the algebra that the left multiplications together define.

The object and its elementary theory are those of *Modules over an Algebra*, which owns the definition of a module, of the regular module and of the action homomorphism; the ambient ring of operators is that of *The Operators on an Algebra*. This article is the first entry of the `- Operator Theory` group of this category, so the marks fixed here — $L_a$ and $R_b$ for the one-sided multiplications, $\rho$ for the structure homomorphism, $L_A$ and $R_B$ for their images — are held by the rest of the group. Only what the one-sided operators need is proved here: the endomorphism ring that is their centralizer is the subject of *Module Endomorphisms*, its algebra structure that of *The Endomorphism Algebra of a Module*, and its units that of *Automorphisms of Modules over an Algebra*.

The article stays inside Part I: no distance, norm, form, topology or limit occurs. The commutation of the two sides is pure associativity, and the representation is a ring homomorphism. Throughout, $R$ is a commutative ring with $1 \neq 0$; $A$ and $B$ are unital associative $R$-algebras, generally noncommutative; $M$ is a left $A$-module unless the side is named; and ${}_A M_B$ is an $(A,B)$-bimodule.

## The One-Sided Multiplications

### Left multiplication

The action of an element on a module is an additive map of the module to itself. It is in fact more, because the action is $R$-bilinear.

**Definition.** Let $M$ be a left $A$-module. For $a \in A$ the **left multiplication** by $a$ is the map

$$
L_a : M \to M, \qquad L_a(m) = am .
$$

**Proposition.** For all $a, a' \in A$ and $r \in R$, the map $L_a$ lies in $\operatorname{End}_R(M)$ and

$$
L_{a+a'} = L_a + L_{a'}, \qquad L_{aa'} = L_a \circ L_{a'}, \qquad L_{ra} = rL_a, \qquad L_1 = \mathrm{id}_M .
$$

Consequently

$$
L : A \to \operatorname{End}_R(M), \qquad a \mapsto L_a,
$$

is a unital homomorphism of $R$-algebras.

*Proof.* Additivity of $L_a$ is the axiom $a(m+n)=am+an$, and $L_a(rm)=a(rm)=r(am)=rL_a(m)$ is the $R$-bilinearity of the action, so $L_a \in \operatorname{End}_R(M)$. The four identities are the module axioms $(a+a')m=am+a'm$, $(aa')m=a(a'm)$, $(ra)m=r(am)$ and $1m=m$, read pointwise; the last two of them say that $L$ preserves the $R$-linear structure and the unit. $\square$

The image of $L$ is the set of operators by which the algebra acts,

$$
L_A = \{L_a : a \in A\} = \rho(A),
$$

and the composition law says it is a subalgebra of $\operatorname{End}_R(M)$, closed under composition and containing the identity. The notation $\rho$ for the structure homomorphism is that of *Modules over an Algebra*.

### Right multiplication

When the module is written with its scalars on the right, the element acts on the right, and the composition reverses.

**Definition.** Let $N$ be a right $B$-module. For $b \in B$ the **right multiplication** by $b$ is the map

$$
R_b : N \to N, \qquad R_b(n) = nb .
$$

**Proposition.** For all $b, b' \in B$ and $r \in R$, the map $R_b$ lies in $\operatorname{End}_R(N)$ and

$$
R_{b+b'} = R_b + R_{b'}, \qquad R_{bb'} = R_{b'} \circ R_b, \qquad R_{rb} = rR_b, \qquad R_1 = \mathrm{id}_N .
$$

Hence $R : B \to \operatorname{End}_R(N)$ is a unital anti-homomorphism of $R$-algebras, equivalently the unital homomorphism

$$
R : B^{\mathrm{op}} \to \operatorname{End}_R(N), \qquad b \mapsto R_b,
$$

where $B^{\mathrm{op}}$ is the opposite algebra.

*Proof.* The additive and scalar identities are the right-module axioms as before. For the product, $R_{bb'}(n)=n(bb')=(nb)b'=R_{b'}(nb)=R_{b'}(R_b(n))$, so $R_{bb'}=R_{b'}R_b$, which is the reversed composition; reversing the product of $B$ turns an anti-homomorphism into a homomorphism. $\square$

Thus the two sides are not symmetric in the algebra: the left action is a homomorphism, the right action is a homomorphism of the opposite algebra. This is the module-level form of the asymmetry recorded in *Modules over an Algebra* for the regular module.

### The two sides on one object

An $(A,B)$-bimodule carries both actions, and the two are required to commute.

**Definition.** Let $M$ be an $(A,B)$-bimodule. Its **two-sided operators** are the composites $L_aR_b$ and $R_bL_a$, with $a \in A$, $b \in B$.

**Proposition.** On a bimodule the two sides commute,

$$
L_a R_b = R_b L_a \qquad (a \in A,\ b \in B),
$$

and this identity is exactly the bimodule axiom $a(mb)=(am)b$.

*Proof.* Evaluating both sides at $m$ gives $a(mb)$ and $(am)b$, which the bimodule axiom declares equal. $\square$

The proposition is the reason the two-sided operators of the following articles — the sandwich and its signed twist — are well defined as single maps.

## Commutation of the One-Sided Actions

### The converse reading

The commutation above was derived from the bimodule axiom; it also generates it.

**Theorem.** Let an abelian group $M$ carry a left $A$-action and a right $B$-action. Then $M$ is an $(A,B)$-bimodule exactly when the two actions commute.

*Proof.* If $M$ is a bimodule the axiom gives the commutation. Conversely, if $am$ and $mb$ are defined for all $a,m,b$, each turning $M$ into a module on its side, and if $L_aR_b=R_bL_a$ for all $a,b$, then $a(mb)=(am)b$, which is the only clause joining the two actions. $\square$

### The general failure

For a left module alone the map $R_b$ is not defined, so there is nothing to commute. The failure is visible already on the algebra: $L_a(b)=ab$ and $L_b(a)=ba$ need not agree, and $L_a$ is not an endomorphism of the left regular module when $a$ is not central.

**Proposition.** On ${}_A A$ the left multiplication $L_a$ is $A$-linear exactly when $a \in Z(A)$; the right multiplication $R_a$ is $A$-linear for every $a$.

*Proof.* $L_a(bc)=abc$ while $bL_a(c)=bac$, and these agree for all $b,c$ exactly when $a$ is central. For the right multiplication, $R_a(bc)=(bc)a=b(ca)=bR_a(c)$. $\square$

This is the asymmetry of *Automorphisms of Modules over an Algebra* seen from the operator side: the endomorphisms of the regular module are the right multiplications, not the left ones.

### The centralizer of one side

The two one-sided images are mutual centralizers on the regular module.

**Proposition.** In $\operatorname{End}_R(A)$ the centralizer of $L_A$ is $R_A$ and the centralizer of $R_A$ is $L_A$:

$$
L_A' = R_A, \qquad R_A' = L_A .
$$

*Proof.* A map $f$ commutes with every $L_a$ exactly when $f(ab)=a f(b)$ for all $a,b$, that is, when $f$ is $A$-linear; by *Automorphisms of Modules over an Algebra* the $A$-linear endomorphisms of ${}_A A$ are the right multiplications, so $L_A'=R_A$. The second identity is the same statement read in $A^{\mathrm{op}}$, or directly: $f(bc)=f(b)c$ for all $b,c$ says $f=R_{f(1)}$. $\square$

## The Representation They Define

### The structure homomorphism

The map $L$ is not an auxiliary device; it is the module.

**Proposition.** Giving $M$ the structure of a left $A$-module is the same as giving a unital $R$-algebra homomorphism $\rho : A \to \operatorname{End}_R(M)$; the operator $L_a$ is the image of $a$.

*Proof.* The axioms of a left module are the axioms of a unital ring homomorphism, as *Modules over an Algebra* records. $\square$

The kernel of $\rho$ is the **annihilator** of the module,

$$
\operatorname{Ann}_A(M) = \{a \in A : am = 0 \text{ for all } m \in M\},
$$

a two-sided ideal, and $M$ is **faithful** when $\rho$ is injective, equivalently when $\operatorname{Ann}_A(M)=0$. The first isomorphism theorem for rings gives

$$
L_A = \rho(A) \cong A / \operatorname{Ann}_A(M)
$$

as $R$-algebras, so the image of the action is the quotient of the algebra by the ideal that acts trivially. Enlarging $A$ by an ideal inside the annihilator changes nothing: the operators, and therefore the module, are the same.

### Faithfulness

Faithfulness is a property of the action, not of the module.

**Proposition.** Let $M$ be a left $A$-module and let $a \in A$ with $L_a = 0$. Then $a \in \operatorname{Ann}_A(M)$. The algebra generated by the one-sided multiplications is $\rho(A)$, and it is a faithful $A/\operatorname{Ann}_A(M)$-module.

*Proof.* $L_a=0$ says $am=0$ for all $m$, which is the definition of the annihilator; the rest is the isomorphism above. $\square$

### Where the two-sided operators act

For a bimodule the two images commute, so the algebra generated by all the one-sided operators is the image of the tensor product.

**Proposition.** Let ${}_A M_B$ be a bimodule and let $C$ be the $R$-subalgebra of $\operatorname{End}_R(M)$ generated by $L_A \cup R_B$. Then $C$ is the $R$-span of the products $L_aR_b$, and

$$
C \cong (A \otimes_R B^{\mathrm{op}}) / \operatorname{Ann},
$$

for the kernel $\operatorname{Ann}$ of the map $A \otimes_R B^{\mathrm{op}} \to \operatorname{End}_R(M)$ that sends $a \otimes b$ to $L_aR_b$.

*Proof.* The commuting of the two sides lets every word in the generators be written as a sum of products $L_{a_1}\cdots L_{a_k}R_{b_1}\cdots R_{b_l}=L_{a_1\cdots a_k}R_{b_1\cdots b_l}=L_{a}R_{b}$ with $a=\prod a_i$, $b=\prod b_j$, so the span of these products is closed under composition and contains the identity: it is $C$. The assignment $a \otimes b \mapsto L_aR_b$ is $R$-bilinear, hence a homomorphism $A \otimes_R B^{\mathrm{op}} \to \operatorname{End}_R(M)$ by the universal property of the tensor product, and its image is the span of the $L_aR_b$. The first isomorphism theorem gives the displayed quotient. $\square$

The construction is the algebra-level form of the commuting actions, and it is the reason a bimodule over $A$ is the same thing as a module over $A \otimes_R A^{\mathrm{op}}$; the tensor product of algebras is the subject of *Tensor Products of Algebras*.

### The double centralizer, named

The commutant of one side is computable from the other, and the two fit into a longer chain that is not developed here.

**Proposition.** Let $M$ be a bimodule as above and let $C = L_A R_B$. Then the centralizer of $C$ in $\operatorname{End}_R(M)$ is the set of maps commuting with both sides. In particular, if $B = A$ and the right action is the opposite of the left, the centralizer of $L_A$ is $\operatorname{End}_A(M)$.

*Proof.* $f$ commutes with all products $L_aR_b$ exactly when it commutes with each of $L_a$ and $R_b$, since these are among the products. $\square$

The inclusion $L_A R_B \subseteq \operatorname{End}_{C'}(M)$ is the **double centralizer** or bicommutant relation; the theorem that it is an equality when $M$ is a faithful finite-dimensional module over a simple algebra is stated in the literature and is not used here. The endomorphism ring on the other side of the relation is the subject of the next article.

## Examples

**(a) A field.** If $A=F$ is a field, then $L_\lambda = \lambda\,\mathrm{id}_M$ and $L_F = F\cdot\mathrm{id}_M$, a one-dimensional algebra of operators; every $F$-linear map is $A$-linear, and $L_F' = \operatorname{End}_F(M)$.

**(b) The regular module.** For $M={}_A A$, the left multiplications are $L_a(b)=ab$ with $L_A \cong A$, and the right multiplications are $R_a(b)=ba$ with $R_A \cong A^{\mathrm{op}}$; the two commute by associativity, so ${}_A A_A$ is a bimodule, and the products $L_aR_b$ are the two-sided operators of that bimodule.

**(c) The free module.** For $M={}_A A^n$, the action is componentwise and $L_A \cong A$ when $A$ is nonzero, because $L_a=0$ forces $a=0$ by acting on the first basis vector; the one-sided multiplications are the scalar multiplications on the free module, and the matrices appear only among the endomorphisms of $M$, not among its multiplications.

**(d) The defining module of a matrix algebra.** For $A=M_n(F)$ and $M=F^n$, the map $L : M_n(F) \to \operatorname{End}_F(F^n)$ is an isomorphism: the left multiplications are exactly the matrices. Consequently $L_A = \operatorname{End}_F(M)$, and its centralizer is $F\cdot\mathrm{id}_M$, the scalars; the general module theory of this case is that of *Automorphisms of Modules over an Algebra*.

**(e) The quaternions.** For $A=\mathbb{H}$ and $M=\mathbb{H}$ the left multiplications are the left quaternion multiplications and $L_{\mathbb{H}} \cong \mathbb{H}$; the right multiplications are the right quaternion multiplications, $R_{\mathbb{H}} \cong \mathbb{H}^{\mathrm{op}} \cong \mathbb{H}$, and $L_{\mathbb{H}}' = R_{\mathbb{H}}$. Right multiplication by a non-real quaternion is not a left multiplication, so the two four-dimensional images are distinct inside $\operatorname{End}_{\mathbb{R}}(\mathbb{H}) \cong M_4(\mathbb{R})$.

**(f) The biquaternions.** For $A=\mathbb{B} \cong M_2(\mathbb{C})$ over $\mathbb{C}$ and $M=\mathbb{C}^2$, the left multiplications reproduce the matrices, $L_{\mathbb{B}} \cong \mathbb{B}$, and the right multiplications give $\mathbb{B}^{\mathrm{op}} \cong \mathbb{B}$; the two images are distinct.

**(g) A commutative algebra.** If $A$ is commutative then $L_a = R_a$ as operators on ${}_A A$, and the distinction between the two sides disappears, exactly as it does for the module structure itself.

## Summary

A left $A$-module $M$ carries, for each $a \in A$, the $R$-linear operator $L_a(m)=am$, and the assignment $a \mapsto L_a$ is a unital $R$-algebra homomorphism $L : A \to \operatorname{End}_R(M)$ whose image $L_A$ is the algebra of operators by which $A$ acts; giving the module structure is the same as giving this homomorphism, and $L_A \cong A/\operatorname{Ann}_A(M)$. A right $B$-module carries the operators $R_b(n)=nb$, and $R : B \to \operatorname{End}_R(N)$ is a unital anti-homomorphism, equivalently a homomorphism of $B^{\mathrm{op}}$. On an $(A,B)$-bimodule both sides are defined and commute, $L_aR_b=R_bL_a$, and the commutation is the bimodule axiom; conversely two commuting actions make the object a bimodule. The left multiplications alone do not commute with each other, and on the regular module $L_a$ is $A$-linear only when $a$ is central, while $R_a$ always is: the two images are mutual centralizers, $L_A'=R_A$ and $R_A'=L_A$. The algebra generated by the two sides of a bimodule is the image of $A \otimes_R B^{\mathrm{op}}$ under $a \otimes b \mapsto L_aR_b$, which is the algebra-level form of the commuting actions. The commutant $L_A'$ on a module is the endomorphism ring, which is the subject of the next article; the double centralizer statement that would close the chain is named and not used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity $1 \neq 0$ |
| $A$, $B$ | unital associative $R$-algebras, generally noncommutative |
| $M$, $N$ | modules; $M$ a left $A$-module unless the side is named |
| ${}_A M_B$ | $(A,B)$-bimodule, with commuting left $A$- and right $B$-actions |
| $L_a(m)=am$ | left multiplication by $a$, an operator in $\operatorname{End}_R(M)$ |
| $R_b(n)=nb$ | right multiplication by $b$, an operator in $\operatorname{End}_R(N)$ |
| $L : A \to \operatorname{End}_R(M)$ | the structure homomorphism, $a \mapsto L_a$ |
| $R : B^{\mathrm{op}} \to \operatorname{End}_R(N)$ | the right action read as a homomorphism |
| $L_A$, $R_B$ | the images of the two actions |
| $\rho$ | the structure homomorphism, $=\rho(a)(m)=am$ |
| $\operatorname{Ann}_A(M)$ | annihilator of $M$, the kernel of $\rho$ |
| ${}_A A$, $A_A$ | left and right regular modules |
| $A^{\mathrm{op}}$ | opposite algebra, product $a \cdot_{\mathrm{op}} b = ba$ |
| $Z(A)$ | centre of $A$ |
| $L_A'$ | centralizer of $L_A$ in $\operatorname{End}_R(M)$ |

## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, second edition, 1992), for the action homomorphism, the annihilator and the regular module.
- Nicolas Bourbaki, *Algebra I* (Springer, 1989), for the correspondence between modules and algebra homomorphisms and for the bimodule axioms.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the one-sided multiplications and the opposite algebra.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for the centralizer description of the endomorphism ring and the double centralizer theorem.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, second edition, 2009), for bimodules and the tensor product of algebras.
