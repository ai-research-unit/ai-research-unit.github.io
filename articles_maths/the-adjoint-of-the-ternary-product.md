# __The Adjoint of the Ternary Product__

## Introduction

The ternary product $\{x,y,z\}=xy^{*}z$ has three slots, and each of them turns the ternary operator $\Theta_{x,y}$ of the pair $(x,y)$ into an operator of the earlier entries of the group: the third slot gives the plain left multiplication $T_{x\star y,1}$ by the derived product, the middle slot the sandwich $S_{x,z}$, and the first slot the plain right multiplication, as *The Ternary Product as an Operator* records. The present article takes the adjoint of the ternary operator for the sesquilinear pairing $\varphi(x,y)=\tau(xy^{*})$. The operator is $R$-linear in its variable, so its adjoint is taken by the plain rule of *The Sesquilinear Adjoint Operator*, and the whole article turns on the single identity

$$
\Theta_{x,y}^{\dagger}=\Theta_{y,x},
$$

the adjoint of the ternary operator of a pair being the ternary operator of the swapped pair. Three consequences are drawn. The diagonal $\Theta_{x,x}$ is self-adjoint for every element, so the quadratic representation of the Jordan theory is self-adjoint. The operator $\Theta_{x,y}$ is self-adjoint if and only if the derived product $x\star y$ is Hermitian, which ties the operator theory to *Hermitian and Skew-Hermitian Elements*. And the adjoint operation permutes the three readings of the ternary product among themselves, so the ternary product introduces no adjoint that the sandwich and the plain one-sided operators had not already named; this is the operator form of the reversibility that the $J^{*}$-triples carry.

**The boundaries.** The ternary operator, its parities, its three readings and its factorisation through the derived product are *The Ternary Product as an Operator*; the ternary product and its Jordan triple identity are *The Sesquilinear Associator and the Ternary Product*; the Jordan triple systems of the product are *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System* and *Jordan Triples with an Involution*; the quadratic representation is *Jordan Algebras of Sesqualgebras*; the sandwich is *The Sesquilinear Sandwich Operator*; the adjoint operation and the parity obstruction are *The Sesquilinear Adjoint Operator*; the Hermitian elements are *Hermitian and Skew-Hermitian Elements*; the one-sided operators are *The Left and Right Multiplication Operators of a Sesqualgebra*. This article stays inside Part I: no distance, no limit, no completeness.

Throughout, $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, $A$ is a unital associative $R$-algebra with a $\varsigma$-semilinear involution $*$ and $1^{*}=1$, and the function $\tau:A\to R$ is $R$-linear, central and compatible with the involution, $\tau(ab)=\tau(ba)$ and $\tau(x^{*})=\varsigma(\tau(x))$, with the pairing $\varphi(x,y)=\tau(xy^{*})$ perfect. The derived product is $x\star y=xy^{*}$, the ternary product is $\{x,y,z\}=xy^{*}z$, and

$$
\Theta_{x,y}(z)=xy^{*}z=\{x,y,z\}, \qquad S_{a,b}(x)=ax^{*}b, \qquad T_{p,q}(x)=pxq .
$$

The adjoint of an $R$-linear operator $T$ is the operator $T^{\dagger}$ with $\varphi(Tx,y)=\varphi(x,T^{\dagger}y)$, and the adjoint of a $\varsigma$-semilinear operator $S$ is the operator $S^{\dagger}$ with $\varphi(Sx,y)=\varsigma\bigl(\varphi(x,S^{\dagger}y)\bigr)$; both exist and are unique by *The Sesquilinear Adjoint Operator*.

## The Operator and its Adjoint

### The Parity of the Operator

**Proposition (the operator is linear, the second parameter is not).** The operator $\Theta_{x,y}$ is $R$-linear, and the pair map is $R$-bilinear with a $\varsigma$-semilinear second slot,

$$
\Theta_{\lambda x,y}=\lambda\,\Theta_{x,y}, \qquad \Theta_{x,\lambda y}=\varsigma(\lambda)\,\Theta_{x,y}, \qquad \Theta_{x,y}(\lambda z)=\lambda\,\Theta_{x,y}(z) .
$$

**Proof.** The variable $z$ enters the plain product on the right, the first parameter on the left, and the second parameter through the involution. $\square$

**Remark.** The adjoint of $\Theta_{x,y}$ is therefore taken by the plain rule, and the parity obstruction of *The Sesquilinear Adjoint Operator* does not arise: the conjugate-linearity of the ternary product sits in the middle slot, which is a parameter of the operator and not its variable. A parameter can be conjugate-linear while the operator it names is linear, and the adjoint reads the operator and not the parameter.

### The Adjoint Swaps the Parameters

**Theorem (the adjoint of the ternary operator).** For all $x,y\in A$,

$$
\Theta_{x,y}^{\dagger}=\Theta_{y,x};\qquad\text{that is,}\qquad \varphi(\Theta_{x,y}z,w)=\varphi(z,\Theta_{y,x}w)\quad\text{for all }z,w\in A .
$$

**Proof.** By the definition of the pairing, $\varphi(\Theta_{x,y}z,w)=\tau\bigl(xy^{*}zw^{*}\bigr)$, and the cyclicity of $\tau$ turns it into $\tau\bigl(zw^{*}xy^{*}\bigr)$. On the other side, $\varphi(z,\Theta_{y,x}w)=\tau\bigl(z(yx^{*}w)^{*}\bigr)=\tau\bigl(zw^{*}xy^{*}\bigr)$, by the anti-multiplicativity of $*$. The two are equal, and the adjoint is unique. $\square$

**Corollary (the order of the operation).** $\Theta_{x,y}^{\dagger\dagger}=\Theta_{x,y}$, and $\Theta_{x,x}^{\dagger}=\Theta_{x,x}$: the diagonal of the pair map is self-adjoint.

**Proof.** The adjoint operation is of order two by the general theory, and the first identity gives $\Theta_{x,x}^{\dagger}=\Theta_{x,x}$. $\square$

**Remark (the parities of the adjoint).** The adjoint $\Theta_{y,x}$ is, as a function of the pair, $\varsigma$-semilinear in $x$ and $R$-linear in $y$, because that is the parity of the pair map of the swapped pair. The adjoint operation therefore exchanges the two parities of the parameters: the linear parameter of $\Theta_{x,y}$ becomes the conjugate-linear parameter of the adjoint, and conversely. In the factorisation of the next section the same exchange appears as the star on the derived product.

## The Diagonal and the Hermitian Criterion

### The Self-Adjointness of the Diagonal

**Theorem (the quadratic representation is self-adjoint).** For every $x\in A$ the operator $\Theta_{x,x}$ is self-adjoint, and

$$
\Theta_{x,x}=T_{x\star x,1},\qquad \Theta_{x,x}^{\dagger}=T_{(x\star x)^{*},1} .
$$

**Proof.** The first identity is the factorisation of the pair through the derived product, $\Theta_{x,x}=T_{x\star x,1}$, and the diagonal is self-adjoint by the corollary of the adjoint theorem. The second identity is the same factorisation read on the adjoint, and it agrees with the first because the derived square is Hermitian: $(x\star x)^{*}=(xx^{*})^{*}=(x^{*})^{*}x^{*}=xx^{*}=x\star x$. $\square$

**Remark.** The quadratic representation of the Jordan theory is the diagonal of the pair map, and the theorem says that it is self-adjoint whatever the involution and whatever the algebra. In the degenerate case of a commutative algebra with $*=\mathrm{id}$ the operator $U_x=\Theta_{x,x}$ is $2T_{x,1}^{2}-T_{x^{2},1}$ of *The Ternary Product as an Operator*, and its self-adjointness is the classical self-adjointness of the quadratic representation; the general theorem recovers it.

### The Hermitian Criterion

**Theorem (when the ternary operator is self-adjoint).** For $x,y\in A$,

$$
\Theta_{x,y}^{\dagger}=\Theta_{x,y}\quad\Longleftrightarrow\quad x\star y=y\star x\quad\Longleftrightarrow\quad (x\star y)^{*}=x\star y .
$$

The operator of a pair is therefore self-adjoint exactly when the derived product of the pair is Hermitian.

**Proof.** By the adjoint theorem, $\Theta_{x,y}^{\dagger}=\Theta_{y,x}$, and the two operators agree exactly when the derived products $x\star y$ and $y\star x$ agree, because the factorisation $\Theta_{p,q}=T_{p\star q,1}$ identifies the operator with its derived product and the left multiplication does not lose the element. Finally $y\star x=(xy^{*})^{*}=(x\star y)^{*}$, so the agreement of the two derived products is the Hermitian condition. $\square$

**Corollary (the Hermitian pairs).** Every diagonal operator $\Theta_{x,x}$ is self-adjoint, since $x\star x=xx^{*}$ is Hermitian; more generally $\Theta_{x,y}$ is self-adjoint for the pairs whose derived product is Hermitian, for instance $y=cx$ with $c$ a central Hermitian element, where $x\star y=xx^{*}c$ and $y\star x=cxx^{*}$ agree. The condition is not automatic, and it is not met for $y=x^{*}$ in general: for $A=M_2(\mathbb{C})$ and $x=E_{11}+E_{12}$ the derived products $x\star x^{*}=x^{2}=E_{11}+E_{12}$ and $x^{*}\star x=(x^{*})^{2}=E_{11}+E_{21}$ differ, so the operator of that pair is not self-adjoint, while the diagonal $\Theta_{x,x}$ is.

**Remark.** The smallest witness is the pair $x=E_{11}$, $y=E_{21}$ of $M_2(\mathbb{C})$: the derived product is $x\star y=E_{11}E_{12}=E_{12}$, whose star is $E_{21}\neq E_{12}$, so $\Theta_{E_{11},E_{21}}^{\dagger}=\Theta_{E_{21},E_{11}}\neq\Theta_{E_{11},E_{21}}$; the operator of that pair is not self-adjoint, while the diagonal $\Theta_{E_{11},E_{11}}$ is.

## The Three Readings under the Adjoint

The three readings of the ternary product each have an adjoint of the same group, and the adjoint operation permutes them.

**Theorem (the readings and their adjoints).** For all $x,y,z\in A$,

$$
\Theta_{x,y}^{\dagger}=\Theta_{y,x}, \qquad S_{x,z}^{\dagger}=S_{z,x}, \qquad T_{x\star y,1}^{\dagger}=T_{(x\star y)^{*},1} .
$$

**Proof.** The first identity is the adjoint theorem above. The second is the adjoint of the sandwich of *The Sesquilinear Adjoint Operator*, read with the middle reading $\Theta_{x,y}(z)=S_{x,z}(y)$. The third is the adjoint of the plain left multiplication, which sends the parameter to its star; with the factorisation $\Theta_{x,y}=T_{x\star y,1}$ it reproduces the first identity. $\square$

**Corollary (no new adjoint).** The adjoint of the ternary operator of a pair is the plain left multiplication by the star of its derived product,

$$
\Theta_{x,y}^{\dagger}=T_{(x\star y)^{*},1}=T_{y\star x,1},
$$

so the adjoint of the ternary operator is a ternary operator again, and the family of the pair operators is stable under the adjoint.

**Remark.** The stability is a genuine closure statement and not a triviality: the adjoint of the conjugate left multiplication does not stay in the one-sided family, as *The Adjoint of the Conjugate Left Multiplication* records, while the adjoint of the ternary operator stays in the family of the pairs. The reason is that the ternary operator of a pair is a plain left multiplication by a derived product, and the plain left multiplications are closed under the adjoint by the third identity above; the pairs therefore inherit the closure that the derived one-sided operators do not have.

## The Triple and its Reversal

The identity $\Theta_{x,y}^{\dagger}=\Theta_{y,x}$ is the algebraic counterpart of the reversal that the $J^{*}$-triples carry, and it is worth stating without the operator notation.

**Theorem (the reversed triple).** For all $x,y,z,w\in A$,

$$
\varphi\bigl(\{x,y,z\},w\bigr)=\varphi\bigl(z,\{y,x,w\}\bigr).
$$

The triple is reversible: the pairing of $\{x,y,z\}$ with $w$ equals the pairing of $z$ with the triple $\{y,x,w\}$, and this is the statement that the operator of the pair $(x,y)$ has the operator of the reversed pair $(y,x)$ as its adjoint.

**Proof.** The identity is the adjoint theorem written with the ternary product: $\varphi(xy^{*}z,w)=\tau(xy^{*}zw^{*})=\tau(zw^{*}xy^{*})=\varphi(z,yx^{*}w)$. $\square$

**Remark.** The reversibility is the symmetry that the $J^{*}$-triples carry: the operator of a pair has the operator of the reversed pair as its adjoint, so the family of the pair operators is closed under the adjoint, and the first slot of the triple may be exchanged with the outside element against the pairing at the cost of swapping the two middle parameters. Read on the derived product, the reversal is $y\star x=(x\star y)^{*}$: the derived product of the swapped pair is the star of the derived product of the pair, and it is this identity that the self-adjointness criterion of the preceding section turns into a condition on the pair.

## The Degenerations

### The Trivial Base Involution

When $\varsigma=\mathrm{id}$ the twisted rule and the plain rule coincide, and the adjoint of the ternary operator is still $\Theta_{y,x}$; nothing in the article uses the non-triviality of $\varsigma$. The degenerate case is nevertheless the bilinear one: $\varsigma=\mathrm{id}$ requires the involution $*$ to be $R$-linear, so the conjugate transpose of the matrix algebra is replaced by the transpose or by another $R$-linear anti-automorphism, and the derived product $x\star y=xy^{*}$ becomes $R$-bilinear. The adjoint identity and the Hermitian criterion are unchanged in form; the pairing is the $R$-bilinear pairing of *The Adjoint in an Involutive Algebra*, and the theorem reduces to the statement that the adjoint of $z\mapsto xy^{*}z$ is $z\mapsto yx^{*}z$ for that pairing.

### The Trivial Algebra Involution

The other degeneration is $*=\mathrm{id}$. The identity is an anti-automorphism only on a commutative algebra, so $*=\mathrm{id}$ forces $A$ commutative, and the scalar rule then forces $\varsigma=\mathrm{id}$ as well. In this case every element is Hermitian, the derived product is the ordinary product, and the ternary operator is symmetric in its two parameters,

$$
\Theta_{x,y}(z)=xyz=yxz=\Theta_{y,x}(z),
$$

so every operator of a pair is self-adjoint, in agreement with the criterion, and the quadratic representation $U_x=\Theta_{x,x}=2T_{x,1}^{2}-T_{x^{2},1}$ is self-adjoint. The two degenerations therefore meet in the commutative case, and there the reversal of the triple is the commutativity of the product.

## Worked Cases

### The Complex Matrices

Let $A=M_n(\mathbb{C})$ with the conjugate transpose, $\varsigma$ the conjugation, $\tau$ the trace and $\varphi(X,Y)=\operatorname{tr}(XY^{*})$. The ternary operator of the pair $(X,Y)$ is $\Theta_{X,Y}(Z)=XY^{*}Z$, its adjoint is $\Theta_{X,Y}^{\dagger}=\Theta_{Y,X}$, and the criterion reads

$$
\Theta_{X,Y}^{\dagger}=\Theta_{X,Y}\quad\Longleftrightarrow\quad XY^{*}=YX^{*} .
$$

The diagonal $\Theta_{X,X}(Z)=XX^{*}Z$ is self-adjoint for every $X$, and its parameter $XX^{*}$ is Hermitian; for $n=2$ and $X=E_{11}$ the diagonal is $Z\mapsto E_{11}Z$, self-adjoint, while the pair $(E_{11},E_{21})$ has the non-self-adjoint operator computed above. The self-adjoint operators of a pair are those with $XY^{*}$ Hermitian, that is those for which the derived product lies in the Hermitian part of the algebra.

### The Biquaternion Algebra

Let $A=\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the quaternionic conjugation of the basis with conjugated complex coefficients, so that $\varsigma$ is the conjugation and $*$ is an anti-automorphism with $1^{*}=1$; the algebra is the $2\times2$ complex matrix algebra by *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and the statements of the previous case transfer under that isomorphism. The ternary operator of a pair has the operator of the swapped pair as its adjoint, the diagonal is self-adjoint, and the Hermitian criterion reads $x\star y=y\star x$ in the biquaternion algebra, the same condition as in $M_2(\mathbb{C})$ because the derived product and the involution are carried across by the isomorphism.

## Summary

The ternary operator $\Theta_{x,y}(z)=xy^{*}z$ of a pair is $R$-linear, and its adjoint for the pairing $\varphi(x,y)=\tau(xy^{*})$ is the ternary operator of the swapped pair, $\Theta_{x,y}^{\dagger}=\Theta_{y,x}$; equivalently $\varphi(\{x,y,z\},w)=\varphi(z,\{y,x,w\})$, the reversal of the triple. The adjoint operation is of order two and exchanges the two parities of the parameters, and it is the star on the derived product in the factorisation $\Theta_{x,y}=T_{x\star y,1}$, so that $\Theta_{x,y}^{\dagger}=T_{(x\star y)^{*},1}$. The diagonal $\Theta_{x,x}$ is self-adjoint for every element, which is the self-adjointness of the quadratic representation of the Jordan theory, and the operator of a general pair is self-adjoint exactly when the derived product of the pair is Hermitian; the criterion is not automatic, the pair $(E_{11},E_{21})$ of $M_2(\mathbb{C})$ being the smallest witness. The adjoint permutes the three readings of the ternary product among themselves and leaves the family of the pair operators stable, in contrast with the conjugate left multiplication, whose adjoint does not stay in the one-sided family. In the two degenerations of the involution the article reduces to the bilinear case on the one hand and to the commutative case on the other, where every element is Hermitian and every operator of a pair is self-adjoint.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Theta_{x,y}(z)=xy^{*}z=\{x,y,z\}$ | the ternary operator of the pair $(x,y)$, $R$-linear |
| $\Theta_{x,y}^{\dagger}=\Theta_{y,x}$ | the adjoint swaps the two parameters |
| $\varphi(\{x,y,z\},w)=\varphi(z,\{y,x,w\})$ | the reversal of the triple |
| $\Theta_{x,x}^{\dagger}=\Theta_{x,x}=T_{x\star x,1}$ | the diagonal is self-adjoint: the quadratic representation |
| $\Theta_{x,y}^{\dagger}=\Theta_{x,y}\iff(x\star y)^{*}=x\star y$ | the Hermitian criterion |
| $S_{a,b}^{\dagger}=S_{b,a}$ | the adjoint of the sandwich |
| $T_{p,q}^{\dagger}=T_{p^{*},q^{*}}$ | the adjoint of the plain two-sided operator |
| $\Theta_{x,y}^{\dagger}=T_{(x\star y)^{*},1}=T_{y\star x,1}$ | the adjoint as a plain left multiplication |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society Colloquium Publications 39, 1968), for the quadratic representation, its self-adjointness and the Jordan triple systems in which the reversibility of the triple is an axiom.
- Ottmar Loos, *Jordan Pairs* (Lecture Notes in Mathematics 460, Springer, 1975), for the triple products, their adjoints and the reversibility that the Jordan pair carries, the abstract form of the central identity of this article.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (CBMS Regional Conference Series 67, American Mathematical Society, 1987), for the $J^{*}$-algebras, the triple product $xy^{*}z$ and the adjoint of its operator, the standard source of the object of this article.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge Tracts in Mathematics 190, Cambridge University Press, 2012), for the Jordan triples with an involution and the reversibility of the triple, treated with the analysis the present article leaves to Part III.
- Yaakov Friedman and Bernard Russo, "The Gelfand–Naimark theorem for $JB^{*}$-triples", *Duke Mathematical Journal* 53 (1986), for the $J^{*}$-triples and the axioms in which the reversal of the triple appears as the symmetry of the triple product.
