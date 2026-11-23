# __The Six Generators and Their Commutators__

## Introduction

The Lorentz algebra has six generators and fifteen independent brackets. This article writes them, checks the table, extracts the structure constants, computes the invariant bilinear form and its inertia, and defines the quadratic Casimir. It closes with the question a reader will ask on seeing the table for the third time: why does the same table appear in every display?

The answer is that the table is a statement about the algebra and not about a representation. Every faithful representation reproduces it, and the differences between the displays are differences of basis, of dimension and of real form, never of bracket.

The article assumes *The Isomorphisms and Their Dimensions* for the traceless part and its dimensions, *Algebra and Element Conventions* for the star, and *The Two Actions of One Group: Adjoint and Congruence* for the congruence that the four-vector display uses. It hands the two-triple rewriting to *The Two Commuting Complex Triples* and the Casimir eigenvalues to *The Two Casimirs of the Lorentz Algebra*.

## The Generators as Elements of the Algebra

### The Three Rotations

$$
J_\imath=\tfrac12\vec e_\imath,\qquad k=x,y,z .
$$

Each is a pure vector with real coefficients, so each is anti-Hermitian, $J_\imath^{*}=-J_\imath$. As a rotor generator, $J_\imath$ exponentiates to the rotation of *The Group of Unit-Norm Biquaternions*,

$$
\exp(\theta_{\mathrm{axr}}J_{\vec u})=\cos\tfrac{\theta_{\mathrm{axr}}}{2}+\sin\tfrac{\theta_{\mathrm{axr}}}{2}\vec u ,
$$

and the factor $\tfrac12$ in the generator is the half-angle of the rotor, seen infinitesimally.

### The Three Boosts

$$
K_\imath=\tfrac12 i\vec e_\imath,\qquad k=x,y,z .
$$

Each is a pure vector with imaginary coefficients, so each is Hermitian, $K_\imath^{*}=K_\imath$. It exponentiates to the boost,

$$
\exp(\theta_{\mathrm{rpd}}K_{\vec u})=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}+\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u ,
$$

with the rapidity $\theta_{\mathrm{rpd}}$ and $\tanh\theta_{\mathrm{rpd}}=v/c$.

### The Two Kinds, in One Table

| | $J_\imath$ | $K_\imath$ |
|---|---|---|
| element | $\tfrac12\vec e_\imath$ | $\tfrac12 i\vec e_\imath$ |
| under the star | anti-Hermitian | Hermitian |
| sector | $\mathbb{B}_{\Phi}$ | $\mathbb{B}_{\Psi}$ |
| exponential is | a rotation, compact, periodic | a boost, non-compact, monotone |
| twice the scalar part of the square | $-\tfrac12$ | $+\tfrac12$ |

The last row is the infinitesimal form of the difference between a closed and an open direction, and it is the row that produces the inertia of the invariant form.

### Why These and Not Others

The six are a basis of the traceless part: three complex directions $\vec e_\imath$ read as six real directions $\vec e_\imath$ and $i\vec e_\imath$. The factors $\tfrac12$ are conventions that make the exponential formula free of factors of two; they do not affect the bracket's shape, only its numerical entries.

## The Commutator Table

### The Nine Brackets

Direct multiplication in the algebra gives, for cyclic $(i,j,k)=(x,y,z)$,

$$
[J_i,J_j]=J_\imath,\qquad [J_i,K_j]=K_\imath,\qquad [K_i,K_j]=-J_\imath .
$$

Written out in full, with the antisymmetry understood:

| | $J_x$ | $J_y$ | $J_z$ | $K_x$ | $K_y$ | $K_z$ |
|---|---|---|---|---|---|---|
| $J_x$ | $0$ | $J_z$ | $-J_y$ | $0$ | $K_z$ | $-K_y$ |
| $J_y$ | $-J_z$ | $0$ | $J_x$ | $-K_z$ | $0$ | $K_x$ |
| $J_z$ | $J_y$ | $-J_x$ | $0$ | $K_y$ | $-K_x$ | $0$ |
| $K_x$ | $0$ | $-K_z$ | $K_y$ | $0$ | $-J_z$ | $J_y$ |
| $K_y$ | $K_z$ | $0$ | $-K_x$ | $J_z$ | $0$ | $-J_x$ |
| $K_z$ | $-K_y$ | $K_x$ | $0$ | $-J_y$ | $J_x$ | $0$ |

### The Three Rows

The table has three blocks, and each block is a statement of its own.

- $[\mathfrak{k},\mathfrak{k}]\subset\mathfrak{k}$: the rotations close. They form a subalgebra, and the corresponding subgroup is the compact $SU(2)$.
- $[\mathfrak{k},\mathfrak{p}]\subset\mathfrak{p}$: the boost directions transform as a vector under the rotations. This is the statement that a rotated boost is a boost in the rotated direction, and it is why the boost manifold is a symmetric space.
- $[\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k}$: the boosts do not close, and their bracket is a rotation. The minus sign in the third row is the Lorentzian sign pattern; with a plus the algebra would be $\mathfrak{so}(4)$.

Here $\mathfrak{k}$ is the span of the $J$ and $\mathfrak{p}$ the span of the $K$; *Composition of Two Boosts: The Commutator Table and Non-Additivity* is the article that reads the third row physically.

### The Structure Constants

Write $[T_a,T_b]=f_{abc}T_c$ with $T_a$ running over $J_x,J_y,J_z,K_x,K_y,K_z$. The nonzero constants are

$$
f_{ij}{}^{k}=\epsilon_{\imath\jmath\ell},\qquad f_{i,j+3}{}^{k+3}=\epsilon_{\imath\jmath\ell},\qquad f_{i+3,j+3}{}^{k}=-\epsilon_{\imath\jmath\ell},
$$

with $\epsilon_{\imath\jmath\ell}$ the Levi-Civita symbol and all indices cyclic in $x,y,z$. Two properties follow at once and are used in the invariant-form computation:

- **Antisymmetry**, $f_{abc}=-f_{bac}$, which is the antisymmetry of the commutator.
- **The Jacobi identity**, which the table satisfies because it is a commutator table in an associative algebra. There is nothing to prove: any associator identity would be a theorem of the algebra, and the algebra is associative.

### The Verification

The table is checked by direct multiplication on all thirty-six ordered pairs, and the check is structural: the six generators are the traceless part of an associative algebra, so the table holds by construction. What a numerical check can catch is a *mis-transcription* — a wrong sign in one entry — and the check is done that way, on the $2\times2$ images, with exact arithmetic on the integer entries.

## Why the Table Is the Lorentz Table

### The Rotation Block

The first block is the rotation algebra: three generators with $[J_i,J_j]=\epsilon_{\imath\jmath\ell}J_\imath$, which is $\mathfrak{su}(2)$ up to the factor of $i$ that the anti-Hermitian convention absorbs. No other three-dimensional algebra has that table.

### The Boost Block

The second and third blocks say that the boosts are a three-dimensional vector space on which the rotations act by the vector representation, and that the bracket of two boosts is a rotation. Those two statements, with the sign of the third block, are the definition of $\mathfrak{so}(1,3)$ as the algebra of the Lorentz group.

### The Alternative That Fails

Had the third block read $[K_i,K_j]=+J_\imath$, the table would be the table of $\mathfrak{so}(4)$, the Euclidean rotation algebra of four dimensions. Both tables are tables of *real forms of the same complex algebra*, and the sign is what decides which real form. A reader who "fixes" the sign to remove the minus gets a compact group and a positive-definite metric, and no light cone.

### The Inertia Check, Done Independently

The identification is confirmed by the invariant form rather than by the table's shape. The form's inertia is $(3,3)$ for this table and $(6,0)$ for the version with the plus sign, and the two are distinguishable by a computation that does not use the identification at all.

## The Invariant Bilinear Form

### The Invariant Form

The simplest invariant form is read from the $2\times2$ image:

$$
\langle T_a,T_b\rangle_{\mathrm{tr}}:=\operatorname{Tr}\bigl(\mathsf{M}_2(T_a)\mathsf{M}_2(T_b)\bigr).
$$

Direct computation gives

$$
\langle J_i,J_j\rangle_{\mathrm{tr}}=-\tfrac12\delta_{ij},\qquad
\langle J_i,K_j\rangle_{\mathrm{tr}}=0,\qquad
\langle K_i,K_j\rangle_{\mathrm{tr}}=+\tfrac12\delta_{ij}.
$$

So the form is diagonal in this basis with three negative and three positive entries: inertia $(3,3)$. It is invariant because twice the scalar part of a product is invariant under the adjoint action, $2\,\mathrm{Sc}(\tilde U\tilde X\tilde U^{-1}\tilde Y)=2\,\mathrm{Sc}(\tilde X\tilde Y)$, which is the invariance computed in *The Two Actions of One Group: Adjoint and Congruence*.

### The Killing Form

The Killing form is

$$
B(T_a,T_b)=\operatorname{tr}\bigl(\mathrm{ad}_{T_a}\mathrm{ad}_{T_b}\bigr),
$$

with the trace taken in the eight-dimensional adjoint representation. Computing it from the structure constants of the previous section gives

$$
B(J_i,J_j)=-4\delta_{ij},\qquad B(J_i,K_j)=0,\qquad B(K_i,K_j)=+4\delta_{ij},
$$

a form proportional to the trace form, with the ratio $8$. Two forms on a simple algebra are proportional, and the factor $8$ is the ratio of the two normalisations. The determinant of the matrix of the form in this basis is

$$
(-4)^{3}(+4)^{3}=-4096,
$$

and its eigenvalues are $\pm4$, three of each. The form is non-degenerate and its inertia is $(3,3)$.

### What the Inertia Means

A non-degenerate form of inertia $(3,3)$ on a six-dimensional real Lie algebra is the inertia of $\mathfrak{so}(1,3)$ and of no other form in this family. The three negative directions are the rotations and the three positive ones the boosts, and the split is not a choice: it is the Cartan decomposition, computed from the form.

The physical statement is that the group's invariant form has a Lorentzian sign pattern because the algebra is the Lorentz algebra. The three compact directions are the ones that close, and the three non-compact ones are the ones that do not.

## The Quadratic Casimir

### The Definition

The quadratic Casimir of the algebra, in the anti-Hermitian convention of this block, is

$$
C=\tfrac12\bigl(\vec K^{2}-\vec J^{2}\bigr),
$$

where $\vec J^{2}=\sum_{\imath\in\{x,y,z\}} J_\imath J_\imath$ and $\vec K^{2}=\sum_{\imath\in\{x,y,z\}} K_\imath K_\imath$ are sums of products inside the universal enveloping algebra. A second, independent invariant exists and is written in *The Two Casimirs of the Lorentz Algebra*; this article needs only the first.

**Why the sign is what it is.** In the physicist's Hermitian convention the generators are $\mathcal{J}_\imath=iJ_\imath$ and $\mathcal{K}_\imath=iK_\imath$, and $\mathcal{J}^{2}-\mathcal{K}^{2}=(i)^{2}(\vec J^{2}-\vec K^{2})=\vec K^{2}-\vec J^{2}$. So the same Casimir is written

$$
C=\tfrac12\bigl(\mathcal{J}^{2}-\mathcal{K}^{2}\bigr)\quad\text{(Hermitian generators)}
=\tfrac12\bigl(\vec K^{2}-\vec J^{2}\bigr)\quad\text{(anti-Hermitian generators)} .
$$

A formula copied from a book that uses the other convention will be off by an overall sign, and the sign is a convention and not a result.

### The Eigenvalue on the Defining Representation

On the $2\times2$ image, $J_\imath=\tfrac12\mathsf{M}_2(\vec e_\imath)$ satisfies $J_\imath^{2}=-\tfrac14I_2$, so $\vec J^{2}=-\tfrac34I_2$; and $K_\imath^{2}=+\tfrac14I_2$, so $\vec K^{2}=+\tfrac34I_2$. Hence

$$
C=\tfrac12\bigl(\tfrac34+\tfrac34\bigr)I_2=\tfrac34 I_2 .
$$

The value $\tfrac34$ is $m(m+1)$ at $m=\tfrac12$, which is the statement that the defining representation is the $(\tfrac12,0)$ carrier of the block. *The Two Casimirs of the Lorentz Algebra* computes the same number and the second Casimir on the same carrier.

### What the Casimir Is For

A Casimir is constant on each irreducible representation, so it is the label of the representation and not a property of the element. The block uses it three times: to name the finite carriers, to separate $(\tfrac12,0)$ from $(0,\tfrac12)$, and to compare the Lorentz labels with the Poincaré labels of mass and spin. None of those uses appears here; this article only fixes the normalisation.

## Why the Same Table Appears in Every Display

### The Two-Dimensional Display

The $2\times2$ image of the generators is a pair of complex matrices per direction. The bracket of the images is the image of the bracket, because $\mathsf{M}_2$ is an algebra isomorphism, so the table holds there entry for entry.

### The Four-Dimensional Display

The congruence action of the group on the material sector $\mathbb{B}_{\Phi}$ is a real four-dimensional representation, and its derived representation carries the same table with real $4\times4$ matrices. The matrices are different, the constants are the same.

### The Eight-Dimensional Display

The adjoint action on the whole algebra is an eight-dimensional representation, and it carries the same table again, in an eight-dimensional matrix form. It is not irreducible — it is the six-dimensional adjoint plus two trivial central directions — but the table on the six directions is unchanged.

### The Invariance Argument

The reason is one sentence long and worth stating precisely.

**Every faithful representation of a Lie algebra is a homomorphism of Lie algebras.** A homomorphism preserves brackets. So the table is carried to the table by every faithful representation, and the only things that can differ between displays are the size of the matrices, the field, the basis and the real form.

| display | carrier | dimension over $\mathbb{R}$ | what it is for |
|---|---|---|---|
| $2\times2$ image | $\mathbb{C}^{2}$ | $4$ real, $2$ complex | the defining module, spinors |
| congruence | $\mathbb{B}_{\Phi}$ | $4$ | four-vectors, the interval |
| adjoint | $\mathbb{B}$ | $8$ | the algebra's own symmetry |

### The Corollary for This Block

A reader who meets the table in the four-vector display and again in the two-triple display and again in the Casimir computation is meeting one object three times. The differences between the articles are the differences between what each display is *for*, and the table is the one invariant that all of them share. That is why it is printed in full once, here, and cited afterwards.

## Summary

The six generators are $J_\imath=\tfrac12\vec e_\imath$, anti-Hermitian and compact, and $K_\imath=\tfrac12 i\vec e_\imath$, Hermitian and non-compact. Their brackets are $[J_i,J_j]=J_\imath$, $[J_i,K_j]=K_\imath$, $[K_i,K_j]=-J_\imath$ cyclically, with structure constants $\pm\epsilon_{\imath\jmath\ell}$. The three blocks say that the rotations close, that the boosts transform as a vector, and that two boosts bracket to a rotation with the sign that makes the algebra Lorentzian rather than Euclidean. The trace form is $-\tfrac12$ on rotations and $+\tfrac12$ on boosts; the Killing form is $-4$ and $+4$; both have inertia $(3,3)$ and the Killing form has determinant $-4096$. The quadratic Casimir is $\tfrac12(\vec K^{2}-\vec J^{2})$ in the anti-Hermitian convention, equal to $\tfrac12(\mathcal{J}^{2}-\mathcal{K}^{2})$ in the Hermitian one, with value $\tfrac34$ on the defining representation. The table is the same in every display because every faithful representation is a Lie algebra homomorphism, and a homomorphism preserves brackets.

## Summary of Notation

| symbol | meaning |
|---|---|
| $J_\imath=\tfrac12\vec e_\imath$ | the rotation generators, anti-Hermitian |
| $K_\imath=\tfrac12 i\vec e_\imath$ | the boost generators, Hermitian |
| $\mathfrak{k}$, $\mathfrak{p}$ | the spans of the $J$ and of the $K$ |
| $f_{abc}$ | the structure constants, $[T_a,T_b]=f_{abc}T_c$ |
| $\langle\cdot,\cdot\rangle_{\mathrm{tr}}$ | the trace form $\operatorname{Tr}(\mathsf{M}_2(T_a)\mathsf{M}_2(T_b))$ |
| $B$ | the Killing form |
| $C=\tfrac12(\vec K^{2}-\vec J^{2})$ | the quadratic Casimir in the anti-Hermitian convention |
| $\theta_{\mathrm{rpd}}$, $\theta_{\mathrm{axr}}$ | rapidity and rotation angle |

## Further Reading

- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978 — the Killing form, its inertia, and the Cartan decomposition read from it.
- B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015 — structure constants, the Jacobi identity and the Casimir element of the universal enveloping algebra.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §2.4 — the Lorentz generators, the commutators in the physicist's Hermitian convention, and the dictionary of signs.
- W. Greiner and B. Müller, *Quantum Mechanics: Symmetries*, 2nd ed., Springer, 1994 — the same table derived in the rotation-plus-boost form with every sign displayed.
- *Composition of Two Boosts: The Commutator Table and Non-Additivity* — the physical reading of the third block.
- *The Two Commuting Complex Triples* and *The Two Casimirs of the Lorentz Algebra* — the rewriting of this table in the complex basis and the invariants built from it.
