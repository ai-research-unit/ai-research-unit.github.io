# __$M_2(\mathbb{C})$ Reduced Representation__

## Introduction

**The model is the matrix of the multiplication, and it is symmetric because the algebra is commutative.** The reduced biquaternion algebra is
$$
\mathbb{B}^{\mathrm{red}}=\mathbb{C}[j]/(j^{2}-1),
$$
with $j$ central, of complex dimension two and real dimension four, and it is isomorphic to $\mathbb{C}\times\mathbb{C}$. Writing $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with the two entries in $\mathbb{C}$, the left multiplication on the complex basis $(1,j)$ is
$$
\mathsf M(\breve Q)=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},
$$
a **symmetric** matrix with two equal diagonal entries and two equal off-diagonal entries. The image is two-dimensional over $\mathbb{C}$ inside the four-dimensional $M_{2}(\mathbb{C})$, and four-dimensional over $\mathbb{R}$ inside the eight-dimensional $M_{2}(\mathbb{C})$ read as a real algebra.

**Two frames, one model.** In the idempotent basis $(\Pi_{+},\Pi_{-})$ the same element is the diagonal matrix $\operatorname{diag}(Q_{+},Q_{-})$, with
$$
Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown},\qquad Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown},
$$
the two idempotent coordinates. The two frames are related by one fixed change of basis, the matrix $P$, of determinant $-2$, and the relation is *the same for every element*: this is the matrix form of semisimplicity, and it is what the dual-number category of the block cannot have.

**What the model shows.** The symmetry is the commutativity. The simultaneous diagonalisation is the semisimplicity, and the two diagonal entries are the two eigenvalues, which are the two components under $\mathbb{B}^{\mathrm{red}}\cong\mathbb{C}\times\mathbb{C}$. The determinant is the reduced norm $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_{+}Q_{-}$, the multiplicative algebraic norm of the algebra and its invertibility criterion. The zero divisors are exactly the matrices of the image that drop rank to one, that is the elements with one vanishing idempotent coordinate, and they are **not nilpotent**: the algebra is reduced. The trace is twice the first complex coordinate and not the sum of the two eigenvalues over $\mathbb{C}$, which is a distinction the realification makes visible.

**The one structural singularity of the category.** The reduced biquaternion algebra is the only algebra of the block that is **semisimple and neither a field nor a full matrix algebra over a division ring**. The complex numbers are a field, the split-complex numbers are a product of two copies of $\mathbb{R}$, the dual numbers are local and not reduced, the quaternion and biquaternion algebras are full matrix algebras, and the split-biquaternions are a product of two quaternion algebras, which is a full matrix algebra over $\mathbb{R}$ in disguise. Here the algebra is a product of two copies of $\mathbb{C}$ and its model is two-dimensional inside a four-dimensional algebra: the model is faithful and not surjective, and the deficit is exactly the two off-diagonal directions of $M_{2}(\mathbb{C})$.

**The boundaries.** The algebra itself, its ideals, its Peirce decomposition, its zero divisors, its units and its four products are *Reduced Biquaternion Space*, *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*, *Zero Divisors of the Algebra of the Reduced Biquaternions*, *Norm and Invertibility in the Algebra of the Reduced Biquaternions* and *The Four Products, Their Forms and Their Algebraic Norms of the Reduced Biquaternions*; the spectral theory is *Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra* and *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*, whose matrix reading is the present article; the real quadruple is *The Four-Vector Element Representation of the Reduced Biquaternions*, and the realification of the model is a closing subsection of the frame; the maps are *$M_{2}(\mathbb{C})$ Reduced Representation : Operators*. The catalogue of the two-way dictionary between algebra objects and matrix objects is *Reduced Biquaternion Objects and their Matrix Correspondences*, and this article does not repeat it.

## The Frame

**The basis $(1,j)$ and the idempotent basis $(\Pi_{+},\Pi_{-})$ are the two frames, and one fixed matrix passes between them.**

**The complex basis.** The algebra is a free module of rank two over $\mathbb{C}$ on the basis $1,j$, with $j^{2}=1$ and $j$ central, so the multiplication is
$$
(Q_{\blacktriangle}+jQ_{\blacktriangledown})(P_{\blacktriangle}+jP_{\blacktriangledown})=(Q_{\blacktriangle}P_{\blacktriangle}+Q_{\blacktriangledown}P_{\blacktriangledown})+j(Q_{\blacktriangle}P_{\blacktriangledown}+Q_{\blacktriangledown}P_{\blacktriangle}).
$$
The real basis is $1,i,j,ij$, of four elements, and the element is written
$$
\breve Q=q_{0}+iq_{1}+jq_{2}+ijq_{3},\qquad Q_{\blacktriangle}=q_{0}+iq_{1},\quad Q_{\blacktriangledown}=q_{2}+iq_{3},
$$
with the four coefficients real.

**The images of the basis.** The left multiplication sends
$$
\mathsf M(1)=\mathrm I_{2},\qquad \mathsf M(i)=i\,\mathrm I_{2},\qquad \mathsf M(j)=\sigma_{1}=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad \mathsf M(ij)=i\,\sigma_{1}.
$$
So the model is generated by the identity and one involution, and $\sigma_{1}^{2}=\mathrm I_{2}$ is the matrix statement of $j^{2}=1$. The central unit $i$ acts as a scalar, which is the matrix statement of the centrality.

**The idempotents.** The two elements
$$
\Pi_{+}=\tfrac12(1+j),\qquad \Pi_{-}=\tfrac12(1-j)
$$
satisfy $\Pi_{\pm}^{2}=\Pi_{\pm}$, $\Pi_{+}\Pi_{-}=0$ and $\Pi_{+}+\Pi_{-}=1$. They are the images of the two factors of $\mathbb{B}^{\mathrm{red}}\cong\mathbb{C}\times\mathbb{C}$, and their matrices in the basis $(1,j)$ are
$$
\mathsf M(\Pi_{+})=\tfrac12\begin{pmatrix}1&1\\ 1&1\end{pmatrix},\qquad \mathsf M(\Pi_{-})=\tfrac12\begin{pmatrix}1&-1\\ -1&1\end{pmatrix},
$$
the two spectral projectors of the frame.

**The change of basis.** The matrix
$$
P=\begin{pmatrix}1&1\\ 1&-1\end{pmatrix},\qquad \det P=-2,\qquad P^{2}=2\,\mathrm I_{2},\qquad P^{-1}=\tfrac12P
$$
has the two columns $1+j$ and $1-j$, that is the unnormalised idempotents, and it diagonalises every matrix of the image at once:
$$
P^{-1}\mathsf M(\breve Q)P=\operatorname{diag}(Q_{+},Q_{-}).
$$
The determinant $-2$ is the index of the idempotent frame: the two unnormalised idempotents form a basis of determinant $-2$, and the normalised ones would give $\det=-\tfrac12$. The realification squares the determinant, and the induced change of the real quadruple has determinant $4$, which is the inverse of the $\tfrac14$ with which *Decompositions Along the Remarkable Subspaces of the Reduced Biquaternions* writes the passage the other way.

**The image.** The image is
$$
\mathsf M(\mathbb{B}^{\mathrm{red}})=\left\{\begin{pmatrix}a&b\\ b&a\end{pmatrix}:a,b\in\mathbb{C}\right\}=\mathbb{C}\,\mathrm I_{2}\oplus\mathbb{C}\,\sigma_{1},
$$
of complex dimension two and real dimension four. It is the **commutant of $\sigma_{1}$**: a matrix $\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ commutes with $\sigma_{1}$ exactly when $a=d$ and $b=c$, which are the two conditions of the image.

**The membership test.** A matrix of $M_{2}(\mathbb{C})$ belongs to the image exactly when
$$
a=d,\qquad b=c,
$$
two **linear** equations over $\mathbb{C}$, that is four real equations. The test is linear and not determinantal, and the contrast with the quaternion and biquaternion categories is the contrast between a subspace and a cone: there the model filled the ambient and its failure to be everything was a rank condition, here the model is a subspace and the rank condition describes the *singular* members inside it. The two equations say that the four entries carry two complex numbers and no more, which is the dimension count of the algebra.

**The centraliser and the double centraliser.** Since the image is the commutant of $\sigma_{1}$ and $\sigma_{1}$ has two distinct eigenvalues, the image is a **maximal commutative subalgebra** of $M_{2}(\mathbb{C})$: the matrices commuting with it are the polynomials in $\sigma_{1}$, and there are no others. The double centraliser theorem holds in its degenerate form,
$$
\operatorname{End}_{\mathbb{B}^{\mathrm{red}}}\bigl(\mathbb{B}^{\mathrm{red}}\bigr)\cong\mathbb{B}^{\mathrm{red}},
$$
because the algebra is commutative, so the left multiplications are all the endomorphisms of the regular module. The two roles fall on one algebra, as in the dual-number category, and for a different reason: there the algebra was local, here it is a product of two fields.

**The real model.** Over the real basis $1,i,j,ij$ the same operator is the $4\times4$ real matrix
$$
L_{\breve Q}=\begin{pmatrix}A_{+}&A_{-}\\ A_{-}&A_{+}\end{pmatrix},\qquad A_{+}=\begin{pmatrix}q_{0}&-q_{1}\\ q_{1}&q_{0}\end{pmatrix},\quad A_{-}=\begin{pmatrix}q_{2}&-q_{3}\\ q_{3}&q_{2}\end{pmatrix},
$$
which is the realification of the complex model: each complex entry becomes the real $2\times2$ block of the multiplication by that complex number. It is a **section and not a second model**: it is the same operator on the same space, read over $\mathbb{R}$, and it is the quadruple of *The Four-Vector Element Representation of the Reduced Biquaternions* in matrix form. Every statement below that mentions a real dimension refers to it.

## The Left and the Right Matrices

**The algebra is commutative, so the two families coincide, and the regular module is a sum of two simple modules.**

**The coincidence.** For every $\breve Q$,
$$
L_{\breve Q}=R_{\breve Q},\qquad \dim_{\mathbb{C}}L(\mathbb{B}^{\mathrm{red}})=2,\qquad L(\mathbb{B}^{\mathrm{red}})=\mathsf M(\mathbb{B}^{\mathrm{red}}),
$$
so the family of one-sided operators is the image itself, of complex dimension two, and there is no anti-homomorphism and no conjugate transpose relating two families. The slot that held a genuine second family in the quaternion category holds here the identity $L_{\breve Q}X=XL_{\breve Q}$.

**The regular module.** The invariant subspaces of the carrier under $L$ are the ideals of the algebra, and they are
$$
0\ \subset\ \mathbb{C}\Pi_{+}\ \subset\ \mathbb{B}^{\mathrm{red}},\qquad 0\ \subset\ \mathbb{C}\Pi_{-}\ \subset\ \mathbb{B}^{\mathrm{red}},\qquad \mathbb{B}^{\mathrm{red}}=\mathbb{C}\Pi_{+}\oplus\mathbb{C}\Pi_{-},
$$
with no others. So the regular module is **completely reducible**: it is the direct sum of two simple modules, each of complex dimension one, each annihilated by the other idempotent. The composition length is two, the two composition factors are the same field $\mathbb{C}$ with two different actions, and the series **splits**, by $\Pi_{+}+\Pi_{-}=1$. This is the exact opposite of the dual-number category, where the series did not split and the regular module was a non-split extension; and it is a refinement of the complex category, where the regular module was simple.

**The reading.** Reducible and decomposable: the phrase describes a diagonal matrix. The two summands are the two eigenvalues, the splitting is the Peirce frame, and the frame is canonical because the two idempotents are attached to the algebra and not to the element. That is why the diagonal form of this category is a theorem about the *frame* and not about each element.

**The kernel and the image.** For the left multiplication by $\breve Q$,

| $\breve Q$ | $\ker L_{\breve Q}$ | $\operatorname{im}L_{\breve Q}$ | $\operatorname{rank}$ |
|---|---|---|---|
| a unit, $Q_{+}\neq0$ and $Q_{-}\neq0$ | $0$ | $\mathbb{B}^{\mathrm{red}}$ | $2$ |
| on $\mathbb{C}\Pi_{+}$, $\breve Q\neq0$ | $\mathbb{C}\Pi_{-}$ | $\mathbb{C}\Pi_{+}$ | $1$ |
| on $\mathbb{C}\Pi_{-}$, $\breve Q\neq0$ | $\mathbb{C}\Pi_{+}$ | $\mathbb{C}\Pi_{-}$ | $1$ |
| $0$ | $\mathbb{B}^{\mathrm{red}}$ | $0$ | $0$ |

The kernel of a zero divisor is the *other* idempotent line and the image is its own line: the two are different subspaces, which is the matrix statement that the operator is a scaled projector and not a nilpotent. In the dual-number category the kernel and the image of a nilpotent were the same line; here they are complementary, and the complement is the frame.

**The two-sided operator.** For a pair of elements,
$$
L_{\breve Q}R_{\breve P}(\breve X)=\breve Q\breve X\breve P=\breve Q\breve P\,\breve X=L_{\breve Q\breve P}(\breve X),
$$
so the pair collapses to the product, as in every commutative category of the block. The operators article computes the fibre of that collapse and the length; here the only fact needed is that the envelope $\mathbb{B}^{\mathrm{red}}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{red}}$ acts through the multiplication, with a two-dimensional image.

**The automorphisms and the derivations.** The algebra has no nonzero derivation, and its $\mathbb{C}$-algebra automorphisms are the identity and the tessarine sign; both facts are proved in *The Multiplication Operators of the Algebra of the Reduced Biquaternions*, and they read in the model as follows. An automorphism of the image that is inner in $M_{2}(\mathbb{C})$ is a conjugation by a unit of the image, and the image is commutative, so every such conjugation is the identity; the tessarine sign is therefore **outer** in the algebra and is realised by the conjugation with $J=\operatorname{diag}(1,-1)$, which is not in the image.

## The Product

**The model is multiplicative, and the powers and the functional calculus are the diagonal formulas read in the basis $(1,j)$.**

**Theorem (multiplicativity).** For all $\breve Q,\breve P$,
$$
\mathsf M(\breve Q)\mathsf M(\breve P)=\mathsf M(\breve Q\breve P),
$$
in the block form
$$
\begin{pmatrix}A&B\\ B&A\end{pmatrix}\begin{pmatrix}C&D\\ D&C\end{pmatrix}=\begin{pmatrix}AC+BD&AD+BC\\ AD+BC&AC+BD\end{pmatrix}.
$$

*Proof.* The two diagonal entries of the product are $AC+BD$ and the two off-diagonal entries are $AD+BC$, which is the multiplication rule of the algebra read in its two coordinates. The map is injective because the first column is the element, and it sends $1$ to the identity, so it is a faithful representation.

**The powers.** In the idempotent basis the matrix is diagonal, so
$$
\mathsf M(\breve Q)^{n}=\operatorname{diag}(Q_{+}^{n},Q_{-}^{n})=\frac{Q_{+}^{n}+Q_{-}^{n}}{2}\,\mathrm I_{2}+\frac{Q_{+}^{n}-Q_{-}^{n}}{2}\,\sigma_{1},
$$
and the second display is the binomial expansion of $(Q_{\blacktriangle}+jQ_{\blacktriangledown})^{n}$ with the even and the odd powers of $j$ collected, $j^{2k}=1$ and $j^{2k+1}=j$. The formula has no nilpotent correction term, in contrast with the dual numbers, where the $n$-th power carried the term $nq^{n-1}q'\varepsilon$: the difference is that $j^{2}=+1$ and $\varepsilon^{2}=0$.

**The functional calculus.** For a polynomial, or an analytic function $f$ on a neighbourhood of the two eigenvalues,
$$
f\bigl(\mathsf M(\breve Q)\bigr)=\operatorname{diag}\bigl(f(Q_{+}),f(Q_{-})\bigr),\qquad f(\breve Q)=f(Q_{+})\Pi_{+}+f(Q_{-})\Pi_{-},
$$
so the calculus is the evaluation at the two idempotent coordinates and nothing else. It is a two-term formula with no derivative term, because the algebra is semisimple; in the dual-number category the same formula needed the derivative $q'f'(q)$, and the presence or the absence of that term is the sharpest single distinction between the two categories.

**The idempotents.** An element of the image satisfies $\breve Q^{2}=\breve Q$ exactly when $Q_{+}^{2}=Q_{+}$ and $Q_{-}^{2}=Q_{-}$, that is when each coordinate is $0$ or $1$. There are therefore **four** idempotents,
$$
0,\qquad 1,\qquad \Pi_{+},\qquad \Pi_{-},
$$
the four diagonal matrices $\operatorname{diag}(0,0)$, $\operatorname{diag}(1,1)$, $\operatorname{diag}(1,0)$, $\operatorname{diag}(0,1)$ of the frame. Two of them are central, $\Pi_{\pm}$, and two are the trivial corners of the algebra. This is a genuine Peirce frame of order two, with two central idempotents and with **no off-diagonal matrix unit**: the algebra has no element $E_{+-}$ with $E_{+-}^{2}=0$ and $\Pi_{+}E_{+-}=E_{+-}$, because the two simple components are fields and a field has no nilpotent.

**The nilpotents.** The image contains no nilpotent but zero: $Q_{+}=Q_{-}=0$ forces $\breve Q=0$. So the algebra is reduced, and the whole nilpotent apparatus of the dual-number category — the square-zero maximal ideal, the shear group, the Jordan block, the derivation — has no analogue here. The zero divisors exist, and they are semisimple: a zero divisor of this algebra is a scaled rank-one projector, not a nilpotent.

**The image as a closed set.** The image is closed under sums, products and complex scalars, contains the identity, and is the algebra $\mathbb{C}[\sigma_{1}]$ of the polynomials in one involution. It is the **group algebra** of $\mathbb{Z}_{2}$ over $\mathbb{C}$, which is the coordinate-free name of $\mathbb{C}\times\mathbb{C}$, and the frame $P$ is its Fourier transform: the diagonalising matrix is the discrete Fourier transform of the group of order two, and the two idempotent coordinates are the two Fourier coefficients. Nothing in the matrix theory needs the group language, and it explains why the frame is fixed and why the two eigenvalues are the two characters.

## The Trace

**The trace is twice the first complex coordinate, and the trace form is nondegenerate of complex rank two.**

**Theorem (the trace).** For every $\breve Q$,
$$
\operatorname{tr}\mathsf M(\breve Q)=2Q_{\blacktriangle},\qquad \operatorname{tr}L_{\breve Q}=4q_{0},
$$
in the complex and in the real model.

*Proof.* The two diagonal entries of the complex matrix are both $Q_{\blacktriangle}$; the real matrix takes $2q_{0}$ from each of the two diagonal blocks $A_{+}$, and the block $A_{-}$ is off the diagonal, so the total is $4q_{0}$.

**Why the two differ by the realification and not by a factor of two alone.** The complex trace is $2Q_{\blacktriangle}$, a complex number, whose real part is $2q_{0}$ and whose imaginary part is $2q_{1}$. The real trace is $4q_{0}$: twice the real part, and nothing about $q_{1}$. So the real trace is the complex trace **plus its conjugate**,
$$
\operatorname{tr}L_{\breve Q}=\operatorname{tr}\mathsf M(\breve Q)+\overline{\operatorname{tr}\mathsf M(\breve Q)}=4q_{0},
$$
which is the general rule for the realification of a complex-linear operator, and it is the same rule that produced the trace $4q_{\blacktriangle}$ in the split-complex and dual categories with a real base field.

**The kernel of the trace.** The trace vanishes exactly when $Q_{\blacktriangle}=0$, that is on the complex line $\mathbb{C}j$, of real dimension two. This is **not** an ideal: the product of two elements of $\mathbb{C}j$ lies in $\mathbb{C}$, so the trace of a product of two traceless elements need not vanish. The traceless subspace is a complement of the scalar line and not a radical, and that is the structural difference from the dual-number category, where the traceless line was the maximal ideal.

**The trace form.** The bilinear form $(\breve Q,\breve P)\mapsto\operatorname{tr}(\mathsf M(\breve Q)\mathsf M(\breve P))$ has
$$
\operatorname{tr}\bigl(\mathsf M(\breve Q)\mathsf M(\breve P)\bigr)=2(Q_{\blacktriangle}P_{\blacktriangle}+Q_{\blacktriangledown}P_{\blacktriangledown}),
$$
so its Gram matrix in the complex basis $(1,j)$ is
$$
G_{\operatorname{tr}}=2\,\mathrm I_{2},\qquad \det G_{\operatorname{tr}}=4\neq0,
$$
and the form is **nondegenerate**, of complex rank two and real signature $(2,2)$ after the realification. In the idempotent basis the same form is
$$
\operatorname{tr}\bigl(\mathsf M(\breve Q)\mathsf M(\breve P)\bigr)=Q_{+}P_{+}+Q_{-}P_{-},
$$
because the trace of a product of diagonal matrices is the sum of the products of the entries.

**The reading.** Three categories, three trace forms: $\operatorname{diag}(2,-2)$ of signature $(1,1)$ for the complex numbers, $\operatorname{diag}(2,0)$ degenerate for the dual numbers, and $2\,\mathrm I_{2}$ nondegenerate for the reduced biquaternions. The form here *is* the form $\langle\cdot,\cdot\rangle$ of *The Four Products, Their Forms and Their Algebraic Norms of the Reduced Biquaternions*, read as a pairing of the model, because the trace of a product is the scalar part of the product; and its nondegeneracy is one more face of semisimplicity. The dual-number trace form was degenerate with the radical as its kernel; here the radical is zero.

## The Determinant

**The determinant is the reduced norm, a product of two linear forms in the idempotent coordinates, and its zero set is a pair of planes.**

**Theorem (the determinant).** For every $\breve Q$,
$$
\det\mathsf M(\breve Q)=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_{+}Q_{-}=\langle\breve Q\rangle_{\mathrm{ts}},
$$
multiplicative, and in the real model
$$
\det L_{\breve Q}=|Q_{+}|^{2}|Q_{-}|^{2}=\bigl|\langle\breve Q\rangle_{\mathrm{ts}}\bigr|^{2}.
$$

*Proof.* The determinant of $\begin{pmatrix}a&b\\ b&a\end{pmatrix}$ is $a^{2}-b^{2}$, and $Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown})$. For the real model, $L_{\breve Q}$ is carried by the block swap to $\operatorname{diag}(A_{+}+A_{-},A_{+}-A_{-})$, of determinant $|Q_{+}|^{2}|Q_{-}|^{2}$, since the real $2\times2$ block of the multiplication by a complex number $\zeta$ has determinant $|\zeta|^{2}$.

**The zero set.** The determinant vanishes exactly when one of the two idempotent coordinates vanishes,
$$
\det\mathsf M(\breve Q)=0\iff Q_{+}=0\ \text{or}\ Q_{-}=0,
$$
which is the union of two complex lines, each of real dimension two. In the basis $(1,j)$ the two are the lines $\mathbb{C}(1-j)$ and $\mathbb{C}(1+j)$; in the real quadruple they are the two planes $\{q_{0}=q_{2},\ q_{1}=q_{3}\}$ and $\{q_{0}=-q_{2},\ q_{1}=-q_{3}\}$, and the two meet only at the origin. The algebra is the union of its two maximal ideals, and the singular locus of the model is that union: this is what a product of two fields looks like as a determinantal variety, and it is the opposite of the quaternion category, where the zero set of the norm is a single point.

**The comparison of the block.** The complex determinant vanishes at one point; the split-complex one on two lines in a plane; the dual one on one line counted twice; the reduced biquaternion one on two planes in a four-space, meeting at the origin. The pattern is set by the number of factors: one field gives a point, two fields give two hyperplanes, and a local algebra gives a hyperplane counted with multiplicity. The reduced biquaternion case is the only one of the four in which the two branches are **transverse**, because the two idempotent coordinates are independent linear functions.

**The rank ladder.** The rank of the matrix takes the three values
$$
\operatorname{rank}\mathsf M(\breve Q)=\begin{cases}2&\text{on the units},\\ 1&\text{on the zero divisors},\\ 0&\text{at }0,\end{cases}
$$
and the realification doubles each value, so the real matrix has rank $4$, $2$ or $0$. The determinant is a complex number, so its vanishing is a condition of real codimension two and the singular set has real dimension two, against the real dimension four of the carrier.

**The sign is lost.** Over $\mathbb{R}$ the determinant of the realification is $|Q_{+}|^{2}|Q_{-}|^{2}\ge0$, so the real model cannot distinguish the two branches, and the sign of the complex determinant is invisible in it. The unit group is $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ in the frame, and the real determinant sees the two moduli and not the two arguments: the information it drops is the two circles of the torus.

## The Spectral Projectors

**Every element is diagonalised by the same matrix, and the two projectors are the central idempotents of the algebra.**

**The theorem.** For every $\breve Q$,
$$
P^{-1}\mathsf M(\breve Q)P=\operatorname{diag}(Q_{+},Q_{-})=\operatorname{diag}(\lambda_{+},\lambda_{-}),
$$
the two eigenvalues being $Q_{+}$ and $Q_{-}$, and the same $P$ serving every element. This is the **simultaneous diagonalisation** of a commutative family, available because the algebra is semisimple and commutative: the two eigenprojectors are the matrices
$$
\mathsf M(\Pi_{+})=\tfrac12\begin{pmatrix}1&1\\ 1&1\end{pmatrix},\qquad \mathsf M(\Pi_{-})=\tfrac12\begin{pmatrix}1&-1\\ -1&1\end{pmatrix},
$$
which do not depend on $\breve Q$.

**The spectral decomposition.** The spectral theorem of the category is three statements in one:
$$
\breve Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-},\qquad \Pi_{+}+\Pi_{-}=1,\qquad \Pi_{+}\Pi_{-}=0,
$$
and the matrix form is the diagonal matrix in the frame, with the two projectors as the coordinate matrices. The decomposition is the Peirce decomposition written with the eigenvalues in place of the coordinates, and it is **the same decomposition for every element**: only the two coefficients change.

**Lagrange and its degenerate locus.** The projector formula
$$
\Pi_{+}=\frac{\breve Q-Q_{-}}{Q_{+}-Q_{-}},\qquad \Pi_{-}=\frac{\breve Q-Q_{+}}{Q_{-}-Q_{+}}
$$
expresses the two projectors as polynomials in $\breve Q$, and it fails exactly when the two eigenvalues coincide, $Q_{+}=Q_{-}$, that is when $Q_{\blacktriangledown}=0$ and the element is a scalar. At that point the denominator vanishes and the two formulas have no limit. The failure is of the **formula** and not of the **object**: the two projectors are constants of the algebra and exist at every element, and the spectral decomposition of a scalar element is the trivial $1=1\cdot\Pi_{+}+1\cdot\Pi_{-}$. The dual-number category is the case where the object itself does not exist, and the comparison is worth stating: here the Lagrange formula degenerates on a line, there it degenerates everywhere, because there is no idempotent at all.

**The characteristic polynomial and the minimal polynomial.** The characteristic polynomial of the matrix is
$$
\chi(\lambda)=(\lambda-Q_{+})(\lambda-Q_{-})=\lambda^{2}-2Q_{\blacktriangle}\lambda+(Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}),
$$
whose coefficients are the trace and the determinant. By Cayley–Hamilton the matrix satisfies $\mathsf M(\breve Q)^{2}-2Q_{\blacktriangle}\mathsf M(\breve Q)+\langle\breve Q\rangle_{\mathrm{ts}}\,\mathrm I_{2}=0$, which is the binomial identity of the product section. The minimal polynomial is $\chi$ for every element with $Q_{\blacktriangledown}\neq0$ and the linear polynomial $\lambda-Q_{\blacktriangle}$ for the scalars; so the two eigenvalues are distinct exactly when the element is not scalar, and the element is nonderogatory exactly then. In the dual-number category the minimal polynomial was $(t-q)^{2}$ on the maximal ideal, because the single eigenvalue was repeated and the element was derogatory; here the derogatory locus is a line and not an open set.

**The zero-divisor case.** When one eigenvalue vanishes the rank drops to one, and the matrix is a scaled idempotent:
$$
\breve Q=Q_{+}\Pi_{+}\ \Longrightarrow\ \mathsf M(\breve Q)=Q_{+}\operatorname{diag}(1,0)\ \text{in the frame},
$$
of rank one and kernel the other idempotent line. So the singular members of the image are the two scaled idempotents, and the projection onto the rank-one stratum is the projection onto the two ideals.

**The spectral mapping.** For a function $f$ analytic on a neighbourhood of the two eigenvalues, $\operatorname{spec}f(\breve Q)=f(\operatorname{spec}\breve Q)=\{f(Q_{+}),f(Q_{-})\}$, and the two eigenprojectors are preserved: $f(\breve Q)$ has the same frame as $\breve Q$. So the calculus is a map of the algebra into itself that fixes the frame, and the frame is the faithful matrix expression of that fact.

## The Adjugate and the Inverse

**The adjugate is the model of the tessarine conjugate, and the inverse is that conjugate divided by the reduced norm.**

**Theorem (the adjugate).** For every $\breve Q$,
$$
\operatorname{adj}\mathsf M(\breve Q)=\begin{pmatrix}Q_{\blacktriangle}&-Q_{\blacktriangledown}\\ -Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}=\mathsf M(\breve Q_{\mathrm{ts}}),
$$
where $\breve Q_{\mathrm{ts}}=Q_{\blacktriangle}-jQ_{\blacktriangledown}$ is the tessarine conjugate. Hence, on the units,
$$
\mathsf M(\breve Q)^{-1}=\frac{\mathsf M(\breve Q_{\mathrm{ts}})}{\langle\breve Q\rangle_{\mathrm{ts}}}=\mathsf M\!\left(\frac{\breve Q_{\mathrm{ts}}}{\langle\breve Q\rangle_{\mathrm{ts}}}\right)=\mathsf M\bigl(\breve Q^{-1}\bigr).
$$

*Proof.* The adjugate of $\begin{pmatrix}a&b\\ b&a\end{pmatrix}$ is $\begin{pmatrix}a&-b\\ -b&a\end{pmatrix}$, which is the image of the element with the sign of the second coordinate reversed; the inverse is the adjugate divided by the determinant, and the quotient of the two displays is the inverse in the algebra, $Q_{+}^{-1}\Pi_{+}+Q_{-}^{-1}\Pi_{-}$.

**The reading.** The formula is the algebraic formula $\breve Q^{-1}=\breve Q_{\mathrm{ts}}/\langle\breve Q\rangle_{\mathrm{ts}}$ and it holds at every unit. In the idempotent basis it is $\operatorname{diag}(Q_{+}^{-1},Q_{-}^{-1})$ and the adjugate there is $\operatorname{diag}(Q_{-},Q_{+})$, the **swap** of the two entries: the conjugate exchanges the two idempotent coordinates, $\overline{Q}_{+}=Q_{-}$ and $\overline{Q}_{-}=Q_{+}$, which is the matrix form of the fact that the tessarine sign exchanges $\Pi_{+}$ and $\Pi_{-}$.

**The unit criterion.** The matrix is invertible exactly when $Q_{+}\neq0$ and $Q_{-}\neq0$, that is on the complement of the two planes of the determinant; in the coordinates $(1,j)$ the criterion is $Q_{\blacktriangle}\neq\pm Q_{\blacktriangledown}$. The group of units is therefore
$$
\mathsf M\bigl({\mathbb{B}^{\mathrm{red}}}^{\times}\bigr)\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times},
$$
of complex dimension two and real dimension four, and it is not the whole $GL_{2}(\mathbb{C})$, which has complex dimension four: the inclusion is proper, of codimension two, exactly as the inclusion of the model in the ambient is.

**The three operations.** In the complex category three operations coincided: the adjugate, the transpose and the model of the conjugate. Here they separate, and the separation has a shape the other categories do not have.
$$
\operatorname{adj}\mathsf M(\breve Q)=\mathsf M(\breve Q_{\mathrm{ts}}),\qquad \mathsf M(\breve Q)^{\mathsf T}=\mathsf M(\breve Q),\qquad \overline{\mathsf M(\breve Q)}=\mathsf M(\bar{\breve Q}).
$$
The **transpose is the identity on the image**, because every matrix of the image is symmetric; so the transpose realises no involution of the algebra and the model is closed under it pointwise. The **entrywise conjugate** is the model of the bar and is antilinear. The **adjugate** is the model of the tessarine sign, which is $\mathbb{C}$-linear.

**Why the adjugate realises the tessarine sign and not the bar.** The adjugate is a polynomial, with integer coefficients, in the entries of the matrix; so it is complex-analytic in $\breve Q$ and cannot implement a map that conjugates the coefficients. Of the three involutions of the algebra exactly one is $\mathbb{C}$-linear, the tessarine sign, and it is the only one the adjugate can produce. The bar and the star are conjugate-linear and are realised by the entrywise conjugation and by its composite with the diagonal conjugation.

**The diagonal conjugation.** With $J=\operatorname{diag}(1,-1)$ and the swap $S=\sigma_{1}$,
$$
J\,\mathsf M(\breve Q)\,J=\mathsf M(\breve Q_{\mathrm{ts}}),\qquad S\,\mathsf M(\breve Q)\,S=\mathsf M(\breve Q),
$$
so the $J$-conjugation realises the conjugate and the $S$-conjugation is trivial, the second because $S=\mathsf M(j)$ is a unit of the image and the image is commutative. The ambient therefore contains one involution that acts on the algebra as its conjugate and one that acts trivially, and the trivial one belongs to the algebra while the nontrivial one does not: precisely the reverse of the dual-number category, where the swap realised the conjugate and the diagonal was the convention exchange.

**Three conformalities, and only one of them is exact.** For the **indefinite** form $J=\operatorname{diag}(1,-1)$ the model is conformal at **every** element, with the determinant as the factor:
$$
\mathsf M(\breve Q)^{\mathsf T}J\,\mathsf M(\breve Q)=\bigl(\det\mathsf M(\breve Q)\bigr)J,
$$
an identity in the entries, because $J\mathsf M(\breve Q)J=\mathsf M(\breve Q_{\mathrm{ts}})$ and the algebra is commutative, so that $\mathsf M^{\mathsf T}J\mathsf M = \mathsf M J\mathsf M = \mathsf M_{\mathrm{ts}}\mathsf M$ and the off-diagonal blocks cancel. This is the exact analogue of the conformal identity of the complex category, with the indefinite form in place of the definite one.

For the **definite** form the identity fails, and
$$
\mathsf M(\breve Q)^{\mathsf T}\mathsf M(\breve Q)=\langle\breve Q\rangle\,\mathrm I_{2}+2Q_{\blacktriangle}Q_{\blacktriangledown}\,\sigma_{1},
$$
which is scalar exactly when $Q_{\blacktriangle}Q_{\blacktriangledown}=0$, that is on the union of the two coordinate lines $\mathbb{C}$ and $\mathbb{C}j$ and not at the scalars alone. For the **adjoint** the condition is different again,
$$
\mathsf M(\breve Q)^{\dagger}\mathsf M(\breve Q)\ \text{is scalar}\iff |Q_{+}|^{2}=|Q_{-}|^{2}\iff \operatorname{Re}\bigl(Q_{\blacktriangle}\bar Q_{\blacktriangledown}\bigr)=0,
$$
a real hypersurface of codimension one that contains the two lines.

So the three forms give three conformal loci — everything, two lines, and a hypersurface — and the exact one is the indefinite one. That is the shape the category takes in the projection of the ambient onto the conformal group: the family sits inside the conformal group of the split metric without exception, and inside the conformal group of the Euclidean metric only on two lines. The operators article uses the adjoint version for the sandwich and the $J$-version for the adjoint table.

## The Norms

**Four algebraic norms, four Gram matrices, and one positive definite form.**

| form | definition | Gram matrix on $1,i,j,ij$ | real signature | multiplicative |
|---|---|---|---|---|
| plain bilinear | $\langle\breve Q\rangle=Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2}$ | $\operatorname{diag}(1,-1,1,-1)$ | $(2,2)$ | no |
| tessarine bilinear | $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ | $\operatorname{diag}(1,-1,-1,1)$ | $(2,2)$ | yes |
| plain sesquilinear | $\langle\breve Q\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}$ | $\operatorname{diag}(1,1,-1,-1)$ | $(2,2)$ | no |
| tessarine sesquilinear | $\langle\breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}$ | $\mathrm I_{4}$ | $(4,0)$ | no |

**The determinant is the multiplicative one.** The tessarine bilinear norm is $Q_{+}Q_{-}$, so it is the determinant of the model and the criterion of invertibility, and the algebra has **one** multiplicative norm and not two: the plain norm $Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2}$ is not multiplicative, because the sign $j^{2}=+1$ enters the expansion of $Q^{2}$ with the wrong sign. In the commutative categories of the block the determinant is always the multiplicative norm, and the reduced biquaternion case is the one in which the plain norm and the multiplicative norm are different complex-valued quadratic forms.

**The positive definite one.** Only $\langle\breve Q\rangle_{\mathrm{ts}*}$ is positive definite, and it is the square of the Euclidean norm of the quadruple $(q_{0},q_{1},q_{2},q_{3})$. In the model it is the Frobenius form,
$$
\langle\breve Q\rangle_{\mathrm{ts}*}=\tfrac12\operatorname{tr}\bigl(\mathsf M(\breve Q)^{\dagger}\mathsf M(\breve Q)\bigr),
$$
and the factor $\tfrac12$ is the dimension of the carrier, which is the general normalisation of the Frobenius form on a model of rank two. The other three are indefinite of real signature $(2,2)$, and their three Gram matrices are the three ways of placing two minus signs among the four coordinates: the plain form keeps the signs of the real and the $j$ coefficients, the tessarine form flips the two imaginary ones, and the sesquilinear form flips the two $j$-ones.

**The four forms in the model.** The two bilinear forms are the traces of products and of $J$-conjugated products,
$$
\langle\breve Q,\breve P\rangle=\tfrac12\operatorname{tr}\bigl(\mathsf M(\breve Q)\mathsf M(\breve P)\bigr),\qquad \langle\breve Q,\breve P\rangle_{\mathrm{ts}}=\tfrac12\operatorname{tr}\bigl(J\mathsf M(\breve Q)J\mathsf M(\breve P)\bigr),
$$
and the two sesquilinear ones are the same two with the entrywise conjugation in the first slot,
$$
\langle\breve Q,\breve P\rangle_{*}=\tfrac12\operatorname{tr}\bigl(J\overline{\mathsf M(\breve Q)}J\mathsf M(\breve P)\bigr),\qquad \langle\breve Q,\breve P\rangle_{\mathrm{ts}*}=\tfrac12\operatorname{tr}\bigl(\overline{\mathsf M(\breve Q)}\mathsf M(\breve P)\bigr).
$$
So the four forms are the four slots of a table of two binary choices, the conjugation in the first slot present or absent and the $J$ present or absent. That is the same table as the four products of *The Four Products, Their Forms and Their Algebraic Norms of the Reduced Biquaternions*, read in the model, and it is the cleanest reading of the sentence that the four products are the four ways of placing a conjugation.

**The non-negative cone.** The tessarine sesquilinear norm is nonnegative and vanishes only at zero, so it defines an order: an element is **non-negative** when its two idempotent coordinates are non-negative reals, $Q_{+}\in[0,\infty)$ and $Q_{-}\in[0,\infty)$. In the model the order is the order of the diagonal matrices with nonnegative entries in the frame, so the non-negative cone is the **positive quadrant** of $\mathbb{R}^{2}$ read in the two idempotent coordinates, of real dimension two inside the four of the algebra. It is a genuine cone, convex and pointed, and it is the object the dual-number category does not have: there the analogous set was the half-line $q\ge0$, of dimension one and empty interior. The order is the coordinatewise order of the frame and not the order of the symmetric matrices by eigenvalues, and the two coincide only on the diagonal.

## The Subspaces

**The distinguished subspaces are block conditions, and there are four canonical splits and three involutions.**

| subspace | algebra condition | matrix condition | real dim |
|---|---|---|---|
| the scalar line $\mathbb{C}$ | $Q_{\blacktriangledown}=0$ | $b=c=0$, scalar | $2$ |
| the $j$-line $\mathbb{C}j$ | $Q_{\blacktriangle}=0$ | $a=d=0$, multiple of $\sigma_{1}$ | $2$ |
| the ideal $\mathbb{B}^{\mathrm{red}}\Pi_{+}$ | $Q_{-}=0$ | $\operatorname{diag}(\cdot,0)$ in the frame | $2$ |
| the ideal $\mathbb{B}^{\mathrm{red}}\Pi_{-}$ | $Q_{+}=0$ | $\operatorname{diag}(0,\cdot)$ in the frame | $2$ |
| the plane $\mathbb{R}\{1,j\}$ | $q_{1}=q_{3}=0$ | real matrices of the image | $2$ |
| the plane $\mathbb{R}\{1,ij\}$ | $q_{1}=q_{2}=0$ | $\begin{pmatrix}a&b\\ b&a\end{pmatrix}$ with $a,b$ real | $2$ |
| the units | $Q_{+}Q_{-}\neq0$ | $\det\neq0$ | open, dense |
| the zero divisors | $Q_{+}Q_{-}=0$, not $0$ | rank $1$ | $2$, two planes |
| the idempotents | $Q_{\pm}\in\{0,1\}$ | $0$, $\mathrm I_{2}$, $\operatorname{diag}(1,0)$, $\operatorname{diag}(0,1)$ | four points |
| the nilpotents | $Q_{+}=Q_{-}=0$ | $0$ | one point |

**The two decompositions.** The carrier splits in two canonical ways, and they are the same split:
$$
\mathbb{B}^{\mathrm{red}}=\mathbb{C}\oplus\mathbb{C}j=\mathbb{C}\Pi_{+}\oplus\mathbb{C}\Pi_{-},
$$
the first the split into scalar and $j$-part, the second the Peirce split into the two ideals. The two are exchanged by the Fourier matrix $P$, and only the second is a decomposition of the algebra as an algebra. This is the difference between a grading and a Peirce decomposition, and the category is the smallest example of the distinction in the block.

**The three involutions and their fixed spaces.** The algebra carries the bar, the tessarine sign and the star, and each fixes a real plane:
$$
\operatorname{Fix}(\bar\cdot)=\mathbb{R}\{1,j\},\qquad \operatorname{Fix}({}_{\mathrm{ts}})=\mathbb{C},\qquad \operatorname{Fix}({}^{*})=\mathbb{R}\{1,ij\},
$$
and the anti-fixed spaces are the three complementary planes. In the model the bar is the entrywise conjugation, the tessarine sign the conjugation by $J$, and the star their composite; the transpose fixes the image pointwise and adds no plane, so the model implements **three** of the four elements of the Klein group and implements the fourth trivially. The count of the distinguished real planes is three, against the six of the biquaternion category, which carries one for each involution and each anti-fixed space.

**The zero divisors as a determinantal variety.** The set $\{Q_{+}Q_{-}=0\}$ is the union of the two ideals, each a complex line and a real plane, and their intersection is the origin. So the singular locus is **reducible with two components**, and its projectivisation in the three-dimensional projective space of the real quadruple is two skew lines: the quadric of the split-complex category, lifted by the complex coefficients. The projective picture is the same two-line picture in each complex direction, and the model of the operator article uses it for the cone of the two-sided product.

**The two sandwiches.** Two sandwiches are worth naming because the operators article uses both. The plain sandwich is a left multiplication,
$$
\breve Q\breve X\breve Q=\breve Q^{2}\breve X=L_{\breve Q^{2}}(\breve X),
$$
and it carries no information beyond the square. The bar-sandwich is the **modulus square**,
$$
\breve Q\breve X\bar{\breve Q}=\operatorname{diag}\bigl(|Q_{+}|^{2},|Q_{-}|^{2}\bigr)\breve X\ \text{in the frame},
$$
which is a scalar operator only when the two moduli agree, and which is the operator behind the modulus–unit polar decomposition. The two are two slots of the table of the four products filled on both sides, and the second is the one that produces a cone of operators: its image is the quadrant $(|Q_{+}|^{2},|Q_{-}|^{2})$, of real dimension two.

**The units and the four sectors.** The unit group is $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ in the frame, of four contractible components distinguished by the signs of the two idempotent coordinates, and it retracts onto $T^{2}$; the four sectors of *The Four Sectors of the Reduced Biquaternion Algebra* are the four sign patterns, read in the frame as the four quadrants of $\mathbb{R}^{2}$ and in the model as the four diagonal forms with positive or negative real entries. This is the difference from the split-complex category, where the four sectors were four quadrants of a plane: here each sector is a product of two half-planes of a complex line.

## Summary

1. The model is $\mathsf M(\breve Q)=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}$, symmetric because the algebra is commutative, spanned by $\mathrm I_{2}$ and $\sigma_{1}=\mathsf M(j)$ with $\sigma_{1}^{2}=\mathrm I_{2}$; its image is the commutant of $\sigma_{1}$, a maximal commutative subalgebra of complex dimension two inside the four of $M_{2}(\mathbb{C})$.
2. The membership test is the two linear equations $a=d$ and $b=c$ and not a determinantal condition; the image is a subspace and not a cone.
3. The idempotent frame $(\Pi_{+},\Pi_{-})$ diagonalises every element at once, by the fixed matrix $P$ of determinant $-2$ and $P^{2}=2\,\mathrm I_{2}$, and the diagonal entries are the two idempotent coordinates $Q_{\pm}=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$.
4. The regular module is completely reducible, the sum of the two simple modules $\mathbb{C}\Pi_{\pm}$, and the Peirce frame exists with two central idempotents and no off-diagonal matrix unit: the exact opposite of the non-split extension of the dual-number category.
5. The trace is $2Q_{\blacktriangle}$ in the complex model and $4q_{0}$ in the realification, the second being the first plus its conjugate; the trace form is $2\,\mathrm I_{2}$, nondegenerate of real signature $(2,2)$.
6. The determinant is the reduced norm $Q_{+}Q_{-}=\langle\breve Q\rangle_{\mathrm{ts}}$, multiplicative, whose zero set is the union of the two transverse planes $Q_{+}=0$ and $Q_{-}=0$; the rank ladder is $2,1,0$, doubled in the realification.
7. Every element is diagonalisable by the same frame, the eigendecomposition is the Peirce decomposition, and Lagrange's formula degenerates on the scalar line although the projectors themselves exist there: the failure is of the formula and not of the object.
8. The adjugate is the model of the tessarine conjugate, the inverse is $\mathsf M(\breve Q_{\mathrm{ts}}/\langle\breve Q\rangle_{\mathrm{ts}})$, and the three operations separate because the transpose is the identity on the image while the bar and the star are conjugate-linear; the model is conformal for the indefinite form $J$ at every element, and for the adjoint exactly on the hypersurface $\operatorname{Re}(Q_{\blacktriangle}\bar Q_{\blacktriangledown})=0$.
9. The four algebraic norms are the four slots of two binary choices, the multiplicative one is the determinant, and the positive definite one is the Frobenius form $\tfrac12\operatorname{tr}(\mathsf M^{\dagger}\mathsf M)$, which defines the coordinatewise order and the positive quadrant of the frame.
10. The distinguished subspaces are the scalar line, the $j$-line, the two ideals, the three fixed planes of the involutions and the union of two planes of the zero divisors; the units form $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ with four contractible components, the idempotents are four points and the nilpotents one.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | a reduced biquaternion, $j$ central with $j^{2}=1$ | *Reduced Biquaternion Space* |
| $\mathsf M(\breve Q)$ | the $2\times2$ complex matrix of the left multiplication | this article |
| $L_{\breve Q}$ | the $4\times4$ real matrix of the same operator | this article |
| $\sigma_{1}$ | $\begin{pmatrix}0&1\\ 1&0\end{pmatrix}=\mathsf M(j)$, the involution generating the image | this article |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | the two central idempotents | *The Peirce Basis of the Reduced Biquaternion Algebra* |
| $Q_{\pm}=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | the two idempotent coordinates, the two eigenvalues | this article |
| $P=\begin{pmatrix}1&1\\ 1&-1\end{pmatrix}$ | the change to the idempotent basis, $\det P=-2$, $P^{2}=2\,\mathrm I_{2}$ | this article |
| $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}$ | the reduced norm, the determinant of the model | *Norm and Invertibility in the Algebra of the Reduced Biquaternions* |
| $\breve Q_{\mathrm{ts}}=Q_{\blacktriangle}-jQ_{\blacktriangledown}$ | the tessarine conjugate, the model of the adjugate | *The Two Involutions and the Group of Involutions of the Reduced Biquaternions* |
| $\breve Q^{*}$ | the star conjugate, the composite of the bar and the tessarine sign | *The Two Involutions and the Group of Involutions of the Reduced Biquaternions* |
| $J=\operatorname{diag}(1,-1)$ | the conjugation realising the tessarine sign, $J\mathsf M J=\mathsf M(\breve Q_{\mathrm{ts}})$ | this article |
| $E_{++},E_{--}$ | the two diagonal matrix units, the projectors in the frame | this article |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition of a semisimple algebra and the matrix units that a product of fields does and does not carry.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the structure of a finite product of fields, the absence of nilpotents in a reduced algebra, and the module theory of the regular representation.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for symmetric matrices, the simultaneous diagonalisation of a commuting family, and the singular values of a normal matrix.
- F. R. Gantmacher, *The Theory of Matrices* (Chelsea, 1959), for the minimal polynomial of a diagonalisable matrix, the derogatory locus, and Lagrange's interpolation formula for the eigenprojectors.
