# __The Adjoint of the Bounded Ternary Product__

## Introduction

The ternary product of a sesqualgebra is $\{x,y,z\}=xy^{*}z$, and its operator form is the **pair operator** $\Theta_{x,y}(z)=\{x,y,z\}$, bounded, linear in the variable and the ordinary left multiplication by the derived product, $\Theta_{x,y}=T_{x\star y,1}=L_{x\star y}$, as *The Bounded Ternary Product* records. The present article takes the adjoint of the pair operator for the canonical pairing $h(x,y)=x^{*}y$ of the layer, and the whole article turns on the single identity

$$
\Theta_{x,y}^{\dagger}=\Theta_{y,x},
$$

the adjoint of the pair operator of $(x,y)$ being the pair operator of the swapped pair. Because the pair operator is a left multiplication, and the adjointable bounded linear operators of *Adjoints of Bounded Sesquilinear Operators* are exactly the left multiplications, the identity is not an accident but the characterisation applied to the derived product: $\Theta_{x,y}^{\dagger}=L_{(x\star y)^{*}}=L_{y\star x}=\Theta_{y,x}$, the star of the derived product being the derived product of the swapped pair.

Three consequences are drawn, and they are the same three as in the algebraic layer. The diagonal $\Theta_{x,x}$ is self-adjoint for every element, because $x\star x=xx^{*}$ is Hermitian: this is the self-adjointness of the quadratic representation of the Jordan theory, now with a norm. The pair operator is self-adjoint exactly when its derived product is Hermitian, which ties the operator theory to the self-adjoint elements. And the adjoint operation permutes the three readings of the ternary product, so the family of the pair operators is stable under the adjoint and introduces no operator that the sandwich and the one-sided families had not already named; the identity is the operator form of the reversibility of the $J^{*}$-triple.

**The boundaries.** The ternary product, its bound, the pair operators and the completion as a Banach $J^{*}$-triple are *The Bounded Ternary Product*; the ternary operator, its three readings and its factorisation are *The Ternary Product as an Operator*; the algebraic adjoint and the reversibility are *The Adjoint of the Ternary Product*; the adjoint of the one-sided operators, the pairing and the anti-automorphism are *Adjoints of Bounded Sesquilinear Operators*; the sandwich is *The Bounded Sesquilinear Sandwich*; the Hermitian elements are *Hermitian and Skew-Hermitian Elements*; the normed $J^{*}$-triple and the $J^{*}$-algebra are *The Topological J\*-Algebra*. This article stops before the spectral theory of the later entries.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ with the continuous involution $\varsigma$, and $A$ is a normed sesqualgebra of *Banach Sesqualgebras*: the standard example $x\star y=xy^{*}$, submultiplicative norm, isometric involution, $\lVert1\rVert=1$. The bounded linear operators are $B(A)$ and the bounded $\varsigma$-semilinear ones $B^{\varsigma}(A)$, of *Bounded Operators on a Sesqualgebra*; the canonical pairing is $h(x,y)=x^{*}y$, and the operator families are

$$
\Theta_{x,y}(z)=xy^{*}z=\{x,y,z\},\qquad S_{a,b}(x)=ax^{*}b,\qquad L_{c}(x)=cx,\qquad T_{p,q}(x)=pxq .
$$

As in *Adjoints of Bounded Sesquilinear Operators*, the symbol $L_{c}$ is the **plain** left multiplication, the multiplication for the associative product; *The Bounded Left and Right Multiplication Operators of a Sesqualgebra* reserves $L_{c}$ for the multiplication $c\star x=cx^{*}$ by the derived product, which is $S_{c,1}$ here.

The adjoint of a bounded linear operator is defined by $h(Tx,y)=h(x,T^{\dagger}y)$ and that of a bounded conjugate-linear operator by the twisted rule $h(Sx,y)=h(x,S^{\dagger}y)^{*}$, both of *Adjoints of Bounded Sesquilinear Operators*, where the adjointable linear operators are characterised as the left multiplications.

## The Pair Operator and its Adjoint

### The Boundedness and the Factorisation

**Theorem (the pair operator is a bounded left multiplication).** For $x,y\in A$ the pair operator is linear in its variable and satisfies

$$
\Theta_{x,y}=T_{x\star y,1}=L_{x\star y},\qquad \lVert\Theta_{x,y}\rVert\le\lVert x\rVert\lVert y\rVert,\qquad \Theta_{x,y}(1)=x\star y,
$$

and the pair map $(x,y)\mapsto\Theta_{x,y}$ is linear in $x$ and $\varsigma$-semilinear in $y$.

**Proof.** The factorisation is *The Bounded Ternary Product*, $\Theta_{x,y}(z)=xy^{*}z=(x\star y)z=T_{x\star y,1}(z)$, which is the left multiplication by the derived product; the bound is the submultiplicative estimate $\lVert xy^{*}z\rVert\le\lVert x\rVert\lVert y\rVert\lVert z\rVert$ of that article, and the value at the unit is $xy^{*}=x\star y$. The parity of the pair map is the parity of the derived product, linear in the first factor and $\varsigma$-semilinear in the second. $\square$

**Remark.** The operator is $R$-linear in its variable, so its adjoint is taken by the plain rule and the parity obstruction of a conjugate-linear operator does not arise: the conjugate-linearity of the ternary product sits in the middle slot, which is a **parameter** of the operator and not its variable. A parameter may be conjugate-linear while the operator it names is linear, and the adjoint reads the operator and not the parameter.

### The Adjoint Swaps the Parameters

**Theorem (the adjoint of the pair operator).** For all $x,y\in A$,

$$
\Theta_{x,y}^{\dagger}=\Theta_{y,x},\qquad\text{equivalently}\qquad h\bigl(\Theta_{x,y}z,w\bigr)=h\bigl(z,\Theta_{y,x}w\bigr)\quad\text{for all }z,w\in A .
$$

**Proof.** The pair operator is the bounded left multiplication $L_{x\star y}$, and *Adjoints of Bounded Sesquilinear Operators* gives $L_{c}^{\dagger}=L_{c^{*}}$; here $c=x\star y$ and $c^{*}=(xy^{*})^{*}=yx^{*}=y\star x$, so $\Theta_{x,y}^{\dagger}=L_{(x\star y)^{*}}=L_{y\star x}=\Theta_{y,x}$. Written out, $h(\Theta_{x,y}z,w)=(xy^{*}z)^{*}w=z^{*}yx^{*}w$ and $h(z,\Theta_{y,x}w)=z^{*}(yx^{*}w)=z^{*}yx^{*}w$, which agree; this is the direct verification and it uses only the anti-multiplicativity of $*$ and the associativity. $\square$

**Corollary (the order of the operation).** $\Theta_{x,y}^{\dagger\dagger}=\Theta_{x,y}$ and $\Theta_{x,x}^{\dagger}=\Theta_{x,x}$: the diagonal of the pair map is self-adjoint.

**Proof.** The adjoint operation is of order two by *Adjoints of Bounded Sesquilinear Operators*, and the identity gives $\Theta_{x,x}^{\dagger}=\Theta_{x,x}$. $\square$

**Remark (the parities of the adjoint).** The adjoint $\Theta_{y,x}$ is, as a function of the pair, $\varsigma$-semilinear in $x$ and linear in $y$, because it is the pair map of the swapped pair. The adjoint operation therefore exchanges the two parities of the parameters, as in the algebraic layer, and in the factorisation the exchange is the star on the derived product, $c\mapsto c^{*}=y\star x$.

## The Diagonal and the Hermitian Criterion

### The Quadratic Representation is Self-Adjoint

**Theorem (the quadratic representation).** For every $x\in A$ the operator $\Theta_{x,x}$ is self-adjoint, and

$$
\Theta_{x,x}=L_{x\star x},\qquad \Theta_{x,x}^{\dagger}=L_{(x\star x)^{*}}=L_{x\star x}.
$$

**Proof.** The diagonal is self-adjoint by the corollary of the adjoint theorem, and the second identity is the same factorisation read on the adjoint; it agrees with the first because the derived square is Hermitian, $(x\star x)^{*}=(xx^{*})^{*}=xx^{*}=x\star x$. $\square$

**Remark.** The quadratic representation of the Jordan theory is the diagonal of the pair map, and the theorem says that it is self-adjoint for the canonical pairing whatever the involution and whatever the algebra. In the bilinear commutative case the operator is $U_{x}=\Theta_{x,x}=2T_{x,1}^{2}-T_{x^{2},1}$ of *The Ternary Product as an Operator*, and its self-adjointness is the classical one; the general theorem recovers it and gives it a norm.

### The Hermitian Criterion

**Theorem (when the pair operator is self-adjoint).** For $x,y\in A$,

$$
\Theta_{x,y}^{\dagger}=\Theta_{x,y}\quad\Longleftrightarrow\quad x\star y=y\star x\quad\Longleftrightarrow\quad (x\star y)^{*}=x\star y .
$$

The pair operator is therefore self-adjoint exactly when the derived product of the pair is Hermitian.

**Proof.** By the adjoint theorem $\Theta_{x,y}^{\dagger}=\Theta_{y,x}$, and the two are equal exactly when $y\star x=x\star y$, because the factorisation $\Theta_{p,q}=L_{p\star q}$ identifies the operator with its derived product and the left multiplication $L_{c}$ does not lose the element $c$, being injective with $L_{c}(1)=c$. Finally $y\star x=(xy^{*})^{*}=(x\star y)^{*}$, so the agreement is the Hermitian condition. $\square$

**Corollary (the Hermitian pairs).** Every diagonal operator is self-adjoint, and more generally $\Theta_{x,y}$ is self-adjoint for the pairs whose derived product is Hermitian, for instance $y=cx$ with $c$ a central Hermitian element, where $x\star y=xx^{*}c$ and $y\star x=cxx^{*}$ agree. The condition is not automatic: in $M_{n}(\mathbb{C})$ and $x=E_{11}$, $y=E_{21}$ the derived product is $x\star y=E_{11}E_{12}=E_{12}$, whose star is $E_{21}\neq E_{12}$, so $\Theta_{E_{11},E_{21}}^{\dagger}=\Theta_{E_{21},E_{11}}\neq\Theta_{E_{11},E_{21}}$, while the diagonal $\Theta_{E_{11},E_{11}}$ is self-adjoint.

**Proof.** The diagonal clause is the theorem above; for $y=cx$ with central Hermitian $c$ the two derived products are $x\star(cx)=xx^{*}c$ and $(cx)\star x=cxx^{*}=xx^{*}c$, equal. The matrix witness is the computation displayed. $\square$

## The Readings and the Reversal

### The Three Readings under the Adjoint

**Theorem (the readings and their adjoints).** For all $x,y,z\in A$,

$$
\Theta_{x,y}^{\dagger}=\Theta_{y,x},\qquad S_{x,z}^{\dagger}=S_{z,x},\qquad T_{x\star y,1}^{\dagger}=T_{(x\star y)^{*},1},
$$

the last two being read modulo the reduction of the pairing by a central functional, where they are the sandwich adjoint and the two-sided adjoint of Part I.

**Proof.** The first identity is the adjoint theorem. The second and the third are the adjoints of the sandwich and of the two-sided operator; for the canonical pairing they exist only after the reduction of *Adjoints of Bounded Sesquilinear Operators*, §*The Reduction to a Scalar Form*, and there they are $S_{b,a}$ and $T_{p^{*},q^{*}}$. With the factorisation $\Theta_{x,y}=T_{x\star y,1}$ the third reproduces the first. $\square$

**Corollary (no new adjoint).** The adjoint of the pair operator of $(x,y)$ is a pair operator again,

$$
\Theta_{x,y}^{\dagger}=T_{(x\star y)^{*},1}=L_{y\star x}=\Theta_{y,x},
$$

so the family of the pair operators is stable under the adjoint and the ternary product introduces no adjoint that the left multiplications had not already named.

**Remark.** The stability is a genuine closure statement: the adjoint of the conjugate left multiplication does not stay in the one-sided family, as *The Adjoint of the Bounded Conjugate Left Multiplication* records, while the adjoint of the pair operator stays in the family of the pairs. The reason is that the pair operator is a **plain** left multiplication by a derived product, and the plain left multiplications are exactly the adjointable linear operators of the canonical pairing; the pairs therefore inherit the closure that the derived one-sided operators do not have.

### The Reversal of the Triple

**Theorem (the reversed triple).** For all $x,y,z,w\in A$,

$$
h\bigl(\{x,y,z\},w\bigr)=h\bigl(z,\{y,x,w\}\bigr).
$$

The triple is reversible: the pairing of $\{x,y,z\}$ with $w$ equals the pairing of $z$ with the triple $\{y,x,w\}$, and this is the statement that the pair operator of $(x,y)$ has the pair operator of the reversed pair $(y,x)$ as its adjoint.

**Proof.** The identity is the adjoint theorem written with the ternary product: $h(xy^{*}z,w)=(xy^{*}z)^{*}w=z^{*}yx^{*}w=h(z,yx^{*}w)$. $\square$

**Remark.** The reversibility is the symmetry that the $J^{*}$-triples carry: the operator of a pair has the operator of the reversed pair as its adjoint, so the family of the pair operators is closed under the adjoint, and the first slot of the triple may be exchanged with the outside element against the pairing at the cost of swapping the two middle parameters. Read on the derived product, the reversal is $y\star x=(x\star y)^{*}$, and it is this identity that the self-adjointness criterion turns into a condition on the pair. The topological statement adds the bound: both sides of the reversal are bounded trilinear forms of norm at most one, so the identity is an identity of bounded operators, and the normed $J^{*}$-triple of *The Bounded Ternary Product* carries it in its axioms.

## The Degenerations

### The Trivial Base Involution

When $\varsigma=\mathrm{id}$ the twisted rule and the plain rule coincide, and the adjoint of the pair operator is still $\Theta_{y,x}$; nothing uses the non-triviality of $\varsigma$. The degenerate case is nevertheless the bilinear one: $\varsigma=\mathrm{id}$ forces the involution $*$ to be $\mathbb{K}$-linear, so the conjugate transpose is replaced by the transpose or another $\mathbb{K}$-linear anti-automorphism, and the derived product becomes $\mathbb{K}$-bilinear. The adjoint identity and the Hermitian criterion are unchanged in form, the canonical pairing becomes the symmetric product pairing, and the theorem reduces to the adjoint of $z\mapsto xy^{*}z$ being $z\mapsto yx^{*}z$.

### The Trivial Algebra Involution

The other degeneration is $*=\mathrm{id}$; the identity is an anti-automorphism only on a commutative algebra, so the algebra is commutative and the scalar rule then forces $\varsigma=\mathrm{id}$. Every element is Hermitian, the derived product is the ordinary product, and the pair operator is symmetric in its two parameters,

$$
\Theta_{x,y}(z)=xyz=yxz=\Theta_{y,x}(z),
$$

so every pair operator is self-adjoint, in agreement with the criterion, and the quadratic representation $U_{x}=\Theta_{x,x}=2T_{x,1}^{2}-T_{x^{2},1}$ is self-adjoint. The two degenerations meet in the commutative case, where the reversal of the triple is the commutativity of the product.

## Worked Cases

### The Complex Matrices

Let $A=M_{n}(\mathbb{C})$ with the conjugate transpose, the operator norm, $\tau=\operatorname{tr}$ and the reduced pairing $h_{\tau}(X,Y)=\operatorname{tr}(X^{*}Y)$, the canonical $A$-valued form being $h(X,Y)=X^{*}Y$. The pair operator of $(X,Y)$ is $\Theta_{X,Y}(Z)=XY^{*}Z$, its adjoint is $\Theta_{X,Y}^{\dagger}=\Theta_{Y,X}$, and the criterion reads

$$
\Theta_{X,Y}^{\dagger}=\Theta_{X,Y}\quad\Longleftrightarrow\quad XY^{*}=YX^{*},
$$

that is, the derived product is Hermitian. The diagonal $\Theta_{X,X}(Z)=XX^{*}Z$ is self-adjoint with $\lVert\Theta_{X,X}\rVert=\lVert X\rVert^{2}$, and its parameter $XX^{*}$ is positive; for $n=2$ and $X=E_{11}$ it is $Z\mapsto E_{11}Z$, self-adjoint, while the pair $(E_{11},E_{21})$ has the non-self-adjoint operator computed above.

### The Biquaternion Algebra

Let $A=\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the quaternionic conjugation of the basis with conjugated complex coefficients, so that $\varsigma$ is the complex conjugation and $*$ is an anti-automorphism with $1^{*}=1$; the algebra is $M_{2}(\mathbb{C})$ by *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, and the statements of the previous case transfer under that isomorphism. The pair operator of a pair has the operator of the swapped pair as its adjoint, the diagonal is self-adjoint, and the Hermitian criterion reads $x\star y=y\star x$ in the biquaternion algebra, the same condition as in $M_{2}(\mathbb{C})$ because the derived product and the involution are carried across by the isomorphism.

## Summary

The pair operator $\Theta_{x,y}(z)=xy^{*}z$ of the ternary product is the bounded left multiplication by the derived product, $\Theta_{x,y}=L_{x\star y}$, of norm at most $\lVert x\rVert\lVert y\rVert$; it is linear in its variable, and the conjugate-linearity of the ternary product sits in the middle parameter. Its adjoint for the canonical pairing is the pair operator of the swapped pair, $\Theta_{x,y}^{\dagger}=\Theta_{y,x}$, equivalently $h(\{x,y,z\},w)=h(z,\{y,x,w\})$, the reversal of the triple; the identity is the characterisation of the adjointable linear operators applied to the derived product, whose star is $y\star x=(x\star y)^{*}$. The diagonal $\Theta_{x,x}$ is self-adjoint for every element, which is the self-adjointness of the quadratic representation of the Jordan theory, and the pair operator is self-adjoint exactly when its derived product is Hermitian; the criterion is not automatic, the pair $(E_{11},E_{21})$ of $M_{2}(\mathbb{C})$ being the smallest witness. The adjoint permutes the readings of the ternary product and leaves the family of the pair operators stable, because the pair operators are the plain left multiplications, exactly the adjointable linear operators of the canonical pairing; the sandwich and the two-sided adjoints are those of the reduced form. In the two degenerations the article reduces to the bilinear case and to the commutative case, where every pair operator is self-adjoint.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Theta_{x,y}(z)=xy^{*}z=\{x,y,z\}$ | the pair operator, a bounded left multiplication $L_{x\star y}$ |
| $\lVert\Theta_{x,y}\rVert\le\lVert x\rVert\lVert y\rVert$ | the trilinear bound, from *The Bounded Ternary Product* |
| $\Theta_{x,y}=T_{x\star y,1}=L_{x\star y}$ | the factorisation through the derived product |
| $\Theta_{x,y}^{\dagger}=\Theta_{y,x}$ | the adjoint swaps the two parameters |
| $h(\{x,y,z\},w)=h(z,\{y,x,w\})$ | the reversal of the triple |
| $\Theta_{x,x}^{\dagger}=\Theta_{x,x}=L_{x\star x}$ | the diagonal is self-adjoint: the quadratic representation |
| $\Theta_{x,y}^{\dagger}=\Theta_{x,y}\iff(x\star y)^{*}=x\star y$ | the Hermitian criterion |
| $L_{c}^{\dagger}=L_{c^{*}}$ | the adjoint of a left multiplication, the engine of the article |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, American Mathematical Society Colloquium Publications 39 (1968), for the quadratic representation, its self-adjointness and the Jordan triple systems.
- Ottmar Loos, *Jordan Pairs* (Lecture Notes in Mathematics 460, Springer, 1975), for the triple products, their adjoints and the reversibility, the abstract form of the central identity.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (CBMS Regional Conference Series 67, American Mathematical Society, 1987), for the $J^{*}$-algebras, the triple product $xy^{*}z$ and the adjoint of its operator.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge Tracts in Mathematics 190, Cambridge University Press, 2012), for the Jordan triples with an involution and the reversibility of the triple, with the analysis of the norm.
- Yaakov Friedman and Bernard Russo, "The Gelfand–Naimark theorem for $JB^{*}$-triples", *Duke Mathematical Journal* 53 (1986), for the $J^{*}$-triples and the axioms in which the reversal of the triple appears as the symmetry of the triple product.
