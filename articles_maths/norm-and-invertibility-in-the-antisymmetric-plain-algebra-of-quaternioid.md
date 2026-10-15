# __Norm and Invertibility in the Antisymmetric Plain Algebra__

## Introduction

A norm and an inverse are read in a product, and the equations name it. The block of this article is
the **antisymmetric plain multiplication**

$$
\tilde p\times\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr)=\vec p\times\vec q,
$$

the cross product of the two vector parts, the antisymmetric half of the general plain bilinear
product; it is $\mathbb{R}$-bilinear, alternating, of zero scalar part and without a unit
(*Introduction to the Antisymmetric Plain Algebra of Quaternions*). The classical theory belongs to
a unital associative product, and the block has neither; this article states what that costs and what
survives.

The answer is an absence and a substitute. The block has **no unit** on either side, hence **no
inverse** and an empty group of units, and **no algebraic norm**, its square and its conjugated
square both vanishing identically. The quadratic objects it does carry are the operator trace form
$K(\tilde a,\tilde b)=\operatorname{Tr}(L_{\tilde a}L_{\tilde b})=-2\,\vec a\cdot\vec b$ and
the scalar-part form $\varphi(\tilde p,\tilde q)=p_0q_0$; the first is the invariant form of the block
and the Killing form of the bracket, the second the rank-one form whose radical is the vector
subspace, and neither is multiplicative.

The word *norm* names here the **algebraic norm**, a central-valued quadratic map attached to a
product and not a norm on a vector space. The general definitions are *Definitions for the Study of
the Algebraic Structures*; the algebraic norms of the parent are *The 2 Algebraic Norms over the
Quaternion $\mathbb{R}$ Space*; and the invariant form of the block is *The Killing Form of the
Antisymmetric Plain Algebra*.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; a generic element is $\tilde q=q_0e_0+\vec q$, the centre is
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the vector subspace is
$\mathrm{Vect}(\mathbb{H})=\{\vec q\}$; $\tilde p\tilde q$ is the general plain bilinear product,
and $\vec p\cdot\vec q$, $\vec p\times\vec q$ the Euclidean dot and vector products. The
natural conjugation is $\tilde q^{\natural}=q_0e_0-\vec q$; over $\mathbb{R}$ the bar is the
identity and the star coincides with the natural conjugation. The plain form is
$B(\tilde p,\tilde q)=p_0q_0-\vec p\cdot\vec q$, the parent norm is
$N(\tilde q)=\tilde q\tilde q^{\natural}=\sum_\mu q_\mu^2$, and the left multiplication operator is
$L_{\tilde p}\tilde x=\tilde p\times\tilde x$. Unqualified, *unit*, *inverse* and *norm* mean the
unit, the inverse and the algebraic norm of the block.

## The Relative Definitions

The word *unit* and the word *inverse* name a product, so the definitions are stated once for a
general product and read on the block; they are *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Element Vocabulary*.

**Definition (unit).** Let $\star$ be a product on $\mathbb{H}$. An element $e$ is a **left unit of
$\star$** when $e\star\tilde x=\tilde x$ for every $\tilde x$, a **right unit** when
$\tilde x\star e=\tilde x$ for every $\tilde x$, and a **unit** or **two-sided unit** when both. A
product with a unit is **unital**.

**Definition (inverse).** Let $\star$ be a unital product with unit $e$. An element $\tilde p$ is
**invertible of $\star$** when there is $\tilde q$ with $\tilde p\star\tilde q=e=\tilde q\star\tilde p$;
such a $\tilde q$ is the **inverse of $\tilde p$**, and the invertible elements form the **group of
units**. The definitions are relative to the product: the element $e_0$ is the unit of the general
plain product and is not a unit of the block.

Throughout this article the product is the antisymmetric plain multiplication $\times$, and the
unit, the inverse and the group of units are read in $\times$.

## The Absence of a Unit

**Theorem (no unit).** The operation $\times$ has no left unit and no right unit; there is no
$\tilde e$ with $\tilde e\times\tilde x=\tilde x$ for every $\tilde x$, and none with
$\tilde x\times\tilde e=\tilde x$ for every $\tilde x$. Hence there is no two-sided unit.

*Proof.* A left unit $\tilde e$ would satisfy, at $\tilde x=e_0$, whose vector part is zero,
$\tilde e\times e_0=\vec e\times\mathbf{0}=0$, which would have to equal $e_0$; the two differ,
since $e_0$ is nonzero. A right unit would satisfy, again at $\tilde x=e_0$,
$e_0\times\tilde e=\mathbf{0}\times\vec e=0$, which would again have to equal $e_0$.

The absence is structural: the value of the block is a pure vector for every pair of arguments, and
the equations that name a unit require the central element $e_0$ on the right. The scalar direction
is invisible to the operation, and a unit is exactly an element the operation cannot see.

## The Absence of an Inverse

**Corollary (no inverse, no group of units).** No element of $\mathbb{H}$ is invertible of the
block, and the group of units of $\times$ is empty.

*Proof.* The inverse is defined by the pair of equations $\tilde p\times\tilde q=e=\tilde q\times\tilde p$
with $e$ a two-sided unit; the block has none, so the equations have no solution. There is no
one-sided notion either, the one-sided inverse being defined against a one-sided unit and no
one-sided unit existing.

**Remark (the equation to the centre).** The equation $\tilde p\times\tilde q=e_0$ has no solution in
$\mathbb{H}$ directly: its left side is a pure vector, of scalar part zero, for every pair, and its
right side has scalar part one. The block cannot produce a central value at all, so the inverse
equation is unsolvable even before the two-sided character of the unit is required.

## The Absence of an Algebraic Norm

**Definition (algebraic norm of a product).** Let $\star$ be a product on $\mathbb{H}$. The
**algebraic norm** of $\star$ is the quadratic map $\tilde x\mapsto\tilde x\star\tilde x$, the
product read at its two equal arguments, and the **conjugated algebraic norm** is the quadratic map
$\tilde x\mapsto\tilde x\star\tilde x^{\natural}$, the product read on the element and its natural
conjugate (*The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*). An algebraic norm is
**central valued** when all its values lie in the centre; the conjugated algebraic norm of the
general plain product is the central square $\tilde x\tilde x^{\natural}=N(\tilde x)e_0$ with
$N(\tilde x)=\sum_\mu x_\mu^2$, and it is that central-valued norm which the block loses (*Norm and
Invertibility in the General Plain Algebra*).

**Theorem (the block has no algebraic norm).** For every element $\tilde x$,

$$
\tilde x\times\tilde x=0,\qquad \tilde x\times\tilde x^{\natural}=0 .
$$

Both canonical quadratics of the block, the square and the conjugated square, vanish identically, so
both are the zero quadratic form and the block has no algebraic norm: neither of the two quadratics
that a product carries is a nonzero central-valued map.

*Proof.* The first identity is alternation, $\tilde x\times\tilde x=0$ for every $\tilde x$, by
*Introduction to the Antisymmetric Plain Algebra of Quaternions*. For the second, the natural
conjugate is $\tilde x^{\natural}=x_0e_0-\vec x$, and the value of the block on a pair is the cross
product of the vector parts, so
$\tilde x\times\tilde x^{\natural}=\vec x\times(-\vec x)=-\vec x\times\vec x=0$.

The vanishing is total: the block removes the scalar part of the parent, and with it the parent's
central-valued form $N(\tilde x)=x_0^2+\lvert\vec x\rvert^2$. What the block keeps is a pair of
forms on the whole space, and the word *norm* is read here as the absent central-valued quadratic
form, not as a norm on a space.

## The Two Forms That Survive

**Definition (the operator trace form).** The **operator trace form** of the block is
$K(\tilde a,\tilde b)=\operatorname{Tr}(L_{\tilde a}L_{\tilde b})$, the trace of the composition of
the two left multiplication operators.

**Definition (the scalar-part form).** The **scalar-part form** of the block is
$\varphi(\tilde p,\tilde q)=p_0q_0$, the product of the two scalar parts.

**Proposition (the operator trace form).** For all $\tilde a,\tilde b$,
$K(\tilde a,\tilde b)=-2\,\vec a\cdot\vec b=-2\,(a_1b_1+a_2b_2+a_3b_3)$; on the diagonal
$K(\tilde x,\tilde x)=-2\lvert\vec x\rvert^2$. The Gram matrix of $K$ in the basis is
$\operatorname{diag}(0,-2,-2,-2)$, the rank of $K$ is three, its radical is the centre
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$, and on the vector subspace $K$ is non-degenerate.

*Proof.* The operator $L_{\tilde a}$ kills the scalar direction, its first column being zero, and acts
on the vector part by $\vec x\mapsto\vec a\times\vec x$, so it is the block matrix
$\operatorname{diag}(0,C_{\vec a})$ with $C_{\vec a}$ the cross-product matrix of $\vec a$.
The composition is $\operatorname{diag}(0,C_{\vec a}C_{\vec b})$, of trace
$\operatorname{Tr}(C_{\vec a}C_{\vec b})$, the scalar block contributing nothing. For
skew-symmetric matrices, $\operatorname{Tr}(C_{\vec a}C_{\vec b})$ is the negative of the
Frobenius pairing, which is $2\,\vec a\cdot\vec b$ here, so the trace is
$-2\,\vec a\cdot\vec b$. The Gram entries are read at the units, $\mathbf e_i\cdot\mathbf e_j=\delta_{ij}$,
whence the diagonal $\operatorname{diag}(0,-2,-2,-2)$; the rank is three, and the radical is the set
orthogonal to every vector part, that is the centre.

**Proposition (the invariance of the two forms).** Both forms are symmetric and invariant under the
block: for all $\tilde p,\tilde q,\tilde x$,

$$
K\bigl(\tilde p\times\tilde x,\tilde q\bigr)+K\bigl(\tilde x,\tilde p\times\tilde q\bigr)=0,
\qquad
\varphi\bigl(\tilde p\times\tilde x,\tilde q\bigr)+\varphi\bigl(\tilde x,\tilde p\times\tilde q\bigr)=0 .
$$

*Proof.* For $K$ the left equation reads
$-2(\vec p\times\vec x)\cdot\vec q-2\,\vec x\cdot(\vec p\times\vec q)=0$, the
antisymmetry of the scalar triple product, the two terms being opposite. For $\varphi$ both terms
vanish outright, because $\tilde p\times\tilde x$ is a pure vector and the scalar-part form is zero
whenever one argument is central. The symmetry of $K$ is that of $\vec a\cdot\vec b$, and that
of $\varphi$ the symmetry of the product of the two scalar parts.

**Remark (the two invariant forms).** The operator trace form $K$ and the scalar-part form
$\varphi$ are independent, and they span the invariant symmetric forms of the block: a computation
on the centre forces every invariant form to annihilate the pairings of the centre with the vector
subspace, and on the vector subspace the invariant symmetric forms are proportional to
$\vec p\cdot\vec q$, the vector subspace carrying the irreducible three-dimensional
representation of the block. The two extremes are $\varphi$, of rank one, whose radical and
isotropic cone are the whole vector subspace, and $K$, non-degenerate on the vector subspace, whose
radical is the centre. Their combination $\varphi+\tfrac12K=B$ is the plain form of the parent. The
identification of $K$ with the Killing form
$\kappa(\tilde p,\tilde q)=\operatorname{Tr}(\operatorname{ad}_{\tilde p}\operatorname{ad}_{\tilde q})=-2\,\vec p\cdot\vec q$
of the block is *The Killing Form of the Antisymmetric Plain Algebra*, cited here and not reproved;
the adjoint operator $\operatorname{ad}_{\tilde p}\tilde r=\tilde p\times\tilde r$ is the left
multiplication $L_{\tilde p}$, so the two traces coincide and the identification is exact.

## Multiplicativity

**Definition (multiplicativity).** Let $\star$ be a product and let $q$ be a quadratic form on
$\mathbb{H}$ valued in the centre. The form is **multiplicative of $\star$** when
$q(\tilde x\star\tilde y)=q(\tilde x)q(\tilde y)$ for all $\tilde x,\tilde y$, the equation being
read in the centre.

**Proposition (no multiplicativity).** Of the three quadratic forms available, none is
multiplicative: the operator trace form gives $K(e_1\times e_2,e_1\times e_2)=K(e_3,e_3)=-2$ against
$K(e_1,e_1)K(e_2,e_2)=(-2)(-2)=4$; the scalar-part form gives
$\varphi(e_0\times e_0,e_0\times e_0)=\varphi(0,0)=0$ against $\varphi(e_0,e_0)^2=1$; and the parent
norm gives $N(e_1\times e_1)=N(0)=0$ against $N(e_1)^2=1$.

*Proof.* The values of the block are read from its table, $e_1\times e_2=e_3$, $e_0\times e_0=0$ and
$e_1\times e_1=0$, and the right sides are computed from $K=-2\,\vec a\cdot\vec b$,
$\varphi=p_0q_0$ and $N(\tilde x)=\sum_\mu x_\mu^2$. A single pair separates the two sides in each
case, so no multiplicativity holds; the vanishing square satisfies the equation only because both
sides vanish, and it is a norm in no sense.

## The Comparison with the Parent Product

**Remark (the invertibility criterion is not transferred).** For the general plain algebra the
invertibility criterion is $N(\tilde q)\neq0$, equivalently the central square
$\tilde q\tilde q^{\natural}$ nonzero, with inverse $\tilde q^{\natural}/N(\tilde q)$ (*Norm and
Invertibility in the General Plain Algebra*). The criterion names the product, and for the block the
corresponding statement is the absence of the two previous sections: there is no unit against which
to invert, and the substitute equation $\tilde p\times\tilde q=e_0$ has no solution. No element of
the block is invertible, and the empty group of units is the sharp form of the statement. The parent
product is the block with the scalar part restored, and the restoration returns the central square
$N(\tilde x)e_0$; the block loses that square with the scalar part, so the loss is the absence of the
norm and not a numerical accident.

## Summary

The antisymmetric plain multiplication $\tilde p\times\tilde q=\vec p\times\vec q$ has no unit
on either side, hence no invertible element and an empty group of units: every value of the block is a
pure vector, and the inverse equation $\tilde p\times\tilde q=e_0$ has no solution. The block has no
algebraic norm, its square vanishing by alternation and its conjugated square
$\vec x\times(-\vec x)$ vanishing too, so the central-valued parent norm is lost with the scalar
part. What survives are two independent invariant symmetric forms, the operator trace form
$K(\tilde a,\tilde b)=-2\,\vec a\cdot\vec b$, of Gram matrix
$\operatorname{diag}(0,-2,-2,-2)$, rank three and radical the centre, which is the Killing form of the
bracket, and the rank-one scalar-part form $\varphi(\tilde p,\tilde q)=p_0q_0$, whose radical and
isotropic cone are the vector subspace. Neither is multiplicative, the pairs $(e_1,e_2)$, $(e_0,e_0)$
and $(e_1,e_1)$ separating the two sides, and the invertibility criterion of the parent is not
transferred.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\vec p\times\vec q$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $L_{\tilde a}\tilde x=\tilde a\times\tilde x$ | the left multiplication operator of the block |
| $K(\tilde a,\tilde b)=\operatorname{Tr}(L_{\tilde a}L_{\tilde b})=-2\,\vec a\cdot\vec b$ | the operator trace form, rank three, radical the centre, the invariant form of the block |
| $\varphi(\tilde p,\tilde q)=p_0q_0$ | the scalar-part form, rank one, radical the vector subspace |
| $N(\tilde q)=\sum_\mu q_\mu^2$, $N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$ | the parent norm and the quaternion form, not norms of the block |
| $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ | the centre, the radical of $K$, on which the block is invisible |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the unit, the inverse and the relativity of the definitions to the product
- *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternioid-r-space.md`), for the algebraic norm as the diagonal of the scalar-part form and the convention that counts a vanishing one as no norm
- *Introduction to the Antisymmetric Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.md`), for the operation, its class, its table and the absence of a unit
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-quaternion-algebra.md`), for the parent norm, its multiplicativity and the invertibility criterion the block does not have
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra-of-quaternioid.md`), for the identification of $K$ with the invariant form of the block, its radical, its rank and the Cartan criteria
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the unit, the inverse and the norm in an associative ring.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the Killing form, the invariant bilinear forms and the radical of a Lie algebra.
