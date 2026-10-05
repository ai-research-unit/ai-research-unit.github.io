# __The Left and Right Multiplication Operators of a Sesquialgebra__

## Introduction

Every element of a sesquialgebra gives two operators on the underlying module, the left multiplication $L_a(x) = a \star x$ and the right multiplication $R_a(x) = x \star a$. The two scalar rules of the category split them: $L_a$ is $\varsigma$-semilinear while $R_a$ is $R$-linear, and the split is not an accident of notation but the operator-level form of the rules themselves. This article reads the two families as operators: the modules in which they live, the laws of their composition, the two maps $a \mapsto L_a$ and $a \mapsto R_a$ that the product defines, and the reason a single faithful linear representation cannot carry the whole product.

The subject is the operator theory of the category, and it belongs to the group *Operator Theory* of the sesquialgebras. The definitions of the two operators and their composition in the associative case are in *Sesquialgebras*, §*The Left and the Right Multiplication*; what is added here is the place of the operators among the semilinear endomorphisms, the composition in the standard example, the reading of the two families as representations, and the obstruction to a single linear one. The classical counterpart, where the product is bilinear and the left multiplications compose exactly when the algebra is associative, is *Left and Right Multiplication*; the proposition that locates associativity in the composition of the left multiplications is in *Associative Algebras*, and the analogue for a Jordan product is *The Left and Right Multiplication Operators on a Jordan Algebra*.

The setting is that of *Sesquialgebras*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, $A$ is an $R$-module with a product additive in each variable satisfying the two scalar rules, and the product is written $\star$. When the example is the standard one, $A$ is an associative $R$-algebra with a $\varsigma$-semilinear involution $*$ and $x \star y = xy^{*}$; in that case juxtaposition denotes the associative product of $A$ and $*$ the involution. The fixed ring is $R^{\varsigma} = \{\lambda \in R : \varsigma(\lambda) = \lambda\}$; the two halves of $A$ and the scalars that preserve them are *Hermitian and Skew-Hermitian Elements*; the case $\varsigma = \mathrm{id}$, where the two families collapse into one, is *Left and Right Multiplication*.

---

## The Two Operators

### The Definition

**Definition.** For $a \in A$ the **left multiplication** and the **right multiplication** of the sesquilinear product are

$$
L_a(x) = a \star x , \qquad R_a(x) = x \star a .
$$

Both are additive in $x$, since the product is additive in each variable. The definition is that of *Sesquialgebras*, §*The Left and the Right Multiplication*, and it is recalled here because the operators are the subject.

### The Two Parities

**Proposition (the parity of the two operators).** For every $a \in A$ the left multiplication $L_a$ is $\varsigma$-semilinear and the right multiplication $R_a$ is $R$-linear:

$$
L_a(\lambda x) = \varsigma(\lambda)L_a(x) , \qquad R_a(\lambda x) = \lambda R_a(x) .
$$

Consequently $L_a$ is $R^{\varsigma}$-linear and lies in $\operatorname{End}_{R^{\varsigma}}(A)$, while $R_a$ lies in $\operatorname{End}_{R}(A)$.

**Proof.** The two displayed identities are the two scalar rules of the sesquialgebra read at $x$, and they are the computation of *Sesquialgebras*, §*The Left and the Right Multiplication*. For the last statement, a map $f$ with $f(\lambda x) = \varsigma(\lambda)f(x)$ satisfies $f(\mu x) = \varsigma(\mu)f(x) = \mu f(x)$ for $\mu \in R^{\varsigma}$, so it is $R^{\varsigma}$-linear; the same reading gives the $R$-linearity of $R_a$. $\square$

**Remark.** The two operators therefore have opposite parities, and this is the whole difference from the bilinear case: over a ring with $\varsigma = \mathrm{id}$ both are $R$-linear and the two families are two subfamilies of one endomorphism ring. When $\varsigma \neq \mathrm{id}$ no single ring of $R$-linear endomorphisms contains both: the common home of the two families is $\operatorname{End}_{R^{\varsigma}}(A)$, which contains $\operatorname{End}_{R}(A)$, strictly in the standard examples, where the conjugation is $R^{\varsigma}$-linear but not $R$-linear. The two families are the operator-level reason the category carries two classes of operators, and the bilinear case is the one in which the two classes meet.

**Proposition (the action on the parameter).** The assignment $a \mapsto L_a$ is $R$-linear, and the assignment $a \mapsto R_a$ is $\varsigma$-semilinear:

$$
L_{\lambda a} = \lambda L_a , \qquad R_{\lambda a} = \varsigma(\lambda)R_a .
$$

**Proof.** $L_{\lambda a}(x) = (\lambda a) \star x = \lambda(a \star x) = \lambda L_a(x)$ by the first scalar rule, and $R_{\lambda a}(x) = x \star (\lambda a) = \varsigma(\lambda)(x \star a) = \varsigma(\lambda)R_a(x)$ by the second. $\square$

**Remark.** The parities are exchanged between the operator and its parameter: the left family is linear in its parameter and its values are conjugate-linear, the right family is conjugate-linear in its parameter and its values are linear. The product of the two parities is the same on the two sides, which is the sense in which the two families carry the same information through opposite routes.

## The Composition

### The Associative Case

**Proposition.** Suppose the product of $A$ is associative. Then

$$
L_aL_b = L_{a \star b} , \qquad R_aR_b = R_{b \star a} , \qquad L_aR_b = R_bL_a .
$$

**Proof.** The three identities are the associative law read in the three possible orders, and they are the ones of *Sesquialgebras*, §*The Left and the Right Multiplication*: for $x \in A$ one has $L_aL_b(x) = a \star (b \star x) = (a \star b) \star x = L_{a \star b}(x)$, and the other two are the same computation. $\square$

**Corollary.** When the product is associative, $a \mapsto L_a$ is an algebra homomorphism $A \to \operatorname{End}_{R^{\varsigma}}(A)$ with $\varsigma$-semilinear values, $a \mapsto R_a$ is an algebra anti-homomorphism $A \to \operatorname{End}_{R}(A)$ with $R$-linear values, and the two images commute.

**Proof.** The composition laws say that $L$ respects products, so it is a homomorphism, and that $R$ reverses them, so it is an anti-homomorphism; the last identity says that every left multiplication commutes with every right multiplication. $\square$

**Remark.** Associativity is exactly the hypothesis that makes the two families compose inside themselves, and it is the same criterion as in the bilinear case: *Associative Algebras* locates it in the identity $L(ab) = L(a)L(b)$, and the sesquilinear statement differs only in the module that receives the operators, $\operatorname{End}_{R^{\varsigma}}(A)$ rather than $\operatorname{End}_{R}(A)$. For a sesquialgebra of full type associativity forces $\varsigma = \mathrm{id}$, by the theorem of *Sesquialgebras*, §*The Collapse at the Identity*, so the associative case of the present proposition is the bilinear one.

### The Standard Example

**Proposition (the composition in the standard example).** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution and let $x \star y = xy^{*}$. Write $T_{p,q}(x) = p\,x\,q$ for the ordinary two-sided multiplication. Then

$$
L_aL_b = T_{a,\,b^{*}} , \qquad R_aR_b = T_{1,\,(a b)^{*}} ,
$$

and $L_aR_b \neq R_bL_a$ in general.

**Proof.** In the standard example $L_a(x) = a x^{*}$, so $L_aL_b(x) = a(b x^{*})^{*} = a x b^{*} = T_{a,b^{*}}(x)$, and $R_a(x) = x a^{*}$, so $R_aR_b(x) = (x b^{*})a^{*} = x b^{*}a^{*} = x(ab)^{*} = T_{1,(ab)^{*}}(x)$. For the last statement $L_aR_b(x) = a(x b^{*})^{*} = ab\,x^{*}$ while $R_bL_a(x) = (a x^{*})b^{*} = a x^{*} b^{*}$, and the two are equal for all $a$ and $b$ exactly when $A$ is commutative and the involution is trivial, so they differ for some pair as soon as $A$ is noncommutative or the involution is nontrivial. $\square$

**Remark.** The composition of two left multiplications is again a two-sided multiplication but not a left multiplication, and the reason is that the derived operation is not associative: the two sides of $L_aL_b = L_{a \star b}$ would read $a x b^{*}$ and $a b\,x^{*}$, which differ. The standard example therefore shows the composition law of the associative case failing in the smallest possible way, with a two-sided operator as the residue. That operator is the subject of *The Sesquilinear Sandwich Operator*, where the family $T_{p,q}$ and the conjugate-linear family attached to it are developed together.

## The Two Representations

### The Homomorphism and the Anti-Homomorphism

**Definition.** The **left regular map** is $\lambda_A : A \to \operatorname{End}_{R^{\varsigma}}(A)$, $\lambda_A(a) = L_a$, and the **right regular map** is $\rho_A : A \to \operatorname{End}_{R}(A)$, $\rho_A(a) = R_a$.

**Proposition.** The map $\lambda_A$ is always $R$-linear, and it satisfies $\lambda_A(a \star b) = \lambda_A(a)\lambda_A(b)$ for all $a, b$ if and only if the product of $A$ is associative; the map $\rho_A$ is always $\varsigma$-semilinear, and it satisfies $\rho_A(a \star b) = \rho_A(b)\rho_A(a)$ for all $a, b$ if and only if the product is associative.

**Proof.** The linearity and the semilinearity are the proposition on the parameter. For the multiplicativity, $\lambda_A(a \star b)(x) = (a \star b) \star x$ and $\lambda_A(a)\lambda_A(b)(x) = a \star (b \star x)$, which are equal for every $x$ exactly when the product is associative; the computation for $\rho_A$ is the same with the order of the two factors reversed. $\square$

**Remark.** The two maps are the two halves of the regular representation of a sesquialgebra, and they are not the same map: one is linear and multiplicative into the conjugate-linear operators, the other is conjugate-linear and anti-multiplicative into the linear ones. In the bilinear case they are the ordinary left and right regular representations of an associative algebra, by the theorem of *Associative Algebras* that a representation of an algebra and a module over it are the same thing; in the sesquilinear case there are two such maps and no single one of them is linear in both the parameter and the argument.

### The Failure of a Single Linear Representation

**Proposition (the obstruction).** Let $A$ be a sesquialgebra with $\varsigma \neq \mathrm{id}$, let $a, x \in A$, and suppose that $L_a$ is $R$-linear. Then $(\lambda - \varsigma(\lambda))(a \star x) = 0$ for every $\lambda \in R$. Consequently $L_a$ is not $R$-linear as soon as there is an $x$ with $a \star x$ of zero annihilator.

**Proof.** $L_a(\lambda x) = \varsigma(\lambda)L_a(x)$ and $R$-linearity requires $L_a(\lambda x) = \lambda L_a(x)$; subtracting the two expressions gives $(\varsigma(\lambda) - \lambda)(a \star x) = 0$. If $a \star x$ has zero annihilator this forces $\varsigma(\lambda) = \lambda$ for every $\lambda$, that is $\varsigma = \mathrm{id}$, contrary to the hypothesis. $\square$

**Corollary.** Let $A$ be of full type with $\varsigma \neq \mathrm{id}$. Then the left multiplication is not an $R$-algebra representation: there is no $R$-algebra map $\rho : A \to \operatorname{End}_{R}(A)$ with $\rho(a) = L_a$ for every $a$.

**Proof.** Such a $\rho$ would make each $\rho(a) = L_a$ an $R$-linear map. Fix $\lambda \in R$ and put $c_{\lambda} = \lambda - \varsigma(\lambda)$. The proposition applied to every $a$ and every $x$ gives $c_{\lambda}(a \star x) = 0$, that is $c_{\lambda} \cdot (A \star A) = 0$. Since the products generate $A$, the element $c_{\lambda}$ vanishes on all of $A$, and since $A$ has no nonzero left annihilator, $c_{\lambda} = 0$. So $\varsigma(\lambda) = \lambda$ for every $\lambda \in R$, that is $\varsigma = \mathrm{id}$, contrary to the hypothesis. $\square$

**Remark.** The corollary is the precise sense in which a single faithful linear representation cannot carry the whole product: the left multiplication of a sesquialgebra is conjugate-linear, so the regular module $A_A$ is not a module over $A$ unless the product is bilinear. The representation theory of a sesquialgebra is therefore the theory of the conjugate-linear operators on the left and of the linear ones on the right, and it is the reason the operator theory of the category carries two classes of operators rather than one. The same split is behind the two adjoints that a conjugate-linear operator requires, the subject of *The Sesquilinear Adjoint Operator*.

## Worked Cases

### The Complex Matrices

Let $A = M_n(\mathbb{C})$ with the conjugate transpose and $\varsigma$ the complex conjugation, so that $x \star y = xy^{*}$. The left multiplication $L_a(x) = ax^{*}$ is conjugate-linear: $L_a(\lambda x) = \bar{\lambda}L_a(x)$, and for the imaginary unit $\lambda$ one gets $L_a(iX) = -i\,L_a(X)$, so no $L_a$ with $a \neq 0$ is complex-linear. The right multiplication $R_a(x) = xa^{*}$ is linear. The composition laws of the standard example read $L_aL_b = T_{a,b^{*}}$ and $R_aR_b = T_{1,(ab)^{*}}$, and the two-sided operators $T_{p,q}$ are the linear maps with $T_{p,q}(iX) = i\,T_{p,q}(X)$; the product $L_aL_b$ is the composition of two conjugate-linear maps and is therefore linear, as the parities require. On the Hermitian part the left multiplication by a Hermitian $a$ is the operator $h \mapsto ah$, and on the skew-Hermitian part it is $s \mapsto as^{*} = -as$; the two differ by the sign, which is the operator form of the anti-fixed subspace of *Hermitian and Skew-Hermitian Elements*.

### The Field

Let $A = \mathbb{C}$ over $R = \mathbb{C}$ with $\varsigma$ the conjugation, so that the fixed ring is $R^{\varsigma} = \mathbb{R}$, and let $x \star y = x\bar{y}$. Then $L_a(x) = a\bar{x}$ and $R_a(x) = x\bar{a}$. The right multiplication is the multiplication by the scalar $\bar{a}$ and is $\mathbb{C}$-linear; the left multiplication is the composition of the multiplication by $a$ with the conjugation, and for $a \neq 0$ it is $\mathbb{R}$-linear but not $\mathbb{C}$-linear. The two endomorphism rings therefore differ: $\operatorname{End}_{R^{\varsigma}}(A) = \operatorname{End}_{\mathbb{R}}(\mathbb{C})$ is the ring of the $\mathbb{R}$-linear maps, of four real parameters, and it strictly contains $\operatorname{End}_{R}(A) = \operatorname{End}_{\mathbb{C}}(\mathbb{C})$, the multiplications by the complex scalars, of two. The field exhibits the obstruction in the simplest way: $L_1$ is the conjugation, which is not $\mathbb{C}$-linear, and the hypothesis of the proposition is met because $1 \star 1 = 1$ has zero annihilator and the imaginary unit lies outside the fixed ring. The composition is $L_aL_b(x) = a\bar{b}\,x$, a $\mathbb{C}$-linear map, which is the field form of $L_aL_b = T_{a,b^{*}}$ with $T_{p,q}(x) = pqx$.

## Summary

The left and the right multiplication of a sesquialgebra are $L_a(x) = a \star x$ and $R_a(x) = x \star a$. The left operator is $\varsigma$-semilinear and lies in $\operatorname{End}_{R^{\varsigma}}(A)$; the right operator is $R$-linear and lies in $\operatorname{End}_{R}(A)$; the parameter maps have the exchanged parities, $a \mapsto L_a$ being $R$-linear and $a \mapsto R_a$ being $\varsigma$-semilinear.

When the product is associative the left multiplications compose, $L_aL_b = L_{a \star b}$, the right ones anti-compose, $R_aR_b = R_{b \star a}$, and the two families commute; associativity is exactly the condition, as in the bilinear case, and a sesquialgebra of full type is then bilinear. In the standard example the composition leaves the family, $L_aL_b = T_{a,b^{*}}$ and $R_aR_b = T_{1,(ab)^{*}}$, the residue being a two-sided multiplication. The two regular maps are the two halves of the regular representation, one linear and multiplicative, the other conjugate-linear and anti-multiplicative, and a single faithful linear representation cannot carry the whole product, because the left multiplication is conjugate-linear and the regular module $A_A$ is a module over $A$ only when the product is bilinear.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_a(x) = a \star x$ | the left multiplication, $\varsigma$-semilinear |
| $R_a(x) = x \star a$ | the right multiplication, $R$-linear |
| $\operatorname{End}_{R^{\varsigma}}(A)$ | the conjugate-linear operators, the home of $L_a$ |
| $\operatorname{End}_{R}(A)$ | the linear operators, the home of $R_a$ |
| $L_{\lambda a} = \lambda L_a$ | the left family is linear in its parameter |
| $R_{\lambda a} = \varsigma(\lambda)R_a$ | the right family is conjugate-linear in its parameter |
| $L_aL_b = L_{a \star b}$ | the composition in the associative case |
| $R_aR_b = R_{b \star a}$ | the anti-composition in the associative case |
| $L_aR_b = R_bL_a$ | the commutation in the associative case |
| $T_{p,q}(x) = pxq$ | the ordinary two-sided multiplication |
| $L_aL_b = T_{a,b^{*}}$ | the composition in the standard example |
| $\lambda_A(a) = L_a$, $\rho_A(a) = R_a$ | the left and the right regular maps |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the regular representation, the left and the right multiplication of an algebra, and the semilinear maps.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the operators attached to a ring with involution and the conjugate-linear maps they produce.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the regular representation of a ring and the module theory attached to it.
- The companion articles of this series: *Sesquialgebras*, *Hermitian and Skew-Hermitian Elements*, *Associative Algebras*, *Left and Right Multiplication*, *The Sesquilinear Sandwich Operator*, *The Sesquilinear Adjoint Operator* and *The Left and Right Multiplication Operators on a Jordan Algebra*.
