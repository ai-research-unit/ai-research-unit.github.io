# __$M_2(R)$ Triangular Representation__

## Introduction

**The model.** Left multiplication by the dual number $Q=q+\varepsilon q'$ is an $R$-linear map of the two-dimensional algebra, and in the reversed basis $(\varepsilon,1)$ it is the matrix

$$
\mathsf{M}_2(Q)=qI_2+q'E=\begin{pmatrix}q&q'\\ 0&q\end{pmatrix},\qquad E=\begin{pmatrix}0&1\\ 0&0\end{pmatrix},\qquad E^{2}=0 .
$$

The map $\mathsf{M}_2$ is an injective $R$-algebra homomorphism onto the subalgebra of **upper-triangular Toeplitz** matrices, of dimension two inside the four of $M_2(R)$.

**The block's only non-semisimple algebra.** Every other category of Part VI is semisimple, being a field, a product of fields, or a full matrix algebra over one of them: the complex numbers, the split-complex and duo-complex numbers, the quaternions, the split-quaternions, the reduced biquaternions, the biquaternions and the split-biquaternions are all of that kind. The dual numbers are the exception, and the whole article is the reading of one fact, that the maximal ideal is a nonzero nilpotent ideal. The consequences, each proved below:

- the regular module is a non-split extension of $R$ by $R$, so the carrier carries one flag and the matrix is triangular;
- there is no idempotent but $0$ and $1$ in any base extension, hence no Peirce frame, no corners, and no decomposition of an element into orthogonal pieces;
- the determinant is $q^{2}$, a square, whose zero set is the whole maximal ideal: a line, and neither a point nor a pair of lines;
- the zero divisors are exactly the maximal ideal over a field, so the two-sided products contain the zero operator as a product of two nonzero parameters;
- the three natural forms are positive semidefinite, two of them degenerate with the maximal ideal as radical, and none is indefinite.

**Why the matrix is triangular, stated once.** The map is not the left regular matrix of the algebra written in a convenient basis; it is the matrix of the *only* indecomposable representation of dimension two. The carrier has the invariant flag

$$
0\subset\langle e_1\rangle\subset R^{2},\qquad Ee_2=e_1,\qquad Ee_1=0,
$$

and the two composition factors are both the residue field $R$, on which $Q$ acts by the same scalar $q$. Two equal diagonal entries, one off-diagonal entry, and no other shape is possible. The triangular form is the visible form of the non-split extension, and the double diagonal entry is the visible form of its having one composition factor twice.

**Boundaries.** The algebra, its product, its ideals and its maximal ideal are *Dual-Numbers Algebra*, *Dual-Numbers Ideals and the Maximal Ideal* and *Dual-Numbers Zero Divisors*; the norm, the unit criterion and the inverse are *Dual-Numbers Norm and Invertibility*; the distinguished submodules are *Dual-Number Subspaces*; the spectrum, the minimal polynomial and the Jordan form are *Spectral Regularity and Degeneracy in the Dual-Number Algebra*; the classification of the representations, the standard non-split extension and the Ext algebra are *Dual-Numbers Linear Representations*; the shears, the parabolic angle and the unit group are *Shears and Parabolic Rotations*; the automorphisms and the derivations are *Dual-Numbers Automorphisms and Derivations*; the polar decomposition is *Dual-Numbers Polar Decomposition*. The operators of this model are *$M_2(R)$ Triangular Representation : Operators*.

**Conventions.** $R$ is a commutative ring with identity in which $2$ is invertible; the field statements are made over a field $K$, and the geometric case is $R=\mathbb{R}$, written $\mathbb{C}^{\mathrm{dln}}$. The natural basis is $(1,\varepsilon)$ and the reversed one, which gives the upper shape, is $(\varepsilon,1)$. The element is $Q=q+\varepsilon q'$, with $q=\operatorname{Re}Q$ and $q'=\operatorname{Inf}Q$; the conjugate is $\bar Q=q-\varepsilon q'$; the norm is $\langle Q\rangle=Q\bar Q=q^{2}$; the maximal ideal is $\mathrm{M}=(\varepsilon)=\varepsilon R$; the real and infinitesimal submodules are $R_{\mathbb{C}^{\mathrm{dln}}}$ and $\varepsilon R_{\mathbb{C}^{\mathrm{dln}}}$. The nilpotent matrix unit is $E=E_{12}$, the diagonal involution is $J=\operatorname{diag}(1,-1)$, and the swap is $S=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. The transpose is written $^{\mathsf T}$, and it is taken in the basis $(1,\varepsilon)$.

## The Frame

**Definition.** The **matrix of** $Q$ is

$$
\mathsf{M}_2(Q)=qI_2+q'E,\qquad E=\begin{pmatrix}0&1\\ 0&0\end{pmatrix},\qquad E^{2}=0,
$$

that is $\mathsf{M}_2=\rho_E$ in the notation of the classification theorem, with $E$ the nilpotent Jordan block of size two.

**The entries, and how to read them.** Two parameters for four entries: the diagonal entry is the real part and is written twice, the upper entry is the infinitesimal part, and the lower entry is zero. The basis that produces the upper shape is $(\varepsilon,1)$, because $L_Q(\varepsilon)=q\varepsilon$ and $L_Q(1)=Q$, so the two columns in that basis are $(q,0)$ and $(q',q)$. In the natural basis $(1,\varepsilon)$ the same matrix of multiplication is the transpose

$$
\begin{pmatrix}q&0\\ q'&q\end{pmatrix}=S\,\mathsf{M}_2(Q)\,S,\qquad S=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},
$$

the reason being that reversing the order of a basis and transposing a matrix are the same operation. Equivalently, with a dual number written as the row $(a,b)$ of its coordinates, $(a,b)\mathsf{M}_2(Q)=(aq,aq'+bq)$ is the row of coordinates of $AQ$. The upper convention is used because it makes the maximal ideal the strictly upper corner and the flag the standard one; and it is $\rho_E$ of the classification, so it is a representation and not merely a transpose.

**The injectivity.** The map is injective by inspection, since $q$ is the diagonal entry and $q'$ the upper one; it is $R$-linear by construction and unital, with $\mathsf{M}_2(1)=I_2$ and $\mathsf{M}_2(\varepsilon)=E$.

**The homomorphism is not an accident of the shape.** The classification of the representations of $\mathbb{C}^{\mathrm{dln}}_R$ says that the representations are the pairs $(V,E)$ with $E^{2}=0$, through the formula

$$
\rho_E(q+\varepsilon q')=q\,\mathrm{id}_V+q'E,
$$

and that the formula is multiplicative precisely because $E^{2}=0$. So the model is $\rho_E$ for $E$ a rank-one nilpotent, and its multiplicativity is a case of a theorem about square-zero endomorphisms and not a computation about this shape. The computation is written out in the section on the product, and it is short, but the general reason is the classification.

**The flag.** The matrix $E$ satisfies $Ee_2=e_1$ and $Ee_1=0$, so the line $\langle e_1\rangle$ is invariant and is the image of $E$ and its kernel at once. A matrix fixes the flag $0\subset\langle e_1\rangle\subset R^{2}$ exactly when it is upper triangular, and the image is the subalgebra of the upper triangular matrices cut out by the single further equation $a=d$:

$$
\mathsf{M}_2(\mathbb{C}^{\mathrm{dln}}_R)=\left\{\begin{pmatrix}a&b\\ c&d\end{pmatrix}:c=0,\ a=d\right\}.
$$

The upper triangular matrices form the **parabolic** subalgebra of the flag, of dimension three; the image is a hyperplane in it, the hyperplane where the two graded pieces are acted on by the same scalar. This is the precise sense in which the model is not the full stabiliser of the flag: the stabiliser is the three-dimensional parabolic, and the algebra is the subalgebra of it whose two graded actions agree.

**The two conventions.** The transposed assignment $Q\mapsto\mathsf{M}_2(Q)^{\mathsf T}$ is the representation $\rho_{E_{21}}$, with the nilpotent in the lower corner, and it is also a homomorphism, since $E_{21}^{2}=0$. The two representations are equivalent, the intertwiner being the swap:

$$
S\,\mathsf{M}_2(Q)\,S=\mathsf{M}_2(Q)^{\mathsf T},\qquad S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad S^{2}=I_2 .
$$

So the regular representation of the companion articles, written in the lower corner, and the model of this article are one representation in two bases. What the transpose does *not* do is stay inside the image: it exchanges the two conventions, and this is the fact behind the failure of the triple coincidence of the adjugate section.

**The uniqueness.** Every faithful two-dimensional representation of $\mathbb{C}^{\mathrm{dln}}_K$ over a field is $\rho_E$ with $E$ a rank-one square-zero endomorphism, and all rank-one nilpotents of $M_2(K)$ are conjugate. So there is one model up to conjugacy, and the choice of corner is a choice of basis and not a second model. The category therefore has no family of models, in contrast to the quaternion category, where two inequivalent ones were needed.

**The membership test.** A matrix $M=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ is in the image exactly when $c=0$ and $a=d$: two linear equations, equivalently $M=aI_2+bE$. The test is **linear**, and its solution set is a linear subspace of dimension two. In the quaternion and split-quaternion categories the corresponding test was determinantal, a rank-one condition on a coefficient array; here it is a pair of equations, and the difference is the commutativity of the algebra.

**The centraliser.** A matrix $A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ commutes with $E$ exactly when $AE=EA$, that is when $c=0$ and $a=d$. So

$$
C\bigl(\mathsf{M}_2(\mathbb{C}^{\mathrm{dln}}_R)\bigr)=\mathsf{M}_2(\mathbb{C}^{\mathrm{dln}}_R),
$$

and the image is a **maximal commutative subalgebra** of $M_2(R)$: every matrix commuting with it lies in it, so no larger commutative subalgebra contains it. This is the same conclusion as in the complex category, and it is reached by the same computation, but the algebra it describes is now local rather than a field.

## The Left and the Right Matrices

**The two families coincide.** The algebra is commutative, so $L_Q=R_Q$ for every $Q$, and the two slots of the general theory hold one family:

$$
L_Q(X)=QX=XQ=R_Q(X),\qquad \dim_R L(\mathbb{C}^{\mathrm{dln}}_R)=2 .
$$

There is one copy of the algebra in the ambient, of dimension two, no anti-homomorphism, and no signed or conjugate transpose relating two families. The slot where those identities sit in the quaternion category is filled by the trivial statement $QX=XQ$.

**The regular module is not simple.** This is where the category differs from the field and matrix-algebra categories of the block: its regular module is neither simple nor a sum of simples. The invariant subspaces of the carrier under $L$ are the ideals of the algebra, and over a field they are

$$
0\ \subset\ \mathrm{M}\ \subset\ \mathbb{C}^{\mathrm{dln}}_K ,
$$

three in number, one for each element of the chain. So the regular representation is **reducible and indecomposable**: it has a composition series of length two, both factors are the residue field $K$ with the same action, and the series does not split, because a splitting would be a nontrivial idempotent and there is none. The classical name for this object is the **non-split extension** of the residue field by itself, and the classification article computes its class as the generator of $\operatorname{Ext}^{1}$.

**The reading.** In the complex category the regular module was simple, since a field has no proper nonzero ideal, and the matrix was conformal with no distinguished subspace. In the split category the module was a sum of two simple modules, and the matrix was diagonalisable. Here the module is a single non-split extension, and the matrix is a single Jordan block once the scalar part is removed. Reducible and not decomposable: the phrase is the exact description of the triangular shape.

**The double centraliser, in its degenerate form.** The endomorphisms of the regular module are the right multiplications, so

$$
\operatorname{End}_{\mathbb{C}^{\mathrm{dln}}_R}\bigl(\mathbb{C}^{\mathrm{dln}}_R\bigr)\cong\mathbb{C}^{\mathrm{dln}}_R,
$$

the two roles fall on one algebra, and the theorem holds trivially. The degenerate form is the same as in the complex category, but the reason is different: there the algebra was a field, here it is commutative and local. In both cases the map $A\otimes A^{\mathrm{opp}}\to\operatorname{End}_R(A)$ collapses to the multiplication, because the algebra is not central simple; the difference is that here the collapsed image is not semisimple.

**The kernel and the image.** For the left multiplication by $Q$,

$$
\ker L_Q=\{X:QX=0\},\qquad \operatorname{im}L_Q=Q\mathbb{C}^{\mathrm{dln}}_R ,
$$

and the two depend on the stratum:

| $Q$ | $\ker L_Q$ | $\operatorname{im}L_Q$ | $\operatorname{rank}L_Q$ |
|---|---|---|---|
| $q\neq0$ | $0$ | $\mathbb{C}^{\mathrm{dln}}_R$ | $2$ |
| $q=0$, $q'\neq0$ | $\mathrm{M}$ | $\mathrm{M}$ | $1$ |
| $Q=0$ | $\mathbb{C}^{\mathrm{dln}}_R$ | $0$ | $0$ |

For a nilpotent parameter the kernel and the image are the *same* line, which is the statement that $L_\varepsilon$ is a single Jordan block of size two. Over $\mathbb{R}$ the rank drops on the maximal ideal minus the origin, which is a line, so the singular set of the family is one-dimensional and not a pair of lines as in the split category and not empty as in the complex one.

**What the collapse costs.** With one copy of the algebra, the two-sided operator of the general theory is the multiplication by the product, and the operator layer has only the degenerations to report; this is stated in the companion article. The model article needs the collapse for one reason: the collapse is *why* the image is a subspace of dimension two and not a cone, and the subspace is why the membership test is linear.

## The Product

**Theorem (multiplicativity).** For all $Q,P$,

$$
\mathsf{M}_2(Q)\mathsf{M}_2(P)=\mathsf{M}_2(QP).
$$

**Proof.** Entrywise,

$$
\begin{pmatrix}q&q'\\ 0&q\end{pmatrix}\begin{pmatrix}p&p'\\ 0&p\end{pmatrix}
=\begin{pmatrix}qp&qp'+q'p\\ 0&qp\end{pmatrix}
=\mathsf{M}_2(QP),
$$

and $QP=qp+\varepsilon(qp'+q'p)$ is the product in the algebra.

**The image.** It is closed under sums, products and scalars, contains $I_2$, and is two-dimensional. It is the **truncated polynomial algebra** $R[E]/(E^{2})$: every member is $qI_2+q'E$, the subalgebra generated by $E$ consists of the polynomials in $E$ of degree at most one, and the relation $E^{2}=0$ is the only relation.

**The powers.** Since $E^{2}=0$,

$$
\mathsf{M}_2(Q)^{n}=q^{n}I_2+nq^{n-1}q'E=\mathsf{M}_2(Q^{n}),
$$

for every $n\geq1$, and the formula is the binomial theorem with the second-order terms removed. Two readings follow. First, the powers of an element never leave the image, so the model is closed under the functional calculus of polynomials. Second, the nilpotent part of the power grows linearly in $n$ and never becomes scalar: the element $Q$ is nilpotent exactly when $q=0$, and then $\mathsf{M}_2(Q)^{2}=0$.

**The shears.** The matrices of the form $I_2+sE$ are unipotent, and they multiply additively in the parameter:

$$
(I_2+sE)(I_2+tE)=I_2+(s+t)E,\qquad (I_2+sE)^{-1}=I_2-sE .
$$

They form the subgroup $1+\mathrm{M}$, isomorphic to $(R,+)$, called the **shear group** in *Shears and Parabolic Rotations*. It is the kernel of the residue map and the only nonlinear distinguished subset of the image that is a group.

**The failure of semisimplicity.** Over a field the image has no idempotent but $0$ and $I_2$, as the section on the spectral projectors proves. Hence no submodule of the regular module has a complement, no member of the image is a sum of two nonzero orthogonal idempotents, and the algebra is not a product of fields. Every structural absence of this article is a corollary of this one: no Peirce frame, no corners, no diagonalisation, no projector formula, no splitting field.

## The Trace

**Theorem (the trace).** For every $Q$,

$$
\operatorname{tr}\mathsf{M}_2(Q)=2q=2\operatorname{Re}Q .
$$

**Proof.** The two diagonal entries are both $q$.

**The kernel of the trace is the radical.** Since $2$ is invertible, the trace vanishes exactly when the real part does:

$$
\operatorname{tr}\mathsf{M}_2(Q)=0\iff q=0\iff Q\in\mathrm{M}.
$$

So the traceless subspace of the image is the maximal ideal, of dimension one, and the trace is a nonzero linear functional whose kernel is the radical of the algebra. In the complex category the traceless subspace was the imaginary line, a complement of the scalars; here it is the ideal, and the difference is not one of shape but of object: the line is nilpotent, and it is the radical.

**The trace form.** The bilinear form $(Q,P)\mapsto\operatorname{tr}(\mathsf{M}_2(Q)\mathsf{M}_2(P))$ has

$$
\operatorname{tr}\bigl(\mathsf{M}_2(1)^{2}\bigr)=2,\qquad
\operatorname{tr}\bigl(\mathsf{M}_2(1)\mathsf{M}_2(\varepsilon)\bigr)=0,\qquad
\operatorname{tr}\bigl(\mathsf{M}_2(\varepsilon)^{2}\bigr)=\operatorname{tr}(E^{2})=0,
$$

so its Gram matrix in the basis $(1,\varepsilon)$ is

$$
G_{\operatorname{tr}}=\begin{pmatrix}2&0\\ 0&0\end{pmatrix},\qquad \operatorname{rank}1,
$$

and in coordinates

$$
\operatorname{tr}\bigl(\mathsf{M}_2(Q)\mathsf{M}_2(P)\bigr)=2qp .
$$

**The reading.** The trace form is **degenerate**, of rank one, and its radical is exactly the maximal ideal: $\operatorname{tr}(\mathsf{M}_2(Q)\mathsf{M}_2(\varepsilon))=0$ for every $Q$, while $\operatorname{tr}(\mathsf{M}_2(Q)^{2})=2q^{2}$ does not vanish for $Q\notin\mathrm{M}$. The three categories of the block now separate cleanly by their trace forms: $\operatorname{diag}(2,-2)$ of signature $(1,1)$ for the complex numbers, $\operatorname{diag}(2,2)$ positive definite for the split-complex numbers, and $\operatorname{diag}(2,0)$ degenerate for the dual numbers. The form is not a metric in this category; it is a functional in disguise, and the direction it does not see is the direction in which the algebra is not reduced.

## The Determinant

**Theorem (the determinant is the norm).** For every $Q$,

$$
\det\mathsf{M}_2(Q)=q^{2}=\langle Q\rangle .
$$

**Proof.** The determinant of a triangular matrix is the product of its diagonal entries, $q\cdot q$; equivalently, $\det(qI_2+q'E)=q^{2}\det(I_2+(q'/q)E)=q^{2}$ for $q\neq0$, and both sides vanish for $q=0$.

**The zero set is a line.** The determinant vanishes exactly on the maximal ideal,

$$
\det\mathsf{M}_2(Q)=0\iff q=0\iff Q\in\mathrm{M},
$$

and this is the sharpest comparison of the block. The zero set of the complex determinant is the single point $0$; of the split determinant, the pair of null lines $q=\pm q'$; of the dual determinant, the one line $\mathrm{M}$, counted twice. The determinant is a square, so the line is a double line, and this is the algebraic statement that the algebra is local with a square-zero maximal ideal.

**The sign is lost.** Over $\mathbb{R}$ the determinant is nonnegative everywhere, and the two half-planes $q>0$ and $q<0$ are indistinguishable by it. In the split category the sign of the determinant still carried information, splitting the units into the sheet where the norm is positive and the sheet where it is negative; here it carries none, and the separation of the two components is made by the sign of the real part, that is by the residue. So the determinant is not an orientation in this category, and the unit group has two components that the determinant does not see.

**The rank ladder.** The rank of the matrix takes the three values

$$
\operatorname{rank}\mathsf{M}_2(Q)=2\ (q\neq0),\qquad 1\ (q=0,\ q'\neq0),\qquad 0\ (Q=0),
$$

while the determinant vanishes on the last two strata. So the determinant does not see the nilpotent direction: it cannot distinguish a nonzero nilpotent from zero, and the invariant that can is the rank. This is the theme of the companion article, where the two ranks of the operator layer separate exactly on the maximal ideal.

**The criterion.** Over a commutative ring the determinant decides invertibility in the usual sense,

$$
\mathsf{M}_2(Q)\ \text{invertible}\iff \det\mathsf{M}_2(Q)\in R^{\times}\iff q\in R^{\times},
$$

and over a field this is $q\neq0$. So the model recovers the criterion of *Dual-Numbers Norm and Invertibility* from the matrix side, and it does so through a determinant that is a square; the square is harmless because a square is a unit exactly when its root is.

**The characteristic polynomial.** It is

$$
\chi_{\mathsf{M}_2(Q)}(t)=(t-q)^{2},
$$

of discriminant zero, so every element is spectrally degenerate and no element is spectrally regular. The two roots coincide, the eigenvalue $q$ is repeated, and the eigenspace is computed in the next section. The dual numbers are the only category of the block in which the spectral classification has one nonempty cell.

**The polar form.** The determinant is a quadratic form, and its polar form is recovered from the trace and the determinant by the identity for $2\times2$ matrices,

$$
B(Q,P)=\tfrac12\Bigl(\operatorname{tr}\mathsf{M}_2(Q)\operatorname{tr}\mathsf{M}_2(P)-\operatorname{tr}\bigl(\mathsf{M}_2(Q)\mathsf{M}_2(P)\bigr)\Bigr)=qp,
$$

of Gram matrix $\operatorname{diag}(1,0)$: the norm form is the square of the real coordinate, and its radical is again the maximal ideal.

## The Spectral Projectors

**The spectrum is a point.** By the criterion of the previous section, $\lambda$ is an eigenvalue exactly when $Q-\lambda$ is not invertible, that is exactly when $\lambda=q$. So

$$
\sigma(Q)=\{q\},
$$

and the spectral theory of the algebra has one point to work with.

**No nontrivial idempotent.** Let $Q^{2}=Q$. In coordinates,

$$
q^{2}=q,\qquad (2q-1)q'=0 .
$$

Over a field the first equation gives $q\in\{0,1\}$; the second, with $2$ invertible, gives $q'=0$ in both cases. So

$$
\{Q:Q^{2}=Q\}=\{0,1\},
$$

and the algebra has no idempotent but the two trivial ones. Hence there is no Peirce frame, no corner, no system of matrix units, and no decomposition of an element into parts supported on orthogonal idempotents. The Lagrange formula for a projector,

$$
\Pi_{\pm}=\frac{Q-\lambda_{\mp}}{\lambda_{\pm}-\lambda_{\mp}},
$$

has a vanishing denominator and no limit, because the two roots have coalesced; the formula is not merely inconvenient here, it has no value, and the object it would produce does not exist.

**No splitting field.** The absence is not repaired by extending scalars. For a field extension $L/K$, the algebra $\mathbb{C}^{\mathrm{dln}}_K\otimes_KL\cong L[\varepsilon]/(\varepsilon^{2})$ is again local with maximal ideal $(\varepsilon)$, and a local ring has no idempotent but $0$ and $1$. So there is no field over which the algebra splits, in contrast to the complex numbers, which split after one extension, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$, and to the split-complex numbers, which are split from the start. The dual algebra is the one category of the block whose Peirce frame does not exist over any field.

**What replaces the projectors: the Jordan decomposition.** The element is a scalar plus a nilpotent,

$$
Q=q\cdot1+\underbrace{q'\varepsilon}_{\in\,\mathrm{M}},\qquad (q'\varepsilon)^{2}=0,
$$

and the decomposition is unique, because the scalar part is the residue and the nilpotent part is the difference. This is the **Jordan decomposition** of $Q$, and it is the exact analogue of the spectral decomposition of the other categories: the semisimple part lies in the centre, where it is the image of the residue, and the nilpotent part lies in the radical. In the split category the same decomposition was the sum over the two idempotents; here the index set has one point and the second summand is a nilpotent instead of a projector.

**The quotient map is the spectral projection.** The map

$$
\pi:\mathbb{C}^{\mathrm{dln}}_R\longrightarrow R,\qquad \pi(q+\varepsilon q')=q,
$$

is a surjective homomorphism of $R$-algebras, split by the inclusion of the constants, and it is the spectral projection of the category: it sends $Q$ to its value at the one point of the spectrum. It is a projection of *algebras* and not an element of the algebra, and the difference is the whole content of the previous paragraph. In the matrix model it is the diagonal map

$$
\pi:\mathsf{M}_2(Q)\longmapsto qI_2 ,
$$

whose kernel is the strictly upper corner.

**The functional calculus.** For a polynomial $f$ with coefficients in $R$,

$$
f(Q)=f(q)+q'f'(q)\,\varepsilon,\qquad f\bigl(\mathsf{M}_2(Q)\bigr)=f(q)I_2+q'f'(q)E=\mathsf{M}_2\bigl(f(Q)\bigr),
$$

which is Taylor's formula at $q$ with the second-order term removed, the removal being exact because $\varepsilon^{2}=0$. The model therefore commutes with the functional calculus, and the calculus is a two-term formula: the pair $(f(q),q'f'(q))$ is the image of the pair $(q,q')$ under the derivative of $f$. For an analytic function the same display is the definition, the series truncating after the linear term. So the exponential, the logarithm and the powers of an element are computed by one derivative, and the model of $e^{Q}$ is $e^{q}\mathsf{M}_2(1+q'\varepsilon)$.

**The eigenspace is the radical.** For $Q$ with $q'\neq0$ the eigenspace of $q$ is

$$
E_q(Q)=\ker L_{Q-q}=\ker L_{q'\varepsilon}=\mathrm{M},
$$

of dimension one, and it is a nilpotent line: every vector in it is killed by a further application of $Q-q$. The generalised eigenspace is the whole algebra. So the spectral decomposition of the carrier exists as a decomposition of vector spaces, $\mathbb{C}^{\mathrm{dln}}_R=R_{\mathbb{C}^{\mathrm{dln}}}\oplus\mathrm{M}$, and it is **not** a decomposition of modules, the second summand being the only proper submodule and the first being a complement that no projector produces. This is the precise reason the matrix is triangular and not diagonal: the generalised eigenspaces exist, and the projections onto them are not given by multiplication by an element.

## The Adjugate and the Inverse

**Theorem (the adjugate is the conjugate).** For every $Q$,

$$
\operatorname{adj}\mathsf{M}_2(Q)=\begin{pmatrix}q&-q'\\ 0&q\end{pmatrix}=\mathsf{M}_2(\bar Q),
$$

and therefore, where $q$ is a unit,

$$
\mathsf{M}_2(Q)^{-1}=\frac{\mathsf{M}_2(\bar Q)}{\langle Q\rangle}=\mathsf{M}_2\!\left(\frac{\bar Q}{\langle Q\rangle}\right)
=\begin{pmatrix}q^{-1}&-q'q^{-2}\\ 0&q^{-1}\end{pmatrix}.
$$

**Proof.** The adjugate of $\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ is $\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}$, which for the display gives the matrix stated; the inverse is the adjugate divided by the determinant, and the determinant is $\langle Q\rangle$.

**The reading.** The formula is the complex formula $Q^{-1}=\bar Q/\langle Q\rangle$ with the degenerate norm in place of the definite one, and it holds over any commutative ring in which $q$ is a unit. The inverse of a shear is a shear of the opposite parameter, $I_2+sE$ inverted by $I_2-sE$, so the nilpotent direction never obstructs invertibility: the units are the matrices with a unit diagonal entry, and the unipotent subgroup is entirely inside them.

**The triple coincidence fails.** In the complex model three operations coincided, the adjugate, the transpose and the model of the conjugate. Here they separate:

$$
\operatorname{adj}\mathsf{M}_2(Q)=\mathsf{M}_2(\bar Q),\qquad
\mathsf{M}_2(Q)^{\mathsf T}=\begin{pmatrix}q&0\\ q'&q\end{pmatrix}\notin\mathsf{M}_2(\mathbb{C}^{\mathrm{dln}}_R)\ \ (q'\neq0).
$$

The adjugate is the conjugate and conjugation by $J=\operatorname{diag}(1,-1)$ is the conjugate,

$$
J\,\mathsf{M}_2(Q)\,J=\mathsf{M}_2(\bar Q),
$$

but the transpose is neither: it is the model of the *other* convention, $\rho_{E_{21}}(Q)$, and it leaves the image. The reason is structural. The transpose of an upper triangular matrix is lower triangular, so the image is not closed under transposition, and the analogous statement in the complex category held only because there the image was closed under transposition, every conformal matrix being normal.

**No conformality.** The consequence is that the members of the image are not similarities. Indeed

$$
\mathsf{M}_2(Q)^{\mathsf T}\mathsf{M}_2(Q)=\begin{pmatrix}q^{2}&qq'\\ qq'&q^{2}+q'^{2}\end{pmatrix}
=q^{2}I_2+\begin{pmatrix}0&qq'\\ qq'&q'^{2}\end{pmatrix},
$$

so the matrix is conformal exactly when $q'=0$, and then it is scalar. The only normal matrices in the image are the scalars. The complex and split categories were conformal everywhere; the dual category is conformal on a line, and elsewhere the member is a shear with unequal singular values. For example $\mathsf{M}_2(1+2\varepsilon)=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ has singular values $\sqrt2+1$ and $\sqrt2-1$, of product $1$, the determinant: the shear stretches one direction and compresses another, and it is not a rotation followed by a scale.

**The transpose as the convention exchange.** Although the transpose leaves the image, it does not leave the ambient, and the two images it exchanges are conjugate:

$$
S\,\mathsf{M}_2(\mathbb{C}^{\mathrm{dln}}_R)\,S=\mathsf{M}_2(\mathbb{C}^{\mathrm{dln}}_R)^{\mathsf T},
$$

the lower triangular Toeplitz subalgebra. So the ambient carries two copies of the algebra, related by the swap, both faithful, both triangular, and the transpose is the map between them. This is the one place in the block where the transpose plays the role of a *change of model* rather than of an involution, and it is the reason the operator article has to say which copy it is working in.

## The Norms

**Three forms.**

| form | definition | Gram matrix on $(1,\varepsilon)$ | rank | radical | multiplicative |
|---|---|---|---|---|---|
| determinant form | $\det\mathsf{M}_2(Q)=q^{2}$ | $\operatorname{diag}(1,0)$ | $1$ | $\mathrm{M}$ | yes |
| trace form | $\operatorname{tr}(\mathsf{M}_2(Q)\mathsf{M}_2(P))=2qp$ | $\operatorname{diag}(2,0)$ | $1$ | $\mathrm{M}$ | no |
| Frobenius form | $\operatorname{tr}(\mathsf{M}_2(Q)^{\mathsf T}\mathsf{M}_2(P))$ | $\operatorname{diag}(2,1)$ | $2$ | $0$ | no |
| polar form | $B(Q_1,Q_2)=q_1q_2$ | $\operatorname{diag}(1,0)$ | $1$ | $\mathrm{M}$ | — |

**The two degenerate forms share their radical.** The determinant form and the trace form differ by a factor two and by nothing else, and both are degenerate with the maximal ideal as radical. The inclusion is clear: if one of the two arguments lies in $\mathrm{M}$ then so does the product, and both $\operatorname{tr}$ and $\det$ vanish on $\mathrm{M}$, so $\mathrm{M}$ sits inside the radical of each form. The count closes it: the radicals have dimension $2-1=1$ and $\mathrm{M}$ has dimension one, so the inclusion is an equality. The forms therefore cannot separate the infinitesimal direction, and the defect of the algebra and the defect of its forms are the same one-dimensional fact.

**The Frobenius form is the only nondegenerate one.** On the image it is

$$
\lVert\mathsf{M}_2(Q)\rVert_F^{2}=2q^{2}+q'^{2},
$$

positive definite over $\mathbb{R}$, of Gram matrix $\operatorname{diag}(2,1)$, and on the whole ambient it is the standard inner product $\operatorname{tr}(A^{\mathsf T}B)$. It separates the infinitesimal direction, and it is not multiplicative, so it is a metric and not a norm of the algebra. The category therefore has once more the pattern of the block, one multiplicative degenerate form and one nondegenerate metric, with the roles exchanged: in the complex category the multiplicative form was the definite one and the metric the indefinite one.

**No indefinite form, and no Hermitian structure.** Over $\mathbb{R}$ the three forms are positive semidefinite; the indefinite forms of the complex and split categories have no analogue, because an indefinite form needs a direction of negative square and the algebra has no element with a negative norm. There is also no Hermitian structure of the quaternionic kind: the model is real, its only involution is the dual conjugation, and that conjugation is an automorphism of the algebra and an inner one in the ambient, so the Hermitian and anti-Hermitian parts of a matrix are the fixed and anti-fixed spaces of an inner involution and not of an antilinear one.

## The Subspaces

**The tabulation.** The entries are the real line $q'=0$, the maximal ideal $q=0$, the algebra, the parabolic of the flag, the ambient, the group of units $q\in R^{\times}$, the **norm-one set** $\{Q:\langle Q\rangle=1\}=\{q=\pm1\}$, the idempotents $Q^{2}=Q$ and the nilpotents $Q^{2}=0$, which coincide with the zero divisors over a field. In the matrix column, the conditions $c=0$ and $a=d$ refer to the entries of a general ambient matrix.

| subspace | algebra condition | matrix condition | dimension |
|---|---|---|---|
| real line $R_{\mathbb{C}^{\mathrm{dln}}}$ | $q'=0$ | $qI_2$, scalar | $1$ |
| maximal ideal $\mathrm{M}$ | $q=0$ | $q'E$, strictly upper | $1$ |
| the algebra | — | $c=0$, $a=d$ | $2$ |
| the parabolic of the flag | — | $c=0$ | $3$ |
| the ambient | — | — | $4$ |
| the units | $q\in R^{\times}$ | $\det\neq0$ | open and dense |
| the norm-one set | $q^{2}=1$ | $\pm I_2+q'E$ | $1$, two components |
| the idempotents | $Q^{2}=Q$ | $0$ and $I_2$ | $0$ |
| the nilpotents and zero divisors | $\mathrm{M}$ | $q'E$ | $1$ |

**The flag and the graded pieces.** The two distinguished lines are the two graded pieces of the flag $0\subset\mathrm{M}\subset\mathbb{C}^{\mathrm{dln}}_R$, and the algebra acts on each by the same scalar: this is the content of $a=d$. The associated graded object is $R\oplus R$ with trivial multiplication, so the model sees the two lines and cannot see the extension between them; the off-diagonal entry is exactly the extension class, and it is the only entry that is not visible in the graded picture. In the language of the previous sections: the trace sees the graded pieces and the determinant sees their product, and neither sees the entry that glues them.

**The two involutions.** The algebra has two involutions, the identity and the dual conjugation, and they produce the two subspaces of the table,

$$
\mathbb{C}^{\mathrm{dln}}_R=R_{\mathbb{C}^{\mathrm{dln}}}\oplus\mathrm{M},\qquad
\operatorname{Fix}(\bar\cdot)=R_{\mathbb{C}^{\mathrm{dln}}},\qquad \operatorname{Anti}(\bar\cdot)=\mathrm{M},
$$

the fixed space being the constants and the anti-fixed space the maximal ideal. The count is two, the same as for the complex and split categories and less than the six of the biquaternion algebra. The difference from the complex case is that here the anti-fixed space is an ideal, so the decomposition is not a decomposition into ideals: the constants are a complement and not a summand.

**The units.** The unit group is

$$
(\mathbb{C}^{\mathrm{dln}}_R)^{\times}\cong R^{\times}\times(R,+),
$$

the second factor being the shear group, and over $\mathbb{R}$ it is $\mathbb{R}^{\times}\times\mathbb{R}$: abelian, two-dimensional, with two contractible components and no compact part. The **norm-one set** is the kernel of the norm,

$$
H=\{Q:\langle Q\rangle=1\}=\{q=\pm1\}=\pm\,(1+\mathrm{M}),
$$

two affine lines, and it **is** a subgroup: the norm is multiplicative, so the set is closed under products and inverses, and it is the direct product $\{\pm1\}\times(R,+)$, the first factor a sign and the second the shear parameter, the action being trivial because the algebra is commutative. Its two components are two cosets of the shear group, each contractible, so the analogue of the circle of the complex category and of the hyperbola of the split category is here a pair of parallel lines: the picture of a degenerate conic, and of a group that has two components and no compact direction.

**The complement of the image.** The image is two-dimensional in a four-dimensional ambient, and a complement is

$$
\left\{\begin{pmatrix}a&0\\ b&-a\end{pmatrix}\right\}=\mathbb{R}\,\operatorname{diag}(1,-1)\oplus\mathbb{R}\,E_{21},
$$

spanned by the traceless diagonal line and the lower corner. The two-dimensional complement contains the swap, which exchanges the two conventions; the residue map $\operatorname{diag}(1,0)$; and the derivation of the algebra, which is $\operatorname{diag}(0,1)$ in the same coordinates and is the operator of the infinitesimal calculus. None of the three is a multiplication, and the operator article reads them as the operators the model contains and the family cannot produce.

## Summary

1. The matrix $\mathsf{M}_2(Q)=qI_2+q'E$ with $E=E_{12}$ and $E^{2}=0$ is the matrix of $L_Q$ in the reversed basis $(\varepsilon,1)$, equivalently the transpose of the matrix in the natural basis $(1,\varepsilon)$; $\mathsf{M}_2(Q)\mathsf{M}_2(P)=\mathsf{M}_2(QP)$, and the map is injective onto the upper-triangular Toeplitz matrices.
2. The model is the representation $\rho_E$ of the classification theorem, so its multiplicativity is a case of the theorem that every square-zero endomorphism gives a representation; the model is unique up to conjugacy, and the lower triangular convention is the equivalent representation $\rho_{E_{21}}$, related by the swap.
3. The carrier carries the flag $0\subset\langle e_1\rangle\subset R^{2}$; the image is the two-dimensional hyperplane inside the three-dimensional parabolic on which the two graded pieces are acted on by the same scalar, and the triangular shape is the visible form of the non-split extension.
4. The regular module is reducible and indecomposable, of composition length two, with the residue field twice; there is no idempotent but $0$ and $1$ in any field extension, so there is no Peirce frame and no splitting field.
5. The left and right multiplications coincide, the centraliser of the image is the image, and the image is a maximal commutative subalgebra of $M_2(R)$; the double centraliser theorem holds trivially, the algebra being commutative.
6. The trace is $2q$ and its kernel is the maximal ideal; the trace form is degenerate of rank one with radical $\mathrm{M}$, against the Lorentzian form of the complex category and the definite form of the split one.
7. The determinant is $q^{2}=\langle Q\rangle$, a square, multiplicative, whose zero set is the line $\mathrm{M}$ counted twice; the rank ladder is $2,1,0$ and the determinant does not see the nilpotent direction.
8. The characteristic polynomial is $(t-q)^{2}$, every element is spectrally degenerate, and the spectral decomposition is the Jordan decomposition $Q=q\cdot1+q'\varepsilon$, the projector being the quotient map and not an element.
9. The adjugate is the model of the conjugate and the inverse is $\mathsf{M}_2(\bar Q/\langle Q\rangle)$; the transpose is not in the image but is the model of the other convention, so the members of the image are not conformal except on the scalars.
10. The three forms are positive semidefinite, two degenerate with radical the maximal ideal and one, the Frobenius form, a positive definite metric; the distinguished subspaces are two, the constants and the maximal ideal, and the complement of the image contains the swap, the residue and the derivation.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathsf{M}_2$ | the triangular map $\mathbb{C}^{\mathrm{dln}}_R\to M_2(R)$ | this article |
| $E=E_{12}$ | the nilpotent matrix unit $\mathsf{M}_2(\varepsilon)$, $E^{2}=0$ | this article |
| $Q=q+\varepsilon q'$ | a dual number, with conjugate $\bar Q=q-\varepsilon q'$ | *Dual-Numbers Algebra* |
| $\langle Q\rangle=q^{2}$ | the norm, equal to $\det\mathsf{M}_2(Q)$ | *Dual-Numbers Norm and Invertibility* |
| $\mathrm{M}=(\varepsilon)$ | the maximal ideal, the nilpotent radical | *Dual-Numbers Ideals and the Maximal Ideal* |
| $R_{\mathbb{C}^{\mathrm{dln}}},\varepsilon R_{\mathbb{C}^{\mathrm{dln}}}$ | the constants and the infinitesimal line | *Dual-Number Subspaces* |
| $J=\operatorname{diag}(1,-1)$ | the involution realising the conjugate, $J\mathsf{M}_2(Q)J=\mathsf{M}_2(\bar Q)$ | this article |
| $S$ | the swap, $S\mathsf{M}_2(Q)S=\mathsf{M}_2(Q)^{\mathsf T}$ | this article |
| $\pi$ | the residue, the spectral projection $\mathsf{M}_2(Q)\mapsto qI_2$ | this article |
| $\rho_E$ | the representation $q\,\mathrm{id}+q'E$ of the classification | *Dual-Numbers Linear Representations* |
| $1+\mathrm{M}$ | the shear group $I_2+sE$, isomorphic to $(R,+)$ | *Shears and Parabolic Rotations* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the regular representation, the Peirce decomposition that a local algebra does not have, and the double centraliser theorem.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for local rings, the absence of idempotents, and the trivial extension of a ring by a bimodule.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for triangular Toeplitz matrices, the cofactor formula, and the rank of a product.
- F. R. Gantmacher, *The Theory of Matrices* (Chelsea, 1959), for Jordan blocks, the centraliser of a nongeneric matrix, and the calculus of a nilpotent.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives* (SIAM, 2008), for the algebra of the truncated Taylor expansion and its matrix model.
