# __The Indefinite Case and the Signature__

## Introduction

Positivity has two branches. The first is the definite one, where the diagonal has a sign and its square root is a **norm**: that branch is *The Norm Defined by a Form*. The second is the **indefinite** one, where the diagonal takes both signs, and it is not an analysis but an arithmetic: there is no norm, there can be nonzero elements of zero diagonal, the tolerance of *Positivity and the Positive Cone of a Hermitian Form*, §*The Tolerance* is not transitive, and what survives is the **signature** of the form, the two ranks that no change of basis destroys, and the orthogonal decomposition of the module into a positive and a negative definite part whose ranks are fixed although the parts are not.

The indefinite case is the complement of the two semi-definite classes, and it is read from the diagonal alone, exactly as the definite case is; the difference is that the diagonal now has both signs and the discriminant argument of the definite theory, whose leading coefficient had to be positive, is no longer available. The invariants are the ones of the scalar form: the **inertia index** $(p,q,z)$ of the ranks of positivity, of negativity and of the radical, Sylvester's law of inertia saying that the two first are independent of the decomposition, the **signature** $(p,q)$ in the nondegenerate case, and the **Pontryagin index** $\kappa = \min(p,q)$, the rank of the smaller of the two parts.

Two facts separate the sesquilinear indefinite case from the bilinear one, and both are consequences of the form sitting on an algebra. First, **the decomposition is a decomposition of the module and not of the algebra**: the positive and the negative parts are subspaces selected by the form and not subalgebras, and the product does not preserve them; on $M_{2}(\mathbb{C})$ with the form $\operatorname{tr}(XGY^{*})$ of the indefinite model the element $E_{21}$ is positive and its square is zero, so the positive part is not closed under multiplication. Second, **the compatibility survives the loss of definiteness only as the adjoint-pair identity**: the left multiplication by $x$ and the left multiplication by $x^{*}$ remain paired by the form, the radical remains a left ideal whose image under the involution is a right ideal, and no positivity of the pairing is left to read the algebra through the form.

The article defines the indefinite case and the neutral elements, computes the inertia through the Gram matrix and proves Sylvester's law, treats the positive and the negative parts and their failure to be subalgebras, records the two objects that replace the norm, classifies the forms over the field cases, and names the boundary with the Krein space. Positivity is *Positivity and the Positive Cone of a Hermitian Form*, the definite branch and its norm are *The Norm Defined by a Form*, the symmetry that turns an indefinite form into a definite one is *The Fundamental Symmetry of the Form*, the operators preserving the form are *Unitary and Isometric Operators of the Form*, the adjoint is *The Adjoint under a Hermitian Form*, the scalar form, its radical and the compatibility are *Topological Sesqualgebras with a Form*, the algebraic theory of the form is *Hermitian Forms on a Sesqualgebra*, the classification of Hermitian forms over a ring with involution is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and the diagonalisation and the inertia law of the scalar theory are *Quadratic Forms and Polarisation* and *Bilinear Forms*. The complete indefinite spaces belong to the bilinear layer, to *Indefinite Inner Product Spaces*, *Krein Spaces* and *Pontryagin Spaces*, and are named and deferred. Throughout, $R$ is a field with an involution $\varsigma$ whose fixed field $k = R^{\varsigma}$ is ordered and in which every nonnegative element is a square, so that signs and square roots of the diagonal are read in $k$; the model is $R = \mathbb{R}$ with $\varsigma = \mathrm{id}$ and $R = \mathbb{C}$ with the conjugation. The algebra $A$ is a topological sesqualgebra with a form in the sense of the entry, with Hermitian form $h$ compatible with the product, involution $*$ and derived operation $x \star y = xy^{*}$, the form is nondegenerate unless a statement says otherwise, and $A$ is a free module of finite rank over $R$ whenever a Gram matrix is used.

## The Indefinite Case

### The Sign of the Diagonal

**Definition.** The form $h$ is **indefinite** when it is neither positive semi-definite nor negative semi-definite, that is when there are $x, y \in A$ with $h(x,x) > 0$ and $h(y,y) < 0$; the four kinds and their signs are *Positivity and the Positive Cone of a Hermitian Form*, §*The Four Kinds*. For an indefinite form the **positive set** $P(h) = \{x : h(x,x) \geq 0\}$ and the **null set** $N(h) = \{x : h(x,x) = 0\}$ are proper subsets of $A$ containing $0$, and the elements of $N(h)$ are the **neutral** or **isotropic** elements of the form.

**Proposition (the null set is not the radical).** For an indefinite form the null set is properly larger than the radical: $A^{\perp} \subseteq N(h)$ with $A^{\perp} \neq N(h)$ in general.

*Proof.* An element of the radical satisfies $h(x,y) = 0$ for every $y$, in particular $h(x,x) = 0$, so $A^{\perp} \subseteq N(h)$; that the inclusion can be proper is the example below. $\square$

**Example (the hyperbolic plane).** Let $A = \mathbb{R}^{2}$ with the pointwise product, the trivial involution $\varsigma = \mathrm{id}$ and $* = \mathrm{id}$, and let

$$
h(u,v) = u_{1}v_{1} - u_{2}v_{2} .
$$

The form is symmetric, bilinear and compatible, since both sides of $h(uv,w) = h(v,uw)$ are $u_{1}v_{1}w_{1} - u_{2}v_{2}w_{2}$, and it is nondegenerate, its Gram matrix in the standard basis being $\operatorname{diag}(1,-1)$. The vectors $e_{1}$ and $e_{2}$ are positive and negative, the vectors $e_{1} \pm e_{2}$ are neutral, and the null set is the union of the two lines they span, while the radical is zero: the inclusion of the proposition is proper. The example is the collapsed, bilinear model of the indefinite layer, and the two neutral lines are the cheapest picture of the failure of a definite geometry.

**Remark (indefinite and isotropic are not the same).** An indefinite form need not have a nonzero neutral element. Over $\mathbb{Q}$ the form $q(u) = u_{1}^{2} - 2u_{2}^{2}$ is indefinite, since $q(1,0) = 1 > 0$ and $q(0,1) = -2 < 0$, and it is **anisotropic**: $u_{1}^{2} = 2u_{2}^{2}$ with $u \neq 0$ has no rational solution. The signature is read from the signs of the diagonal values and not from the existence of isotropic elements, and the two notions coincide only over a base in which the relevant square roots exist, as over $\mathbb{R}$.

### The Failure of the Tolerance

**Remark (the tolerance is not transitive).** The relation $x \succeq y$ when $h(x-y,x-y) \geq 0$ of *Positivity and the Positive Cone of a Hermitian Form*, §*The Tolerance* is transitive exactly for the semi-definite forms; for an indefinite form it is a tolerance and not an order. In the hyperbolic plane $(2,1) \succeq (0,0)$ and $(0,0) \succeq (2,-1)$, since $h((2,1),(2,1)) = 3$ and $h((-2,1),(-2,1)) = 3$, while $(2,1) \nsucceq (2,-1)$, since $h((0,2),(0,2)) = -4$. The witness is the same as the one of the scalar theory, the pair $(h,\succeq)$ being the scalar form of the hyperbolic plane, and it is the reason the order of the layer is on the Hermitian elements and the positive functionals and not on the module.

## The Inertia

### The Gram Matrix and the Inertia Index

**Definition.** Let $e_{1}, \ldots, e_{n}$ be a basis of $A$ over $R$. The **Gram matrix** of $h$ is the matrix $H$ with entries $H_{ij} = h(e_{i}, e_{j})$; it is Hermitian for $\varsigma$, $H^{T} = \varsigma(H)$, and the form is nondegenerate exactly when $H$ is invertible, the criterion of *Topological Sesqualgebras with a Form*, §*Full Type and Nondegeneracy*. The **congruence** by an invertible matrix $P$ is the change $H \mapsto P^{*}HP$, the Gram matrix of the same form in the basis with matrix $P$.

**Definition.** The **inertia index** of a Hermitian form on a finite-dimensional module is the triple $(p,q,z)$ of the **ranks of positivity and of negativity** and the dimension of the radical, the triple of *Indefinite Inner Product Spaces*, §*Inertia and the Signature*,

$$
p = \max\{\dim W : W \text{ positive definite}\}, \qquad q = \max\{\dim W : W \text{ negative definite}\}, \qquad z = \dim A^{\perp} ,
$$

and in the nondegenerate case the **signature** is the pair $(p,q)$, with $p + q = n$; the **Pontryagin index** is $\kappa = \min(p,q)$, the rank of the smaller of the two parts. It is not the **rank of negativity** of *Pontryagin Spaces*, the dimension of the negative part, which that article calls the index of $\Pi_{\kappa}$: the two numbers agree exactly when the negative part is the smaller, $q \leq p$, and they differ in the biquaternion instance, where the general quaternionic sesquilinear form of signature $(2,6)$ of *The Four Pairings of the Biquaternion Algebra* makes the Pontryagin space $\Pi_{6}$ of *The Krein Gram Matrix and the Restrictions of the Form*, of positive part of dimension $2$ and negative part of dimension $6$, whose Pontryagin index is $2$.

**Proposition.** $p + q + z = n$, and the four kinds are read off the ranks: the form is positive semi-definite exactly when $q = 0$ and positive definite exactly when in addition $z = 0$, symmetrically with $p$ and $q$ exchanged, so that it is semi-definite exactly when $pq = 0$ and indefinite exactly when $pq > 0$.

*Proof.* The decomposition theorem of §*Sylvester's Law* gives the orthogonal direct sum $A = A_{+} \oplus A_{-} \oplus A^{\perp}$ with $A_{+}$ positive definite and $A_{-}$ negative definite, so the three dimensions add to $n$ and $\dim A^{\perp} = z$. The projection argument of that section, applied to an arbitrary positive definite subspace $W$ in place of $A'_{+}$, bounds $\dim W \leq \dim A_{+}$, so the maximum that defines $p$ is $\dim A_{+}$, and the symmetric argument gives $q = \dim A_{-}$; hence $p + q + z = n$. The kinds are then read off the same decomposition: $q = 0$ means $A_{-} = 0$, that is $A = A_{+} \oplus A^{\perp}$ with $h(x,x) \geq 0$ for every $x$, which is positive semi-definiteness, and the form is positive definite when in addition $z = 0$, since then $A$ itself is the positive definite part; exchanging the two parts gives the negative pair, and with them semi-definiteness at $pq = 0$ and indefiniteness at $pq > 0$, the four kinds being those of *Positivity and the Positive Cone of a Hermitian Form*, §*The Four Kinds*. $\square$

### Sylvester's Law

**Theorem (the decomposition).** Let $h$ be a Hermitian form on a finite-dimensional module. Then $A$ is the orthogonal direct sum

$$
A = A_{+} \oplus A_{-} \oplus A^{\perp} ,
$$

with $A_{+}$ positive definite and $A_{-}$ negative definite, and the Gram matrix in a basis adapted to the decomposition is the diagonal matrix with $p$ entries $+1$, $q$ entries $-1$ and $z$ entries $0$ after a rescaling of the basis by the square roots of the diagonal values.

*Proof.* The existence is the diagonalisation of a Hermitian form of *Quadratic Forms and Polarisation*, §*Diagonalisation over a Field*, read with the involution of the base carried along: the theorem of that article produces an orthogonal basis, the nonneutral elements of which are scaled to $\pm 1$ by the square roots of their diagonals and the neutral ones of which are orthogonal to the whole basis, hence lie in the radical because the form is orthogonal to every element when it is orthogonal to a basis. A neutral element of an orthogonal basis is therefore in $A^{\perp}$, and the diagonalisation gives both the decomposition and its normal form. The scalar statement of the decomposition and of its normal form is *Indefinite Inner Product Spaces*, §*The Fundamental Decomposition*. $\square$

**Theorem (Sylvester's law of inertia).** The three numbers $p$, $q$, $z$ are independent of the decomposition: if $A = A_{+} \oplus A_{-} \oplus A^{\perp}$ and $A = A'_{+} \oplus A'_{-} \oplus A^{\perp}$ are two such decompositions, then $\dim A_{+} = \dim A'_{+}$ and $\dim A_{-} = \dim A'_{-}$.

*Proof.* Divide by the radical and use the induced nondegenerate form on $A/A^{\perp}$, in which the images of $A_{+}$, $A_{-}$, $A'_{+}$, $A'_{-}$ are again definite and orthogonal complements; the two sums $A_{+} \oplus A_{-}$ and $A'_{+} \oplus A'_{-}$ are both equal to the whole of $A/A^{\perp}$. Let $\pi$ be the projection of $A'_{+}$ onto $A_{+}$ along $A_{-}$, so that $\ker\pi = A'_{+} \cap A_{-}$. An element of that kernel other than zero would be positive, being in $A'_{+}$, and negative, being in $A_{-}$, which is impossible; hence $\pi$ is injective and $\dim A'_{+} \leq \dim A_{+}$. The roles of the two decompositions are symmetric, so the two dimensions are equal, and then $\dim A'_{-} = \dim A_{-}$ because both sums equal $n - z$. $\square$

**Remark (the law is the invariance of the arithmetic).** Sylvester's law is what makes the signature an invariant of the form and not of a basis, and it is the finite-dimensional content of the classification of the next section. It is proved here for the scalar form carried by the sesqualgebra; the scalar statement, the discriminant and the Witt theory are *Quadratic Forms and Polarisation*, §*Sylvester's Law of Inertia*, and *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

**Example (inertia by congruence).** On $\mathbb{Q}^{3}$ with the Hermitian matrix

$$
H = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 0 & 1 \\ 0 & 1 & 3 \end{pmatrix}
$$

the inertia index is $(2,1,0)$, and the congruent matrix $P^{T}HP$ for the invertible upper triangular $P$ with ones on and above the diagonal has the same inertia index $(2,1,0)$: the signs survive the congruence. The computation of the inertia from the matrix is the diagonalisation of the theorem, and it was verified by recomputation, as the context of this article records.

### The Degenerate Case

**Remark (the radical is a left ideal).** The radical of the form of a sesqualgebra with a form is a left ideal, its image under $*$ is a right ideal, and the two need not agree; the asymmetry is *Topological Sesqualgebras with a Form*, §*The Radical Is an Ideal*, and the sesquilinear example is the matrix form $\operatorname{tr}(XE_{11}Y^{*})$, whose radical is the matrices with first column zero. For an indefinite form the radical is not the null set, and the descent to the quotient of *Positivity and the Positive Cone of a Hermitian Form*, §*The Definite Quotient*, is available on the module; the quotient carries the descended form with the inertia index $(p,q,0)$.

## The Positive and the Negative Parts

### The Decomposition

**Corollary (fixed ranks, movable parts).** The ranks are fixed by Sylvester's law, but the parts are not unique: in the hyperbolic plane both $A = \mathbb{R}e_{1} \oplus \mathbb{R}e_{2}$ and $A = \mathbb{R}(e_{1} + \tfrac{1}{2}e_{2}) \oplus \mathbb{R}(e_{1} + 2e_{2})$ are decompositions into a positive and a negative definite line, and the two decompositions are distinct. What the form fixes is the pair of ranks, and it is the reason the signature classifies the form while it does not canonise a subspace.

*Proof.* In the first decomposition $h(e_{1},e_{1}) = 1$ and $h(e_{2},e_{2}) = -1$ with $h(e_{1},e_{2}) = 0$, so the two lines are definite and orthogonal; in the second, $e_{1} + \tfrac{1}{2}e_{2}$ has diagonal $1 - \tfrac{1}{4} = \tfrac{3}{4}$ and $e_{1} + 2e_{2}$ has diagonal $1 - 4 = -3$, while $h(e_{1} + \tfrac{1}{2}e_{2}, e_{1} + 2e_{2}) = 1 - 1 = 0$, so the two lines are again definite and orthogonal. The ranks are $1$ and $1$ in both cases by Sylvester's law, and the decompositions are distinct because $e_{1} + \tfrac{1}{2}e_{2}$ is not a multiple of $e_{1}$. $\square$

### The Product Does Not Preserve the Parts

**Proposition (the parts are not subalgebras).** For a compatible Hermitian form the positive part need not be closed under multiplication: on $M_{2}(\mathbb{C})$ with the form $h(X,Y) = \operatorname{tr}(XGY^{*})$, $G = \operatorname{diag}(1,-1)$, the element $E_{21}$ is positive, $h(E_{21},E_{21}) = 1$, and its product with itself is zero, $E_{21}^{2} = 0$, which is neutral and not positive.

*Proof.* The form is Hermitian and compatible, since for a Hermitian $G$ the identity $h(XY,Z) = \operatorname{tr}(XYGZ^{*}) = \operatorname{tr}(YG(X^{*}Z)^{*}) = h(Y,X^{*}Z)$ holds by the cyclicity of the trace; the diagonal is $h(X,X) = \lvert X_{11}\rvert^{2} + \lvert X_{21}\rvert^{2} - \lvert X_{12}\rvert^{2} - \lvert X_{22}\rvert^{2}$, so the unit matrices in the first column are positive and those in the second column negative, and $E_{21}^{2} = 0$. $\square$

**Remark (what the failure means).** The inertia is an invariant of the **pairing** and not an algebraic decomposition of the object: a definiteness class of a compatible form is not a subalgebra, and no product structure is respected by the parts beyond the adjoint-pair identity that the compatibility keeps, $h(xz,w) = h(z,x^{*}w)$, which pairs the left multiplications without asking any sign of the values of $h$. Whether the positive part is closed under multiplication is a property of the pair and not a consequence of the compatibility, and the layer records the failure and claims nothing general; for a definite form the positive part is the whole of $A$, by *Positivity and the Positive Cone of a Hermitian Form*, §*The Positive Set*, and the question does not arise.

### The Symmetries of the Form

**Remark (the isometry group).** The operators preserving the form, $h(Tx,Ty) = h(x,y)$, form the **isometry group** of the pair, whose classical instances are the orthogonal groups $O(p,q)$ for the real symmetric forms and the unitary groups $U(p,q)$ for the complex Hermitian ones, both indefinite as soon as both parts are nonzero; in the layer the operators are *Unitary and Isometric Operators of the Form*, and the group of the elements, $h(ux,uy) = h(x,y)$ for the multiplication by an element, is *The Unitary Group as a Topological Group*. The size of the negative part of the form is what bounds the geometry; the complete indefinite theory of that geometry is the Krein-space layer named above and not this article.

**Remark (the fundamental symmetry).** For a nondegenerate indefinite form on a finite-dimensional module there is an invertible linear operator $J$ with $J^{2} = \mathrm{id}$ which is self-adjoint for $h$ and for which the pairing $h(Jx,y)$ is positive definite; the decomposition of the theorem is an eigenspace decomposition of such a $J$, the operator is not unique, and it is the bridge over which the definite theory is imported into the indefinite one. The existence of $J$ in the scalar theory is *Indefinite Inner Product Spaces*, §*The Fundamental Symmetry*; the construction, its non-uniqueness and the angular operator are *The Fundamental Symmetry of the Form*, and *The Fundamental Symmetry* of the bilinear layer is the completed counterpart; this article uses the decomposition and not the operator.

## The Loss of the Norm

The failure of the Cauchy–Schwarz inequality and of the triangle inequality, and the definite companion form that the fundamental symmetry supplies, are the topological reading of an indefinite form: they are Part II's, in *Positivity and the Positive Cone of a Hermitian Form*, §*The Tolerance*, and *The Norm Defined by a Form*, §*The Inequality*, and they are named here rather than proved. What the algebraic theory keeps is the arithmetic of the form — the inertia index, the decomposition into the definite parts and the signature — which is the subject of the next section; the complete indefinite space, its topology and its operator theory are the bilinear layer's, of *Indefinite Inner Product Spaces*, *Krein Spaces* and *Pontryagin Spaces*.

## The Classification

### The Field Case

**Theorem (classification over $\mathbb{R}$ and $\mathbb{C}$).** Over $\mathbb{R}$ with $\varsigma = \mathrm{id}$ a nondegenerate symmetric form is determined up to congruence by its signature $(p,q)$, and over $\mathbb{C}$ with the conjugation a nondegenerate Hermitian form is likewise determined by its signature $(p,q)$; in both cases there is a basis in which the Gram matrix is $\operatorname{diag}(1,\ldots,1,-1,\ldots,-1)$.

*Proof.* The existence of the normal form is the decomposition theorem, and its uniqueness is Sylvester's law; the classical statement and its proof for the scalar theory are *Indefinite Inner Product Spaces*, §*Classification over $\mathbb{R}$ and $\mathbb{C}$*. $\square$

**Remark (bilinear against Hermitian over $\mathbb{C}$).** A symmetric **bilinear** form over $\mathbb{C}$ is classified by its rank alone, because the scaling by $i$ turns $-1$ into the square $i^{2}$; the signature is a phenomenon of the Hermitian forms, where the scalar square is a modulus square and the sign is preserved by every scalar. This is the scalar distinction of *Indefinite Inner Product Spaces*, §*Classification over $\mathbb{R}$ and $\mathbb{C}$*, and it is the sense in which the layer with $\varsigma \neq \mathrm{id}$ has an arithmetic that the collapsed layer with $\varsigma = \mathrm{id}$ and a complex base does not have.

### The Witt Group

**Remark (the signature is the complete invariant over the classical bases).** Over $\mathbb{R}$, and over $\mathbb{C}$ with the conjugation, the signature is a complete invariant of the nondegenerate Hermitian forms up to congruence, and the Witt group of those forms is $\mathbb{Z}$, the class of a form being its signature. Over a general field the signature is not complete and the discriminant and the Hasse invariants enter, as over $\mathbb{Q}$; over a general involutive ring the Witt group is the object of *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, whose forms are the Hermitian ones of this article. The inertia index of a degenerate form is not a Witt invariant, the radical being the part that the Witt construction discards, and it is read on the quotient of *Positivity and the Positive Cone of a Hermitian Form*, §*The Definite Quotient*.

### The Collapse at the Trivial Involution

**Theorem (the collapse).** Let $\varsigma = \mathrm{id}$, so that the form is symmetric and $R$-bilinear. Then the inertia index, Sylvester's law and the decomposition are the statements of the scalar indefinite theory, and the object is an involutive algebra with a symmetric nondegenerate form whose left multiplications are self-adjoint; the diagonal lies in $k = R$, the neutral elements and the tolerance are those of *Indefinite Inner Product Spaces*, and the Pontryagin index is the smaller of the two ranks.

*Proof.* Each statement is the corresponding statement above read at $\varsigma = \mathrm{id}$: the modulus square is the square, the Hermitian condition is the symmetry, and the form of the layer collapses by *Topological Sesqualgebras with a Form*, §*The Collapse at the Trivial Involution*. $\square$

**Remark (which statements are sesquilinear).** The inertia law, the decomposition and the classification are statements about a scalar form and hold in both categories; the sesquilinear content of the article lies in the fact that the Hermitian condition $h(y,x) = \varsigma(h(x,y))$ is not the symmetry, so that the Gram matrix is Hermitian for the involution rather than symmetric, and in the vanishing of the modulus square at a neutral element, $h(x,x) = 0$ with $x \neq 0$, which in the sesquilinear case is not merely the vanishing of a square.

## Examples

### The Hyperbolic Plane

**Example (the hyperbolic plane).** Let $A = \mathbb{R}^{2}$ with the pointwise product, $\varsigma = \mathrm{id}$, $* = \mathrm{id}$ and $h(u,v) = u_{1}v_{1} - u_{2}v_{2}$. The inertia index is $(1,1,0)$, the Pontryagin index is $1$, the null set is the union of the two neutral lines while the radical is zero, and the neutral pair $e_{1} + e_{2}$, $e_{1} - e_{2}$ has $h(x,x) = h(y,y) = 0$ with $h(x,y) = 2$, the failure of the Cauchy–Schwarz inequality being Part II's. The example is the collapsed model and the reference for the failures named above.

### The Matrix Algebra with an Indefinite Form

**Example (the indefinite matrix form).** On $M_{2}(\mathbb{C})$ with $G = \operatorname{diag}(1,-1)$ the form $h(X,Y) = \operatorname{tr}(XGY^{*})$ is Hermitian, compatible and nondegenerate, its Gram matrix in the order $E_{11}, E_{21}, E_{12}, E_{22}$ being $\operatorname{diag}(1,1,-1,-1)$, so its inertia index is $(2,2,0)$ and its Pontryagin index is $2$; the identity matrix is neutral, $h(1,1) = \operatorname{tr}G = 0$, without being in the radical, and the positive part is not closed under multiplication, $E_{21}^{2} = 0$. The example is the sesquilinear model of the article: it exhibits a nondegenerate indefinite form on a sesqualgebra, the neutral element $1$ of the unit, and the algebraic failure of the parts.

### The Biquaternion Caution

**Remark (an indefinite form on the algebra is not an indefinite form of the layer).** On the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ the four pairings of *The Four Pairings of the Biquaternion Algebra* have signatures $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$ over $\mathbb{R}$; the two bilinear ones belong to the bilinear layer, the general plain sesquilinear one $\operatorname{Sc}(PQ^{*}) = \sum_\mu P_\mu\varsigma(Q_\mu)$ is the definite form of the layer on $\mathbb{B}$ with the definite form of *The Norm Defined by a Form*, and the **general quaternionic sesquilinear** one

$$
\operatorname{Sc}(P^{\natural}Q^{*}) = \sum_{\mu} \varepsilon_{\mu} P_{\mu}\,\varsigma(Q_{\mu}), \qquad \varepsilon = (1,-1,-1,-1),
$$

is indefinite, Hermitian, nondegenerate, of signature $(2,6)$, with the diagonal $\lvert Q_0\rvert^{2} - \lvert Q_1\rvert^{2} - \lvert Q_2\rvert^{2} - \lvert Q_3\rvert^{2}$. It is nevertheless **not an indefinite form of the layer**, because it is not compatible with the product: the adjoint of the left multiplication $L_{Q}$ for it is the **right** multiplication $R_{\bar{Q}}$, the rule $(L_Q)^{\langle\cdot,\cdot\rangle_{\natural*}} = R_{\bar{Q}}$ of *The Four Pairings of the Biquaternion Algebra*, §*The Forms in Comparison*, whereas the compatibility requires the adjoint to be the left multiplication $L_{Q^{*}}$, which is what holds for the general plain sesquilinear form. The identity $h(xz,w) = h(z,x^{*}w)$ of the entry therefore fails for it, and a witness to the failure was recomputed. An indefinite form of the layer on $\mathbb{B}$ does exist: transporting the matrix model along the algebra isomorphism $\Phi : \mathbb{B} \to M_{2}(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, which carries $*$ to the conjugate transpose, gives $h(P,Q) = \operatorname{tr}(\Phi(P)G\Phi(Q)^{*})$ with $G = \operatorname{diag}(1,-1)$, a compatible, nondegenerate and indefinite form of the same inertia as the matrix model, $(2,2)$ over $\mathbb{C}$ and $(4,4)$ over $\mathbb{R}$. The remark is the general warning that the phrases "an indefinite form on $A$" and "an indefinite form of the layer on $A$" are not the same, the second requiring the compatibility, and that the four pairings of the biquaternion algebra are compared in one and the same space in the pairings article, without the compatibility being at issue there.

### The Anisotropic Caution

**Example (indefinite without neutral elements).** Over $\mathbb{Q}$, let $A = \mathbb{Q}^{2}$ with the pointwise product, $\varsigma = \mathrm{id}$, $* = \mathrm{id}$ and $h(u,v) = u_{1}v_{1} - 2u_{2}v_{2}$. The form is symmetric, compatible, nondegenerate, of inertia index $(1,1,0)$ and of Pontryagin index $1$, and it has no nonzero neutral element, since $u_{1}^{2} = 2u_{2}^{2}$ has no rational solution for $u \neq 0$. The example is the caution that the indefinite case is read from the two ranks and not from the presence of neutral elements, and it is the reason the article states the inertia through the decomposition rather than through the isotropic set.

## Summary

A Hermitian form is **indefinite** when its diagonal takes both signs, $h(x,x) > 0$ and $h(y,y) < 0$ for some $x, y$, and then no norm is available: the **null set** $N(h) = \{x : h(x,x) = 0\}$ is in general properly larger than the radical, the tolerance $x \succeq y$ when $h(x-y,x-y) \geq 0$ is not transitive, and no norm is read off the diagonal; the failure of the Cauchy–Schwarz and of the triangle inequality, and the definite companion form, are Part II's. What replaces the norm is the **arithmetic** of the form: the **Gram matrix** $H_{ij} = h(e_{i},e_{j})$ is Hermitian for $\varsigma$ and the form is nondegenerate exactly when $H$ is invertible, the **inertia index** $(p,q,z)$ counts the ranks of positivity and of negativity and the dimension of the radical, $A$ is the orthogonal sum $A_{+} \oplus A_{-} \oplus A^{\perp}$ with the parts definite and the normal form $\operatorname{diag}(1^{p},(-1)^{q},0^{z})$, and **Sylvester's law of inertia** makes $(p,q,z)$ independent of the decomposition, the **signature** $(p,q)$ classifying the nondegenerate form over $\mathbb{R}$ and, in the Hermitian case, over $\mathbb{C}$, with the **Pontryagin index** $\kappa = \min(p,q)$. Two facts are proper to the sesqualgebra layer: the parts are **not subalgebras** — on $M_{2}(\mathbb{C})$ with $\operatorname{tr}(XGY^{*})$, $G = \operatorname{diag}(1,-1)$, the positive element $E_{21}$ has $E_{21}^{2} = 0$ — so the inertia is an invariant of the pairing and not an algebraic decomposition of the object; and the **compatibility** survives the loss of definiteness only as the adjoint-pair identity $h(xz,w) = h(z,x^{*}w)$, the radical remaining a left ideal. The definite companion $h(J\cdot,\cdot)$ of the **fundamental symmetry** and its norm are *The Fundamental Symmetry of the Form* and *The Norm Defined by a Form*, the isometries are *Unitary and Isometric Operators of the Form*, and the complete indefinite spaces, the Krein and Pontryagin spaces and their spectral theory, are the bilinear layer of *Indefinite Inner Product Spaces*, *Krein Spaces* and *Pontryagin Spaces*, named and deferred. At $\varsigma = \mathrm{id}$ the article collapses to the scalar indefinite theory, the sesquilinear content lying in the Hermitian condition and in the vanishing of the modulus square at a neutral element. The examples are the hyperbolic plane, the indefinite matrix form of inertia $(2,2,0)$ and the anisotropic form over $\mathbb{Q}$, and the biquaternion caution that the general quaternionic sesquilinear pairing of the four pairings of $\mathbb{B}$, though indefinite, Hermitian, nondegenerate and of signature $(2,6)$, is not compatible with the product and is therefore an indefinite form on the algebra and not an indefinite form of the layer.

## Summary of Notation

| symbol | meaning |
|---|---|
| $h(x,x) > 0$ and $h(y,y) < 0$ | the indefinite form: the diagonal takes both signs |
| $N(h) = \{x : h(x,x) = 0\}$ | the null set, in general properly larger than the radical for an indefinite form |
| $x \succeq y \iff h(x-y,x-y) \geq 0$ | the tolerance, symmetric and translation invariant, transitive only in the semi-definite cases |
| $H_{ij} = h(e_{i},e_{j})$ | the Gram matrix, Hermitian for $\varsigma$, invertible exactly in the nondegenerate case |
| $(p,q,z)$ | the inertia index: ranks of positivity and of negativity, and $\dim A^{\perp}$ |
| $A = A_{+} \oplus A_{-} \oplus A^{\perp}$ | the fundamental decomposition, with the parts definite and the ranks fixed but the parts not unique |
| $\operatorname{diag}(1^{p},(-1)^{q},0^{z})$ | the normal form of the Gram matrix after a congruence and a rescaling |
| $(p,q)$ | the signature in the nondegenerate case; the complete invariant over $\mathbb{R}$ and over $\mathbb{C}$ for Hermitian forms |
| $\kappa = \min(p,q)$ | the Pontryagin index, the rank of the smaller of the two parts |
| $\lvert h(x,y)\rvert^{2} \leq C\,h(x,x)h(y,y)$ | fails for an indefinite form; no constant $C$ repairs it |
| $E_{21}^{2} = 0$ with $h(E_{21},E_{21}) = 1$ | the positive part is not closed under multiplication, on $M_{2}(\mathbb{C})$ with $\operatorname{tr}(XGY^{*})$ |
| $\varsigma = \mathrm{id}$ | the collapse: symmetric bilinear form, Hermitian condition becomes symmetry, scalar indefinite theory |

## Further Reading

- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for Sylvester's law, the inertia of a Hermitian form and the Witt group.
- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the classification of the indefinite spaces, the invariant subspaces and the operator theory of the indefinite case.
- Tomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the indefinite form, its subspaces and the neutral vectors.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the canonical forms of the indefinite pairs and the perturbation of the definite and indefinite cases.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the Hermitian forms over a ring with involution and the congruence by the twisted transpose.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the inertia law for Hermitian matrices, the congruence $P^{*}HP$ and its signed invariants.
