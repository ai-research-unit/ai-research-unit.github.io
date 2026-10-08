# __The Bounded Sesquilinear Commutator__

## Introduction

The sesquilinear product carries a second product, its transpose $y \star x$, and the difference of the two is the bracket $[x,y]_{\varsigma} = x \star y - y \star x$. This article reads the bracket of *The Sesquilinear Commutator* with a topology on the module. It shows that the bracket is a bounded sesquilinear map, with $\lVert[x,y]_{\varsigma}\rVert \leq 2\lVert x\rVert\lVert y\rVert$, that its values lie in the closed subspace of the skew-Hermitian elements, so that it is a continuous map $A \times A \to S(A)$, and that on the skew-Hermitian elements it is the negative of the commutator of the associative envelope, so that the skew-Hermitian part is a real Banach Lie algebra and the topological form of the Lie-admissibility of the sesqualgebra is a statement about a closed subspace of a Banach space.

Three facts organise the article. The bracket is antisymmetric by definition but not $\mathbb{K}$-bilinear: the scalar rule carries a correction term $(\lambda - \varsigma(\lambda))(y \star x)$, so the bracket is continuous as a sesquilinear map and only over the fixed field $\mathbb{R}$ is it bilinear, and this is the topological content of the correction term, a difference that is invisible when only the norm is read. The bracket takes its values in the skew-Hermitian part for every pair of arguments, so the sesquilinear form factors through the closed subspace $S(A)$, and on that subspace the twist disappears: the bracket is the negative of the commutator, the commutator makes $S(A)$ a Banach Lie algebra, and the bracket makes it the same Lie algebra with all signs reversed. And the bracket is not a Lie bracket on all of $A$: the Jacobi identity fails, with a finite-dimensional witness, and it holds on $S(A)$ and on the sesquilinear field, so the failure is produced by the noncommutativity of the envelope and not by the twist.

The article defines the bracket and its norm, treats the scalar rule and the failure of bilinearity, proves the values and the two halves with their bounds, reads the bracket as a pair of bounded multiplications and as a bounded operator on the tensor product, and works the examples. The algebraic bracket, its correction term, the failure of the Jacobi identity and the two halves are *The Sesquilinear Commutator*; the Lie-admissibility and the collapse are *Lie Algebras of Sesqualgebras*; the two halves as a Jordan and a Lie algebra are *Hermitian and Skew-Hermitian Elements*; the bounded multiplications are *The Bounded Left and Right Multiplication Operators of a Sesqualgebra*; the tensor product is *Topological Tensor Products of Sesqualgebras*. Throughout $(\mathbb{K},\varsigma)$ is $\mathbb{R}$ or $\mathbb{C}$ with its continuous involution, $A$ is the standard example of the layer, an associative algebra with a submultiplicative norm and an isometric involution carrying the derived product $x \star y = xy^{*}$, complete where a Banach statement is made, and $2$ is invertible in $\mathbb{K}$.

## The Bracket and its Norm

### The Definition

**Definition.** The **sesquilinear commutator**, or the **bracket**, of $x,y \in A$ is

$$
[x,y]_{\varsigma} = x \star y - y \star x .
$$

It is the difference of the product and its transpose, the antisymmetric half of the split of the product whose symmetric half is the symmetrised product of *The Sesquilinear Symmetrised Product*.

**Proposition (additivity and the two parities).** The bracket is additive in each variable, $\mathbb{K}$-linear in the first and $\varsigma$-semilinear in the second, so it is an $R^{\varsigma}$-bilinear map $A \times A \to A$; it is antisymmetric, $[y,x]_{\varsigma} = -[x,y]_{\varsigma}$ and $[x,x]_{\varsigma} = 0$.

*Proof.* The additivity is that of the product; the parities are the two scalar rules of the layer read on the difference, and they are computed in *The Sesquilinear Commutator*, §*The Scalars and the Correction Term*; the antisymmetry is the antisymmetry of the subtraction. $\square$

### The Boundedness

**Theorem (the bracket is bounded).** Let $A$ be a normed sesqualgebra with submultiplicative norm. Then for all $x,y$,

$$
\lVert[x,y]_{\varsigma}\rVert \leq 2\lVert x\rVert\lVert y\rVert ,
$$

so the bracket is a bounded sesquilinear map, and its sesquilinear norm $\lVert[\ ,\ ]_{\varsigma}\rVert = \sup\{\lVert[x,y]_{\varsigma}\rVert : \lVert x\rVert \leq 1,\ \lVert y\rVert \leq 1\}$ satisfies $\lVert[\ ,\ ]_{\varsigma}\rVert \leq 2$. It is continuous as a map $A \times A \to A$ for the product topology.

*Proof.* $\lVert x \star y\rVert \leq \lVert x\rVert\lVert y\rVert$ and $\lVert y \star x\rVert \leq \lVert y\rVert\lVert x\rVert$ by the submultiplicative estimate, so the triangle inequality gives $\lVert[x,y]_{\varsigma}\rVert \leq 2\lVert x\rVert\lVert y\rVert$. A sesquilinear map bounded by a constant is continuous, and the continuity of the sesquilinear form in each variable follows from the bound and additivity. $\square$

**Corollary (the factorisation through the tensor product).** The bracket factors as

$$
A \times A \xrightarrow{\ \ } A \otimes A \xrightarrow{\ C\ } A , \qquad C(x \otimes y) = x \star y - y \star x ,
$$

and the linear map $C$ is bounded for the projective norm with $\lVert C\rVert \leq 2$; its completion is a bounded operator $\widehat{C} : A \widehat{\otimes}_{\pi} A \to A$, the **commutator operator** of the sesqualgebra.

*Proof.* The bracket is bilinear on the pair $A \times A^{\varsigma}$ in the sense of *The Sesquilinear Product*, §*The Product as a Bilinear Map on the Pair*, so it factors through the tensor product by the universal property; the norm bound is the theorem, and the extension to the completion is the bounded linear extension of *The Completion of a Sesqualgebra*, §*The Product on the Completion*. $\square$

### The Failure of Bilinearity and the Corrected Identities

**Theorem (the scalar rule and the correction term).** For all $\lambda \in \mathbb{K}$ and all $x,y$,

$$
[\lambda x,y]_{\varsigma} = \lambda\,(x \star y) - \varsigma(\lambda)\,(y \star x) , \qquad [x,\lambda y]_{\varsigma} = \varsigma(\lambda)\,(x \star y) - \lambda\,(y \star x) ,
$$

so that

$$
[\lambda x,y]_{\varsigma} - \lambda[x,y]_{\varsigma} = \bigl(\lambda - \varsigma(\lambda)\bigr)(y \star x) , \qquad [x,\lambda y]_{\varsigma} - \varsigma(\lambda)[x,y]_{\varsigma} = \bigl(\varsigma(\lambda) - \lambda\bigr)(x \star y) ,
$$

and the bracket is $\mathbb{K}$-bilinear exactly when $\varsigma = \mathrm{id}$ or the product vanishes identically.

*Proof.* The two displays are the theorem of *The Sesquilinear Commutator*, §*The Scalars and the Correction Term*; the topological content is that the correction term is not bounded by a multiple of $\lVert x\rVert\lVert y\rVert$ with a constant independent of $\lambda$, so no estimate repairs the loss of bilinearity. The bracket is nevertheless bounded as a sesquilinear map and it is bilinear over $\mathbb{R}$, the scalar rule of a real scalar being free of the correction term. $\square$

**Corollary (the real structure).** Over $\mathbb{R}$ the correction term vanishes, $(\lambda - \varsigma(\lambda)) = 0$ for real $\lambda$, so the bracket is $\mathbb{R}$-bilinear and continuous; the bounded sesquilinear form of this article restricts to a bounded real-bilinear form, and the failure of $\mathbb{K}$-bilinearity is exactly the correction term on the imaginary scalars.

*Proof.* $\varsigma$ fixes $\mathbb{R}$, so $\lambda - \varsigma(\lambda) = 0$ for real $\lambda$. The rest is the theorem. $\square$

## The Values in the Skew-Hermitian Part

### The Values and the Closed Subspace

**Theorem (the values are skew-Hermitian).** For all $x,y$,

$$
[x,y]_{\varsigma}^{*} = -[x,y]_{\varsigma} ,
$$

so $[A,A]_{\varsigma} \subseteq S(A)$, where $S(A) = \{s : s^{*} = -s\}$ is the skew-Hermitian part. The set $S(A)$ is a closed real subspace of $A$, and the bracket is a bounded sesquilinear map $A \times A \to S(A)$.

*Proof.* The conjugation of a product reverses it, $(x \star y)^{*} = y \star x$, so $[x,y]_{\varsigma}^{*} = y \star x - x \star y = -[x,y]_{\varsigma}$; this is *The Sesquilinear Commutator*, §*The Values in the Skew-Hermitian Part*. The skew-Hermitian part is the kernel of the continuous map $x \mapsto x^{*} + x$, hence closed, and it is a real subspace because $is$ is Hermitian when $s$ is skew-Hermitian. The bracket lands in it by the first display, and it is bounded by §*The Boundedness*. $\square$

**Remark.** The bracket is therefore never a map into the Hermitian part unless it vanishes, and the topological statement is stronger than the algebraic one in one respect: it says that the bracket is a bounded map into a closed subspace, so a limit of brackets is a bracket only in the sense of the closure, and the closure is automatic because $S(A)$ is closed. The Hermitian part $H(A)$ is likewise closed, and it is the image of the idempotent $x \mapsto \tfrac12(x + x^{*})$ along with $S(A)$, which is the topological form of the decomposition of *Hermitian and Skew-Hermitian Elements*, §*The Decomposition*.

### The Two Halves

**Theorem (the bracket on the two halves).** For $h,h' \in H(A)$ and $s,s' \in S(A)$,

$$
[h,h']_{\varsigma} = [h,h'] , \qquad [s,s']_{\varsigma} = -[s,s'] , \qquad [s,h]_{\varsigma} = sh + hs ,
$$

where $[h,h'] = hh' - h'h$ is the commutator of the envelope; each identity is an identity of bounded operators, and the bounds are $\lVert[h,h']_{\varsigma}\rVert \leq 2\lVert h\rVert\lVert h'\rVert$ and so on.

*Proof.* The identities are the theorem of *The Sesquilinear Commutator*, §*The Two Halves*, and the bounds are those of §*The Boundedness* with the submultiplicative estimate. $\square$

## The Lie Algebra of the Bounded Skew-Hermitian Elements

### The Banach Lie Algebra

**Theorem (the skew-Hermitian part is a real Banach Lie algebra).** Let $A$ be a Banach sesqualgebra. Then $S(A)$ is a real Banach space, the commutator $[s,s'] = ss' - s's$ is a bounded real-bilinear map $S(A) \times S(A) \to S(A)$ with $\lVert[s,s']\rVert \leq 2\lVert s\rVert\lVert s'\rVert$, and it satisfies the Jacobi identity; the sesquilinear bracket is its negative,

$$
[s,s']_{\varsigma} = -[s,s'] ,
$$

so $S(A)$ is a real Banach Lie algebra under either bracket, the two brackets being isomorphic by the negation. The Hermitian part $H(A)$ is not a Lie algebra under the sesquilinear bracket, since the bracket of two Hermitian elements is skew-Hermitian.

*Proof.* The skew-Hermitian part is closed by §*The Values and the Closed Subspace*, hence complete because $A$ is; it is a real vector space because $is \in H(A)$ for $s \in S(A)$. If $s,s' \in S(A)$ then $(ss')^{*} = (s')^{*}s^{*} = (-s')(-s) = s's$, so $(ss' - s's)^{*} = s's - ss' = -[s,s']$, and the commutator is closed in $S(A)$; the Jacobi identity is the associativity of the envelope, by the derivation form $[s,[s',s'']] = [[s,s'],s''] + [s',[s,s'']]$; the bound is the submultiplicative estimate. The identity $[s,s']_{\varsigma} = -[s,s']$ is the middle identity of the theorem above, and negation is an isomorphism of brackets because $[s,s']_{\varsigma} = -\mathrm{id}\circ[s,s']\circ(\mathrm{id}\times\mathrm{id})$. For the last statement, $[h,h']_{\varsigma} = [h,h']$ with $h,h'$ Hermitian and $[h,h']$ skew-Hermitian, so the bracket leaves $H(A)$. $\square$

**Corollary (the Lie structure of the layer).** The Lie algebra that a sesqualgebra carries is the real Banach Lie algebra $S(A)$; the Hermitian part carries instead the symmetrised product, under which it is a Jordan algebra, by *Hermitian and Skew-Hermitian Elements*, §*The Hermitian Part is a Jordan Algebra*, and the passage between the two is the decomposition $A = H(A) \oplus S(A)$.

*Proof.* The statement about $S(A)$ is the theorem; the statement about $H(A)$ is the cited result, and the decomposition is the topological form of the algebraic decomposition into fixed and anti-fixed points of the involution. $\square$

### The Failure of the Jacobi Identity and the Operator Reading

**Theorem (the bracket is not a Lie bracket on $A$).** The Jacobi identity for the sesquilinear bracket fails on $A$; in $M_{2}(\mathbb{C})$ the elements $E_{11}, E_{22}, E_{12}$ give a nonzero Jacobi sum, and three Hermitian elements already fail. It holds on $S(A)$ by the theorem above and it holds identically on the sesquilinear field, so the failure is produced by the noncommutativity of the envelope and not by the twist.

*Proof.* The witness and the field computation are those of *The Sesquilinear Commutator*, §*The Failure of the Jacobi Identity*; the two positive cases are the theorem above and the cited field computation. $\square$

**Proposition (the bracket as a difference of two multiplications).** For all $x,y$,

$$
[x,y]_{\varsigma} = L_x(y) - R_x(y) = R_y(x) - L_y(x) ,
$$

so the bracket is the difference of the left and the right multiplication, and with $x$ fixed it is the adjoint action $\operatorname{ad}_x = L_x - R_x$ of *The Bounded Left and Right Multiplication Operators of a Sesqualgebra*, §*The Adjoint Action*; it is bounded with $\lVert \operatorname{ad}_x\rVert \leq 2\lVert x\rVert$, and it is the sum of an even and an odd bounded operator.

*Proof.* $x \star y = L_x(y)$ and $y \star x = R_x(y)$ by the definitions of the two multiplications; the second form is the first with the variables exchanged and the antisymmetry used. The bound and the parity statement are those of the adjoint action. $\square$

**Remark.** The proposition is the reason the bracket operator belongs to the graded operator algebra of *Bounded Operators on a Sesqualgebra*: it is not a homogeneous operator but a sum of the odd left multiplication and the even right multiplication, and its norm is bounded by the sum of the two norms. This is the operator form of the statement that the sesquilinear bracket is not $\mathbb{K}$-bilinear, and the two statements are the same fact read in the two languages.

## The Comparison with the Bilinear Layer

**Proposition (the commutator at the trivial involution).** Let $A$ be the standard example with $\varsigma = \mathrm{id}$, so that the product is bilinear, and suppose in addition that the involution is trivial, $* = \mathrm{id}$. Then $A$ is commutative — the identity involution satisfies $(xy)^{*} = y^{*}x^{*}$, that is $xy = yx$ — the product is the ordinary one, and the bracket vanishes identically, $[x,y]_{\varsigma} = xy - yx = 0$; the skew-Hermitian part is $S(A) = \{0\}$ while $H(A) = A$, and the Banach Lie algebra $S(A)$ of the sesquilinear layer degenerates to the zero Lie algebra.

*Proof.* A trivial involution satisfies $(xy)^{*} = y^{*}x^{*}$ with $* = \mathrm{id}$ on both sides, so $xy = yx$; then the derived operation is the ordinary product and the bracket is the ordinary commutator of a commutative algebra, which vanishes. With $* = \mathrm{id}$ the condition $s^{*} = -s$ reads $s = -s$, so $S(A) = \{0\}$ because $2$ is invertible, and every element is Hermitian. $\square$

**Remark.** The comparison with the bilinear layer is therefore not one of an operator but of an algebra: the sesquilinear bracket is bounded, antisymmetric, $\mathbb{R}$-bilinear and skew-Hermitian-valued, and it is a Lie bracket only on the skew-Hermitian part; the ordinary commutator that *The Commutator Operator* studies is the bilinear antisymmetrisation of an arbitrary algebra, and it is recovered from the sesquilinear bracket only at the trivial involution, where the identity involution forces the algebra to be commutative and the bracket to vanish, in agreement with the vanishing criterion of *The Sesquilinear Commutator*, §*The Vanishing and the Involution*. The one place where the two layers agree in full, with no degeneration of the product, is the skew-Hermitian part, which is the reason the Lie theory of the sesqualgebra is developed there, in *Lie Algebras of Sesqualgebras* and *The Unitary Lie Algebra*.

## Examples

### The Matrices

**Example (the matrices, verdict: the bracket of the skew-Hermitian matrices is the unitary Lie algebra).** Let $A = M_{n}(\mathbb{C})$ with the operator norm, the conjugation and the product $X \star Y = XY^{*}$. The bracket is $[X,Y]_{\varsigma} = XY^{*} - YX^{*}$, bounded with $\lVert[X,Y]_{\varsigma}\rVert \leq 2\lVert X\rVert\lVert Y\rVert$, with values in the skew-Hermitian matrices $S(A) = \mathfrak{u}(n)$. On $S(A)$ the bracket is the negative of the commutator, so $S(A)$ is the real Banach Lie algebra $\mathfrak{u}(n)$ with all signs reversed; the Jacobi identity fails on the Hermitian matrices, the Hermitian triple $E_{11}, E_{22}, E_{12} + E_{21}$ of *The Sesquilinear Commutator*, §*The Failure of the Jacobi Identity* producing the nonzero sum.

### The Field

**Example (the field, verdict: a one-dimensional abelian Lie algebra).** Let $A = \mathbb{C}$ with the modulus, the conjugation and the product $x \star y = x\bar y$. The bracket is $[x,y]_{\varsigma} = 2i\,\mathrm{Im}(x\bar y)$, bounded with $\lvert[x,y]_{\varsigma}\rvert \leq 2\lvert x\rvert\lvert y\rvert$ and with values in the purely imaginary numbers $S(A) = i\mathbb{R}$. On $S(A)$ the commutator vanishes because the field is commutative, so the real Banach Lie algebra of the skew-Hermitian elements is abelian, and the Jacobi identity holds on all of $\mathbb{C}$ by the telescoping computation of *The Sesquilinear Commutator*, §*The Field*.

### The Sequences

**Example (the sequences, verdict: the bracket inherits the $\ell^{1}$ bound).** Let $A = \ell^{1}$ with the norm, the termwise conjugation and the termwise product. The bracket is the termwise bracket, $\lVert[x,y]_{\varsigma}\rVert_{1} \leq 2\lVert x\rVert_{1}\lVert y\rVert_{1}$, and the skew-Hermitian part is the closed real subspace of the sequences with purely imaginary terms, which is a real Banach Lie algebra under the termwise commutator, abelian because the termwise product is commutative.

## Summary

The sesquilinear commutator $[x,y]_{\varsigma} = x \star y - y \star x$ is a bounded sesquilinear map with $\lVert[x,y]_{\varsigma}\rVert \leq 2\lVert x\rVert\lVert y\rVert$, continuous on $A \times A$ and factoring through a bounded operator $\widehat{C} : A \widehat{\otimes}_{\pi} A \to A$ of norm at most two. It is antisymmetric but not $\mathbb{K}$-bilinear: the scalar rule carries the correction term $(\lambda - \varsigma(\lambda))(y \star x)$ and it is bilinear only over $\mathbb{R}$, so the bounded sesquilinear form is the complexification of a bounded real-bilinear one. Its values lie in the skew-Hermitian part for every pair, $[A,A]_{\varsigma} \subseteq S(A)$, and $S(A)$ is closed, so the bracket is a continuous map into a closed subspace and the Hermitian part is never met unless the bracket vanishes.

On the two halves the bracket is the ordinary commutator on $H(A)$, its negative on $S(A)$ and the symmetrised product across the two. On the skew-Hermitian part the bracket is the negative of the commutator of the envelope, so $S(A)$ is a real Banach Lie algebra under either bracket, isomorphic to itself under negation, while $H(A)$ is a Jordan algebra under the symmetrised product and no Lie algebra under the bracket. The Jacobi identity fails on all of $A$, with the finite-dimensional witness and with three Hermitian elements, and it holds on $S(A)$ and on the sesquilinear field, so the failure is produced by the noncommutativity of the envelope. The bracket is the difference of the two bounded multiplications, $[x,y]_{\varsigma} = L_x(y) - R_x(y)$, with $x$ fixed the adjoint action $\operatorname{ad}_x$ of norm at most $2\lVert x\rVert$ and the sum of an even and an odd bounded operator in the graded algebra; at the trivial involution the identity involution forces the algebra to be commutative and the bracket vanishes, in agreement with the vanishing criterion of *The Sesquilinear Commutator*, §*The Vanishing and the Involution*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $[x,y]_{\varsigma} = x \star y - y \star x$ | the sesquilinear commutator |
| $\lVert[x,y]_{\varsigma}\rVert \leq 2\lVert x\rVert\lVert y\rVert$ | the bound of the bracket |
| $\widehat{C} : A \widehat{\otimes}_{\pi} A \to A$ | the bounded commutator operator on the projective tensor product |
| $(\lambda - \varsigma(\lambda))(y \star x)$ | the correction term of the scalar rule |
| $[A,A]_{\varsigma} \subseteq S(A)$ | the values of the bracket in the skew-Hermitian part |
| $S(A) = \{s : s^{*} = -s\}$ | the closed real subspace of the skew-Hermitian elements |
| $H(A) = \{h : h^{*} = h\}$ | the closed real subspace of the Hermitian elements |
| $[s,s']_{\varsigma} = -[s,s']$ | the bracket on the skew-Hermitian part |
| $[h,h']_{\varsigma} = [h,h']$ | the bracket on the Hermitian part |
| $[s,h]_{\varsigma} = sh + hs$ | the bracket across the two halves |
| $\mathfrak{u}(n)$ | the Lie algebra of the skew-Hermitian matrices |
| $[x,y]_{\varsigma} = L_x(y) - R_x(y)$ | the bracket as a difference of two multiplications |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the commutator of an involutive algebra and the Lie algebra of its skew-Hermitian elements.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume I* (Cambridge University Press, 1994), for the continuity of the commutator and the Banach Lie algebras attached to a Banach algebra with an involution.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the Lie algebras of skew elements and the Jacobi identity in an associative envelope.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the two halves of a ring with involution and the operations they carry.
- The companion articles of this series: *The Sesquilinear Commutator*, *Lie Algebras of Sesqualgebras*, *Hermitian and Skew-Hermitian Elements*, *The Bounded Left and Right Multiplication Operators of a Sesqualgebra* and *The Bounded Ternary Product*.
