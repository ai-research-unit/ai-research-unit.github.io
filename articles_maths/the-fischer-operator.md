
# __The Fischer Operator__

## Introduction

The Fischer decomposition writes the homogeneous polynomials of a hypercomplex system as layers of
harmonic, or of monogenic, pieces multiplied by powers of a radial or a Clifford factor; this
article treats the operator that performs the decomposition. The setting is the one of *The Dirac
Operator*: a Clifford algebra $A=\mathrm{Cl}_{0,m}$ with frame $1,e_1,\dots,e_m$, a left Clifford
module $\mathcal{S}$ of values, the vector variable $x$ ranging over $\mathbb{R}^{m+1}$, the
Cauchy–Riemann operator $D=\sum_{\mu=0}^{m}e_\mu\partial_\mu$ and the Laplacian
$\Delta=D\bar D=\bar DD$.

On the space $\mathcal{P}_k$ of $\mathcal{S}$-valued homogeneous polynomials of degree $k$ there are
two decompositions. The harmonic one, classical and due to Stokes and Fischer, writes
$\mathcal{P}_k=\bigoplus_j|x|^{2j}\mathcal{H}_{k-2j}$ with
$\mathcal{H}_j=\ker\Delta\cap\mathcal{P}_j$ the harmonic polynomials; the monogenic one, its
Clifford refinement, writes $\mathcal{P}_k=\bigoplus_j(x^{\natural})^j\mathcal{M}_{k-j}$ with
$\mathcal{M}_j=\ker D\cap\mathcal{P}_j$ the solid spherical monogenics. Both are statements that a
*lowering* operator — the Laplacian, or the Cauchy–Riemann operator — has a complementary *raising*
operator — multiplication by $|x|^2$, or by the conjugate variable $x^{\natural}$ — whose images
fill the polynomials degree by degree. The **Fischer operator** is the projection onto the harmonic,
or the monogenic, part that this decomposition defines, and it is a polynomial expression in the
raising and lowering operators.

The article establishes the two projections, the algebraic identities that make them computable, and
the comparison between them: every monogenic polynomial is harmonic, so the monogenic part is a
subspace of the harmonic part, while the two projections are different operators. The
function-theoretic content of the decompositions — the Cauchy theory, the integral formulae, the
spherical monogenics as such — is *Clifford Analysis*'s and *Regularity and the Cauchy–Riemann
Operator*'s; the article reads the decompositions as operator statements and keeps the
spherical-harmonic side, which is the same statement with the Laplacian in place of $D$, as the
model.

## The Euler Operator and the Grading

**Definition.** The **Euler operator** is

$$
E = \sum_{\mu=0}^{m}x_\mu\,\partial_\mu ,
$$

the infinitesimal generator of the dilations $x\mapsto\lambda x$; a polynomial $P$ is homogeneous of
degree $k$ exactly when $EP=kP$, and $\mathcal{P}_k$ is the eigenspace of $E\subset\mathcal{P}$ with
eigenvalue $k$.

**Proposition (commutation with the grading).** The Euler operator commutes with the Laplacian and
with the Cauchy–Riemann operator, $[E,\Delta]=0$ and $[E,D]=0$, and it satisfies
$[E,L_{|x|^2}]=2L_{|x|^2}$ and $[E,L_{x^{\natural}}]=L_{x^{\natural}}$, where $L_f$ denotes
multiplication by $f$ on the left; consequently the lowering operators preserve the degree by $-2$
and $-1$ respectively and the raising operators increase it by $2$ and $1$.

*Proof.* The Laplacian and $D$ have constant coefficients, so $E$ commutes with them term by term
because $x_\mu\partial_\mu$ and $\partial_\nu$ satisfy
$[\partial_\nu,x_\mu\partial_\mu]=\partial_\nu$ and the second derivatives cancel. For the
multipliers, $E(fP)=(Ef)P+f(EP)$ for a homogeneous $f$, giving $[E,L_f]=(\deg f)L_f$, and
$\deg|x|^2=2$, $\deg x^{\natural}=1$. $\square$

**Corollary (the grading of the two decompositions).** The harmonic decomposition has layers of
degree $k,k-2,k-4,\dots$ and the monogenic one has layers of degree $k,k-1,k-2,\dots$; the parity of
the degree is preserved by the harmonic layers and not by the monogenic ones.

## The Harmonic Fischer Operator

**Lemma (Fischer, harmonic form).** For $k\ge2$ the Laplacian
$\Delta:\mathcal{P}_k\to\mathcal{P}_{k-2}$ is surjective, and multiplication by $|x|^2$ maps
$\mathcal{P}_{k-2}$ injectively with image meeting $\mathcal{H}_k$ only at $0$.

*Proof.* The surjectivity follows from the map of the divisor: with the complexified symbol,
$\Delta$ is induced by the quadratic form $\sum_\mu\xi_\mu^2$, which is nondegenerate, so the
multiplication $\mathcal{P}_{k-2}\to\mathcal{P}_k$, $Q\mapsto|x|^2Q$, has kernel $0$ and the
orthogonality is by the argument of *Regularity and the Cauchy–Riemann Operator*, where the lemma is
stated and proved. $\square$

**Theorem (the commutator identity).** With $n=m+1$ the dimension of the ambient space,

$$
[\Delta, L_{|x|^2}] = \Delta L_{|x|^2}-L_{|x|^2}\Delta = 4E+2n .
$$

*Proof.* Direct computation: $\partial_\mu(|x|^2Q)=2x_\mu Q+|x|^2\partial_\mu Q$, so
$\partial_\mu^2(|x|^2Q)=2Q+4x_\mu\partial_\mu Q+|x|^2\partial_\mu^2Q$; summing over the $n$
coordinates gives $\Delta(|x|^2Q)=2nQ+4EQ+|x|^2\Delta Q$, which is the identity. $\square$

**Corollary (the triangularity and the isomorphism).** On $\mathcal{P}_{k-2}$ the composition
$\Delta L_{|x|^2}$ is triangular with respect to degree, of the form
$(4k+2m-6)\,\mathrm{id}+|x|^2\Delta$, so $\Delta:L_{|x|^2}\mathcal{P}_{k-2}\to\mathcal{P}_{k-2}$ is
an isomorphism for $k\ge2$.

*Proof.* By the theorem, $\Delta(|x|^2Q)=(4E+2n)Q+|x|^2\Delta Q$; on $\mathcal{P}_{k-2}$ the first
term is the scalar $4(k-2)+2n=4k+2m-6$ times $Q$, and the second raises the degree. The scalar does
not vanish for $k\ge2$ and the degree-raising term is nilpotent on $\mathcal{P}_{k-2}$, so the map
is invertible. $\square$

**Definition (the harmonic Fischer operator).** For $k\ge2$ the **Fischer projection** of degree $k$
is

$$
\pi^{\mathrm{har}}_k = I - L_{|x|^2}\circ\bigl(\Delta\big|_{L_{|x|^2}\mathcal{P}_{k-2}}\bigr)^{-1}\circ\Delta ,
$$

and for $k\le1$ it is the identity, $\mathcal{P}_k=\mathcal{H}_k$.

**Theorem (the projection and the decomposition).** The map $\pi^{\mathrm{har}}_k$ is a projection
of $\mathcal{P}_k$ onto $\mathcal{H}_k$ with kernel $|x|^2\mathcal{P}_{k-2}$, and it is equivariant
for the orthogonal group of the ambient space. Iterating gives

$$
\mathcal{P}_k = \mathcal{H}_k\oplus|x|^2\mathcal{H}_{k-2}\oplus|x|^4\mathcal{H}_{k-4}\oplus\cdots ,
$$

that is $\mathcal{P}_k=\bigoplus_{j\ge0}|x|^{2j}\mathcal{H}_{k-2j}$, the **Stokes decomposition**.

*Proof.* If $P=\pi^{\mathrm{har}}_kP$ then $\Delta P=0$ by construction, since
$\Delta\pi^{\mathrm{har}}_kP =\Delta P-\Delta(|x|^2Q)$ with
$Q=(\Delta|_{L_{|x|^2}\mathcal{P}_{k-2}})^{-1}\Delta P$; conversely a harmonic $P$ has $\Delta P=0$,
so $Q=0$ and $\pi^{\mathrm{har}}_kP=P$. The map kills $|x|^2Q$ because $\Delta(|x|^2Q)$ is its own
image under $\Delta$; idempotency follows. The equivariance is that of $\Delta$ and of $|x|^2$, both
of which are rotation-invariant. Applying the projection repeatedly to the remainder gives the
layered form. $\square$

**Remark (the classical statement).** The harmonic Fischer decomposition is the statement that the
harmonic polynomials of all degrees, multiplied by the radial factors $|x|^{2j}$, exhaust the
polynomials; it reduces the theory of spherical harmonics to the linear algebra of the spaces
$\mathcal{H}_k$. It is *Regularity and the Cauchy–Riemann Operator*'s, and for $m=0$, where there is
no Clifford algebra and the operator is the radial derivative, it is the statement that the
homogeneous polynomials of one variable are the powers $x_0^k$.

## The Monogenic Fischer Operator

The same plan with the first-order operator $D$ in place of $\Delta$ and the Clifford multiplier
$x^{\natural}$ in place of $|x|^2$ produces the Clifford refinement.

**Lemma (Fischer, monogenic form; standard).** For $k\ge1$ the operator
$D:\mathcal{P}_k\to \mathcal{P}_{k-1}$ is surjective, and left multiplication by $x^{\natural}$ maps
$\mathcal{P}_{k-1}$ injectively with image meeting $\mathcal{M}_k$ only at $0$.

**Theorem (the monogenic Fischer decomposition).** For every $k\ge0$,

$$
\mathcal{P}_k = \bigoplus_{j=0}^{k}\,(x^{\natural})^{\,j}\,\mathcal{M}_{k-j} , \qquad
\dim\mathcal{M}_k = \dim\mathcal{S}\left[\binom{m+k}{k}-\binom{m+k-1}{k-1}\right] .
$$

*Proof.* By the lemma, $\dim\mathcal{M}_k=\dim\mathcal{P}_k-\dim\mathcal{P}_{k-1}$ and
$\mathcal{P}_k=\mathcal{M}_k\oplus x^{\natural}\mathcal{P}_{k-1}$; the first equality is the
dimension count, the second the direct-sum statement, and iterating the second gives the layered
form. The lemma and the resulting decomposition are quoted as standard, the proof being the
triangular induction of *Clifford Analysis*. $\square$

**Definition (the monogenic Fischer operator).** Let $\pi^{\mathrm{mon}}_k$ be the projection of
$\mathcal{P}_k$ onto $\mathcal{M}_k$ along $x^{\natural}\mathcal{P}_{k-1}$, which exists and is
unique by the theorem. The **Fischer operator** of the Clifford theory is the direct sum

$$
\mathcal{F} = \bigoplus_{k\ge0}\pi^{\mathrm{mon}}_k : \mathcal{P}\longrightarrow\mathcal{M},
$$

defined on the space $\mathcal{P}$ of all $\mathcal{S}$-valued polynomials, mapping it onto the
space $\mathcal{M}$ of all monogenic polynomials.

**Theorem (characterisation).** The operator $\mathcal{F}$ is a projection,
$\mathcal{F}^2=\mathcal{F}$; its image is $\mathcal{M}$ and its kernel is $x^{\natural}\mathcal{P}$,
the ideal of the polynomial algebra generated by the conjugate variable. It is equivariant for the
orthogonal group and for the symmetry group of the system, and it commutes with the Euler operator.

*Proof.* A projection along a complementary subspace is idempotent by definition; the image is
$\mathcal{M}$ and the kernel is $\bigoplus_k x^{\natural}\mathcal{P}_{k-1}=x^{\natural}\mathcal{P}$.
The equivariance is that of $D$ and of the Clifford multiplication, which are both invariant under
the orthogonal group, and commutation with $E$ is the grading statement of the first section.
$\square$

**Remark (the two projections compared).** Every monogenic polynomial is harmonic, because
$\Delta f=\bar DDf=0$ when $Df=0$, so $\mathcal{M}_k\subseteq\mathcal{H}_k$. The inclusion is proper
for $m\ge2$; in the definition $\mathcal{M}_k=\ker D\cap\mathcal{P}_k$ against
$\mathcal{H}_k=\ker\Delta\cap\mathcal{P}_k$, the operator $D$ is the stronger condition.
Consequently $\mathcal{F}$ and the harmonic projection $\pi^{\mathrm{har}}$ are different operators
with the same codomain behaviour only in degree $0$: $\mathcal{F}$ kills the ideal generated by
$x^{\natural}$, while $\pi^{\mathrm{har}}$ kills the ideal generated by $|x|^2$, and the second
ideal is contained in the first because $|x|^2=x^{\natural}x$. The example to keep in mind is $m=1$,
where $D$ is the holomorphic operator, $\mathcal{M}_k$ is spanned by $z^k$, and $\mathcal{H}_k$ has
complex dimension $2$ for $k\ge1$, so the inclusion $\mathcal{M}_k\subset\mathcal{H}_k$ is strict as
soon as $k\ge1$.

**Example (the complex case).** For $m=1$ the monogenic decomposition is
$\mathcal{P}_k=\bigoplus_{j=0}^{k}\bar z^{\,j}\mathbb{C}z^{k-j}$, the standard monomial basis of the
homogeneous polynomials of degree $k$, and $\mathcal{F}$ is the projection onto the highest
holomorphic part. The harmonic decomposition is
$\mathcal{P}_k=\bigoplus_{j\ge0}|z|^{2j}\mathcal{H}_{k-2j}$, and the two are related by the identity
$|z|^2=\bar zz$: iterating the harmonic layers and splitting each $\mathcal{H}_l$ into its monogenic
tower reproduces the monogenic decomposition degree by degree. The comparison is the whole content
of the refinement: the harmonic Fischer decomposition is the Laplacian's, the monogenic one is the
Cauchy–Riemann operator's, and the second refines the first.

## The Fischer Operator on a Hypercomplex System

**Remark (the general form).** The construction is not special to the Clifford case. Let $(A,D)$ be
a hypercomplex system in the sense of *Regularity and the Cauchy–Riemann Operator*, with $D$
elliptic and $D\bar D=\Delta$; then the same three ingredients are available: the Euler operator
$E$, the multiplier $|x|^2$ for the Laplacian (whose layer multiplier is the radial factor), and the
multiplier dual to $D$ (the Clifford conjugate variable) for the first-order operator. The operator
$\Delta$ is surjective on homogeneous polynomials and
$\Delta:L_{|x|^2}\mathcal{P}_{k-2}\to\mathcal{P}_{k-2}$ is triangular with nonvanishing scalar part,
so the harmonic Fischer projection exists for every admissible system; the monogenic projection
exists whenever the Fischer lemma for $D$ does, which is the case under the standing hypotheses. The
particular dimensions of the pieces are properties of the system, computed by the dimension
recursion; the operator is the same.

**Remark (why the multiplier is the conjugate variable).** In the corpus's sign convention the
operator $D$ carries $+e_i\partial_i$ and satisfies $D\bar D=\Delta$, so the *dual* multiplier — the
one for which $D$ acts triangularly with positive diagonal — is
$x^{\natural}=x_0-\sum_{i\ge1}x_ie_i$, whose Clifford norm is $|x|^2$; the conjugate operator
$\bar D$ plays the mirror role and pairs with the plain variable $x$. The point is that the
multiplier has the same *Clifford* sign as the operator, not the same *coordinate* sign, and this is
what makes the pieces of the decomposition the standard monomials rather than a triangular transform
of them. The corpus states the decomposition in the conjugate variable in *Clifford Analysis*; the
article *Regularity and the Cauchy–Riemann Operator* states the same refinement with the plain
variable, where the layers are still a decomposition but of the mirror pairing $(\bar D,x)$. A
reader comparing the two must therefore read the multiplier together with the operator, and the two
statements agree once the pairing is fixed.

## Summary

On the space $\mathcal{P}_k$ of $\mathcal{S}$-valued homogeneous polynomials of degree $k$, the
**Euler operator** $E=\sum_\mu x_\mu\partial_\mu$ is the grading, and the Laplacian and the
Cauchy–Riemann operator commute with it. The harmonic **Fischer lemma** —
$\Delta:\mathcal{P}_k\to\mathcal{P}_{k-2}$ is surjective and
$|x|^2\mathcal{P}_{k-2}\cap\mathcal{H}_k=0$ — together with the commutator identity
$[\Delta,L_{|x|^2}]=4E+2n$ makes $\Delta:L_{|x|^2}\mathcal{P}_{k-2}\to\mathcal{P}_{k-2}$ an
isomorphism for $k\ge2$, and hence defines the harmonic **Fischer operator**
$\pi^{\mathrm{har}}_k=I-L_{|x|^2}(\Delta|_{L_{|x|^2}\mathcal{P}_{k-2}})^{-1}\Delta$, a projection of
$\mathcal{P}_k$ onto $\mathcal{H}_k$ with kernel $|x|^2\mathcal{P}_{k-2}$; iterating gives the
Stokes decomposition $\mathcal{P}_k=\bigoplus_j|x|^{2j}\mathcal{H}_{k-2j}$. The monogenic refinement
replaces $\Delta$ by $D$ and $|x|^2$ by the conjugate variable $x^{\natural}$: the monogenic
**Fischer decomposition** is $\mathcal{P}_k=\bigoplus_{j=0}^{k}(x^{\natural})^j\mathcal{M}_{k-j}$,
with $\dim\mathcal{M}_k=\dim\mathcal{S}[\binom{m+k}{k}-\binom{m+k-1}{k-1}]$, and the **Fischer
operator** $\mathcal{F}=\bigoplus_k\pi^{\mathrm{mon}}_k$ is the projection onto the monogenic
polynomials with kernel $x^{\natural}\mathcal{P}$. Since every monogenic polynomial is harmonic,
$\mathcal{M}_k\subseteq\mathcal{H}_k$, strictly for $m\ge2$; the two projections differ and are
related by $|x|^2=x^{\natural}x$. The construction is available on every admissible hypercomplex
system, and the function-theoretic content of the decompositions is *Clifford Analysis*'s and
*Regularity and the Cauchy–Riemann Operator*'s.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{P}_k$ | $\mathcal{S}$-valued homogeneous polynomials of degree $k$ |
| $E=\sum_\mu x_\mu\partial_\mu$ | Euler operator; $EP=kP$ on $\mathcal{P}_k$ |
| $\mathcal{H}_k=\ker\Delta\cap\mathcal{P}_k$ | Harmonic homogeneous polynomials |
| $\mathcal{M}_k=\ker D\cap\mathcal{P}_k$ | Solid spherical monogenics |
| $L_f$ | Left multiplication by $f$ |
| $[\Delta,L_{|x|^2}]=4E+2n$ | The harmonic commutator identity, $n=m+1$ |
| $\pi^{\mathrm{har}}_k$ | Harmonic Fischer projection onto $\mathcal{H}_k$ |
| $\mathcal{F}=\bigoplus_k\pi^{\mathrm{mon}}_k$ | The Fischer operator, projection onto $\mathcal{M}$ |
| $\ker\mathcal{F}=x^{\natural}\mathcal{P}$, $\operatorname{im}\mathcal{F}=\mathcal{M}$ | Kernel and image of the Fischer operator |
| $\mathcal{P}_k=\bigoplus_j|x|^{2j}\mathcal{H}_{k-2j}$ | Stokes decomposition |
| $\mathcal{P}_k=\bigoplus_{j}(x^{\natural})^j\mathcal{M}_{k-j}$ | Monogenic Fischer decomposition |

## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the monogenic Fischer decomposition and the spherical monogenics.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the Fischer decomposition over Clifford modules.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton University Press, 1971), for the harmonic Fischer decomposition and the theory of spherical harmonics.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the decomposition as an operator statement.
- Sheldon Axler, Paul Bourdon and Wade Ramey, *Harmonic Function Theory* (Springer, 2nd ed. 2001), for the Fischer decomposition of polynomials into harmonic layers.
