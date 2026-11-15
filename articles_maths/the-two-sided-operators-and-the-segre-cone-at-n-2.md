# __The Two-Sided Operators and the Segre Cone at $n=2$__

## Introduction

**A two-sided operator $Z\mapsto XZY$ has rank the product of the two ranks, and the elements of the matrix space that it can produce from the identity are the decomposable tensors, whose determinant vanishes: the Segre cone of the algebra is the quadric cone $\det=0$.**

The article studies the operators built from one left and one right multiplication, computes their rank, identifies the decomposable elements as the rank-one matrices and their projectivisation as the Segre variety $\mathbb{P}^{1}\times\mathbb{P}^{1}$, proves that the determinant is the defining quadratic form of the cone with signature $(2,2)$ over the real field, and describes the operators that preserve the cone. It assumes *The One-Sided Operators at $n=2$*, *$\operatorname{End}(M_2(\mathbb{C}))$ as an Algebra: the Regular Representation* and *The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$*.

It follows the biquaternion article *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* for the norm that plays the role of the determinant.

## The Two-Sided Operators

**The operators $L_{X}R_{Y}$ form a sixteen-dimensional space, and every endomorphism of the matrix space is one.**

**Definition.** A **two-sided operator** is an operator of the form $T_{X,Y}(Z)=XZY$.

**Proposition.** The two-sided operators span the whole endomorphism algebra, and $T_{X,Y}$ depends bilinearly on the pair.

**Proof.** The products $L_{E_{ij}}R_{E_{kl}}$ are the sixteen matrix units of the endomorphism algebra by *$\operatorname{End}(M_2(\mathbb{C}))$ as an Algebra: the Regular Representation*, and the map is bilinear by the bilinearity of the product.

**Corollary.** Every endomorphism is a sum of at most four two-sided operators.

**Proof.** The sixteen matrix units group into four blocks of four, and each block is a single two-sided operator.

**Corollary.** The composition of two-sided operators is two-sided, so they form a subsemigroup of the endomorphism semigroup.

**Proof.** $T_{X,Y}\circ T_{X',Y'}=T_{XX',Y'Y}$, by associativity.

## The Rank of a Two-Sided Operator

**Theorem.** For matrices $X$ and $Y$ the rank of $T_{X,Y}$ is the product $\operatorname{rank}X\cdot\operatorname{rank}Y$.

**Proof.** The image of $T_{X,Y}$ consists of the matrices $XZY$; their columns lie in the image of $X$ and their rows lie in the image of $Y^{\mathsf T}$, so the image is contained in a space of dimension $\operatorname{rank}X\cdot\operatorname{rank}Y$. Conversely, choosing basis vectors in the two images exhibits that many independent images, so the bound is attained.

**Corollary.** The two-sided operator is invertible exactly when both factors are invertible.

**Proof.** The rank is four exactly when both ranks are two.

**Corollary.** A two-sided operator built from two rank-one matrices has rank one, so it is a rank-one operator.

**Proof.** The product is one times one.

## The Decomposable Elements

**Proposition.** The rank-one matrices are exactly the products $uv^{\mathsf T}$ with $u,v$ nonzero column vectors, and they are the decomposable tensors of the space $\mathbb{C}^{2}\otimes\mathbb{C}^{2}$.

**Proof.** A rank-one matrix has a one-dimensional image spanned by some $u$ and a one-dimensional row space spanned by some $v^{\mathsf T}$, so it is $uv^{\mathsf T}$; conversely such a product has rank one.

**Corollary.** The set of decomposable elements is the image of the Segre map $\mathbb{P}^{1}\times\mathbb{P}^{1}\to\mathbb{P}^{3}$, and it is a quadric surface.

**Proof.** The pair of lines $(u,v)$ is taken up to two independent scalars, which is the product of two projective lines; the image satisfies the quadratic equation of the determinant and has dimension two, so it is a quadric surface.

**Corollary.** The rank-one matrices are exactly the rank-one idempotents up to scaling, and the idempotents among them are $uv^{\mathsf T}$ with $v^{\mathsf T}u=1$.

**Proof.** The square of $uv^{\mathsf T}$ is $(v^{\mathsf T}u)uv^{\mathsf T}$, which equals $uv^{\mathsf T}$ exactly when the scalar is one.

## The Determinant and the Cone

**Theorem.** The determinant is a quadratic form on the matrix space, its zero set is the set of matrices of rank at most one, and over $\mathbb{R}$ its signature is $(2,2)$.

**Proof.** The determinant is a homogeneous polynomial of degree two in the four entries, and it vanishes exactly when the two columns are dependent, which is the rank condition. In the basis of matrix units the associated bilinear form has the Gram matrix with the two off-diagonal blocks $\tfrac12$ and $-\tfrac12$, whose eigenvalues are $\pm\tfrac12$, twice each.

**Corollary.** The Segre cone is the quadratic cone of the determinant, and its projectivisation is the quadric surface of decomposable elements.

**Proof.** The cone over the Segre variety is the zero set of the determinant minus the origin, which is the cone of a quadratic form.

**Corollary.** The cone is not convex, and it contains the two halves $\det>0$ and $\det<0$ on opposite sides.

**Proof.** A quadratic form of signature $(2,2)$ has a cone with two components in the positive set and one in the negative set, and the cone itself separates them.

## The Sign of the Determinant

**Proposition.** On the real matrix space the two sets $\det>0$ and $\det<0$ are each connected, and the cone separates them.

**Proof.** Because the determinant has signature $(2,2)$, there are linear coordinates in which it reads $u^{2}+v^{2}-w^{2}-z^{2}$. The set where this is positive is $\{u^{2}+v^{2}>w^{2}+z^{2}\}$, which retracts onto the circle $u^{2}+v^{2}=1$, $w=z=0$, so it is connected; the set where it is negative similarly retracts onto the circle in the other pair of coordinates.

**Corollary.** The rotations of the plane lie in the set $\det>0$ and the reflections lie in the set $\det<0$, and each of the two sets is connected.

**Proof.** A rotation has determinant one, a reflection has determinant minus one, and the two sets are connected by the proposition.

**Corollary.** The group of invertible matrices has two connected components over $\mathbb{R}$ and one over $\mathbb{C}$.

**Proof.** The sign of the determinant separates the two real components by the proposition, and over $\mathbb{C}$ the determinant can be moved to one along a path because the complex numbers other than zero are connected.

**Corollary.** The cone is the common boundary of the two sets, and every path from one to the other crosses a matrix of rank one.

**Proof.** A continuous path whose determinant changes sign must have a point where the determinant vanishes, and that is a matrix of rank at most one.

## The Operators Preserving the Cone

**Proposition.** An invertible two-sided operator $T_{X,Y}$ multiplies the determinant by $\det(X)\det(Y)$, so it preserves the zero set of the determinant.

**Proof.** $\det(XZY)=\det X\det Z\det Y$ for every $Z$.

**Corollary.** Every invertible two-sided operator preserves the Segre cone, and it preserves the two components exactly when the product of the determinants is positive.

**Proof.** The determinant is multiplied by a nonzero scalar, so its zero set is preserved; the sign of the scalar decides whether the two components are exchanged.

**Corollary.** The operators that preserve the cone up to a scalar are the two-sided operators together with the transposition, which also multiplies the determinant by a sign.

**Proof.** The two-sided operators give all the multiplications of the determinant by nonzero scalars, and transposition gives the remaining sign, since $\det(Z^{\mathsf T})=\det Z$.

## Summary

A two-sided operator $Z\mapsto XZY$ has rank the product of the ranks of the two parameters, and the sixteen operators of this form span the endomorphism algebra. The decomposable elements of the matrix space are the rank-one matrices $uv^{\mathsf T}$, whose projectivisation is the Segre variety $\mathbb{P}^{1}\times\mathbb{P}^{1}$.

The determinant is the quadratic form whose zero set is the cone over that variety, and over $\mathbb{R}$ its signature is $(2,2)$. An invertible two-sided operator multiplies the determinant by the product of the two determinants, so it preserves the cone and acts on its components according to the sign of that product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{X,Y}(Z)=XZY$ | the two-sided operator |
| $uv^{\mathsf T}$ | a rank-one matrix, a decomposable tensor |
| $\mathbb{P}^{1}\times\mathbb{P}^{1}$ | the Segre variety of decomposable elements |
| $\det$ | the quadratic form defining the cone |
| $(2,2)$ | the signature of the determinant over $\mathbb{R}$ |

## Further Reading

- Igor R. Shafarevich, *Basic Algebraic Geometry* (Springer, 2013), for Segre varieties and quadrics.
- Joseph M. Landsberg, *Tensors: Geometry and Applications* (American Mathematical Society, 2012), for decomposable tensors and their secant varieties.
- [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html), for the two families whose products are studied here.
- [$\operatorname{End}(M_2(\mathbb{C}))$ as an Algebra: the Regular Representation](end-m2c-as-an-algebra-the-regular-representation.html), for the ambient algebra.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$](the-element-rank-trace-determinant-characteristic-polynomial-at-n-2.html), for the determinant used as a quadratic form.
