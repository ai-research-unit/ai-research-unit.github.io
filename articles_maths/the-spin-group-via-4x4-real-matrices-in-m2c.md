# __The Spin Group via $4\times4$ Real Matrices__

## Introduction

**The question.** The spin group is $S^3$, the unit quaternions. Its $2\times2$ complex display is $SU(2)$. What is the $4\times4$ real display, how is it built from the same multiplication, and what does it show that the $2\times2$ display cannot?

**Why it is the same statement.** This is the in-depth matrix reading of [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices.html). The source builds the left regular matrix $L(\tilde q)_{\mu\nu}=[\tilde qe_\nu]_\mu$ from the multiplication table alone; under the display $A=\mathsf M_2(\tilde q)$ the same matrix appears as the coefficient-frame array of $L_A$, and the $2\times2$ display is $A$ itself. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. That the coefficient-frame array of $L_A$ is the left regular matrix of the source, entry for entry, and that for real coefficients it is a real orthogonal matrix. The three generators as signed permutations, with real antisymmetry, square minus one, the bracket and the zero diagonal. The group as an exponential, with the closed form, the kernel and the surjectivity. The isoclinic structure and the doubled spectrum. The absence of a diagonal generator, and its reading as the display's freedom from a preferred axis. The two copies and the double cover. The parallel with the $2\times2$ display, in a table.

**What the article does not do.** It does not carry the spin labels, which belong to the carriers and are [The Clebsch–Gordan Decomposition of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra-in-m2c.html); it does not treat the two-sided action of the spin group, which is [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, and the coefficient basis is $(E_t,E_x,E_y,E_z)=(\mathrm I_2,-i\sigma_1,-i\sigma_2,-i\sigma_3)$. The coefficient-frame array of a $\mathbb{C}$-linear operator $T$ is $[T]_{\mu\nu}$ defined by $T(E_\nu)=\sum_\mu[T]_{\mu\nu}E_\mu$. The three generators are $L_k=[E_k\cdot]$ for $k=x,y,z$. A quaternion is real when its four coefficients are real; the spin group is the set of real $q$ with $N=1$.

**Boundaries.** The arrays themselves are [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html). The two-sided operator is [Two-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-regular-sector-in-m2c.html). The display privilege is [The Axis-Free $4\times4$ Representation : Operators](m4c-axis-free-representation-operators.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $q=(q_t,q_x,q_y,q_z)$ are real coefficients, $A=\mathsf M_2(q)\in SU(2)$, $L(q)$ is the coefficient-frame array of $Y\mapsto AY$, and $L_x,L_y,L_z$ are the three generators.

## The Coefficient-Frame Array Is the Left Regular Matrix

**The identity.** For every $q$, real or complex,
$$
\left[Y\mapsto AY\right]_{\mu\nu}=\left[A E_\nu\right]_\mu,\qquad A=\mathsf M_2(q),
$$
and for real $q$ this is exactly the left regular matrix of the source,
$$
L(q)=\begin{pmatrix}
q_t&-q_x&-q_y&-q_z\\
q_x&q_t&-q_z&q_y\\
q_y&q_z&q_t&-q_x\\
q_z&-q_y&q_x&q_t
\end{pmatrix}.
$$
Verified in two ways: the array of $L_A$ equals $q_t\mathrm I_4+q_xL_x+q_yL_y+q_zL_z$ with residual $0$, and the printed matrices $L_x,L_y,L_z$ equal the source's, entry for entry.

**The reading.** The first column of $L(q)$ is the coordinate column of $q$ itself, because $A\mathrm I_2=A$. Every other column is the coordinate column of a product. So the array is the multiplication table read aloud, with integer entries, and no entry is imaginary.

**The three generators.** With rows and columns indexed $(t,x,y,z)$,
$$
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

**The four properties.** Each generator is real and antisymmetric, $L_k^{\mathsf T}=-L_k$; each squares to minus the identity, $L_k^2=-\mathrm I_4$; the brackets are $[L_x,L_y]=2L_z$ and cyclically; and each has exactly one non-zero entry, equal to $\pm1$, in every row and every column, with zero diagonal. All four verified exactly, with residual $0$.

**The last property, said carefully.** None of the generators has a zero row or a zero column. The coordinate that a generator fixes does not appear as a zero line; it appears as the cut between two equal rotation blocks, as the isocliny section shows.

## The Group

**The image.** For real $q$ of norm one the array is real orthogonal:
$$
L(q)^{\mathsf T}L(q)=\mathrm I_4,\qquad \det L(q)=1,\qquad \operatorname{tr}L(q)=4q_t .
$$
Verified on a hundred random unit quaternions, with residuals $3\cdot10^{-16}$, $7\cdot10^{-16}$ and $0$.

**The closed form.** For a real unit $u=(0,u_x,u_y,u_z)$ and real $\theta$, put $U=u_xL_x+u_yL_y+u_zL_z$. Then $U^2=-\mathrm I_4$ and
$$
\exp(\theta U)=\cos\theta\,\mathrm I_4+\sin\theta\,U=L\left(\cos\theta\,e_t+\sin\theta\,u\right).
$$
The parameter $\theta$ is the half angle of the rotor, and the array is the full rotation of $\mathbb{R}^4$ by that half angle in two planes.

**The spectrum.** The eigenvalues of $L(q)$ are $e^{i\theta}$ and $e^{-i\theta}$, each with multiplicity two; verified on a random unit quaternion, where $\cos\theta=q_t$ recovers the scalar part from the trace alone.

**The kernel and the surjectivity.** The exponential is onto the group, since every unit quaternion is $\cos\theta\,e_t+\sin\theta\,u$ with $0\le\theta\le\pi$. It is not injective: $\exp(\theta U)=\exp((\theta+2\pi)U)$, and $\exp(\pi U)=-\mathrm I_4$ for every unit $u$. The kernel is the union of the spheres of radius $2\pi k$ in the three-dimensional algebra $\mathfrak{g}_L=\operatorname{span}_\mathbb{R}\{L_x,L_y,L_z\}$.

**The two descriptions of the group.** $\exp(\mathfrak{g}_L)=\{L(q):q\in S^3\}$; the inclusion from left to right is the closed form, and the other follows from the polar form of a unit quaternion.

## Isocliny and the Doubled Spectrum

**The block form.** In the basis $(e_t,e_z,e_x,e_y)$ the generator $L_z$ is
$$
L_z=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}=\operatorname{diag}(R,R),\qquad R=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
$$
and the other two are the same after a cyclic relabelling, which is an automorphism of the algebra. Verified with residual $0$.

**The consequence.** Every element of the group is, in a suitable basis, $\operatorname{diag}(R_\theta,R_\theta)$: it rotates its two invariant planes by the same angle. That is the isoclinic property, and it is why the group is one of the two copies of $S^3$ inside the six-dimensional $SO(4)$.

**The spectral form of the same fact.** A rotation of $\mathbb{R}^4$ with angles $\alpha,\beta$ has eigenvalues $e^{\pm i\alpha},e^{\pm i\beta}$; the spectrum $e^{\pm i\theta}$ each twice is the equality $\alpha=\beta$ up to sign.

## No Diagonal Generator

**The theorem.** No non-zero element of $\mathfrak{g}_L$ is diagonal, and no element of the group other than $\pm\mathrm I_4$ is diagonal.

**The proof.** Every element of $\mathfrak{g}_L$ is real antisymmetric, and a real diagonal antisymmetric matrix is zero. A diagonal orthogonal matrix has entries $\pm1$; the array $L(q)$ for $q\neq\pm e_t$ has the non-real eigenvalues $e^{\pm i\theta}$, so it is not diagonal, and $L(\pm e_t)=\pm\mathrm I_4$.

**The contrast with the $2\times2$ display.** There the third generator is diagonal,
$$
-i\sigma_3=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$
so the $2\times2$ display marks the third axis, and the other two generators are not diagonal. The three generators pairwise fail to commute, so no display can make two of them diagonal at once; the mark is forced to be a single axis.

**What the mark is.** It is the choice of a complex structure on the real four-space, that is a point of $S^2$; different choices give conjugate displays. The real array makes no such choice.

**The privilege, stated correctly.** The axis-free array is the representative of the corpus because its entries are signed permutations and every identity in it is an integer check. That is a canonical choice of representative, not a preference for a direction: the array fixes no invariant and singles out no axis. The argument here is the three-dimensional instance of the same point: an array can carry a frame inside its symbols, and the real array carries the least.

## The Two Copies and the Double Cover

**The right regular family.** Right multiplication $Y\mapsto YE_k$ has coefficient-frame array $R_k$, and the two families commute, $L_jR_k=R_kL_j$, with residual $0$. The six generators $L_x,L_y,L_z,R_x,R_y,R_z$ have rank six, and the commutant of $\mathfrak{g}_L$ in $M_4(\mathbb{R})$ has dimension four, the right regular family.

**The two copies.** $\mathfrak{so}(4)=\mathfrak{g}_L\oplus\mathfrak{g}_R$ with $3+3=6$; at group level $(q_L,q_R)\mapsto[Y\mapsto q_LYq_R^{-1}]$ is onto $SO(4)$ with kernel $\{\pm(\mathrm I_4,\mathrm I_4)\}$, and the two copies meet in $\{\pm\mathrm I_4\}$.

**The covering maps.** The adjoint display $q\mapsto[\vec v\mapsto q\vec vq^{-1}]$ is onto $SO(3)$ with kernel $\{\pm1\}$; the left regular display is injective, so it carries the sign, $L(-q)=-L(q)$, and the trace separates the two, $\pm4q_t$.

**The two-sided display in this language.** $Y\mapsto AYA^{\dagger}$ with $A\in SU(2)$ is the pair $(q,\bar q)$ read on both slots; it is a rotation of $\mathbb{R}^4$ by the full angle, and it is the subject of [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html).

## The Two Displays Side by Side

| item | $2\times2$ display | coefficient-frame $4\times4$ array |
|---|---|---|
| group | $SU(2)\subset M_2(\mathbb{C})$ | real orthogonal, $\det1$ |
| field | $\mathbb{C}$ | $\mathbb{R}$ for real coefficients |
| size | $2$ | $4$ |
| carrier | $\mathbb{C}^2$ | $\mathbb{R}^4$ |
| faithful | yes | yes |
| bracket of raw generators | $2\varepsilon_{ijk}$ | $2\varepsilon_{ijk}$ |
| diagonal generator | one, $-i\sigma_3$ | none |
| trace | $2q_t$ | $4q_t$ |
| determinant of a unit element | $1$ | $1$ |
| spectrum of a unit element | $e^{\pm i\theta}$ | $e^{\pm i\theta}$, each twice |
| isocliny | hidden | displayed |

**The two rows easily got wrong.** The bracket is the same on both sides, because both arrays are images of one quaternion bracket; a table that mixes $\varepsilon_{ijk}$ with $2\varepsilon_{ijk}$ compares two normalizations, not two displays. The trace differs by the size and by nothing else: $2q_t$ against $4q_t$ both recover the scalar part.

## Worked Example: the Quarter Turn

**The rotor.** $q=\tfrac1{\sqrt2}(e_t+e_z)$, of rotor angle $\pi/4$, inducing a rotation of angle $\pi/2$.

**The real array.** $L(q)=\tfrac1{\sqrt2}(\mathrm I_4+L_z)$, that is
$$
\frac1{\sqrt2}\begin{pmatrix}1&0&0&-1\\0&1&-1&0\\0&1&1&0\\1&0&0&1\end{pmatrix},
$$
which rotates the plane $(e_t,e_z)$ and the plane $(e_x,e_y)$ each by $\pi/2$; the two blocks are equal, and the half-angle factor $\tfrac1{\sqrt2}$ sits in all eight non-zero entries.

**The $2\times2$ array.**
$$
A=\frac1{\sqrt2}\left(\mathrm I_2-i\sigma_3\right)=\frac1{\sqrt2}\begin{pmatrix}1-i&0\\0&1+i\end{pmatrix},
$$
diagonal, with the half-angle in the modulus. The two arrays are one group element in two displays; only the second marks an axis.

## Where $n=2$ Differs

**Nothing differs, and this is the point.** The spin group is the group of unit elements of the real quaternion subalgebra, which sits inside $\mathbb{B}$ and inside $M_2(\mathbb{C})$ without reference to a size. Its displays are the $2\times2$ complex one and the $4\times4$ real one; there is no larger display because the algebra has complex dimension two and real dimension four.

**The one thing that does change.** At order $n$ the analogue is the group of unitary matrices, of real dimension $n^2-1$, and the left regular array lives on $n^2$ complex dimensions. Its commutant is again the right regular family, but the isocliny has no direct analogue: it is a property of the four-dimensional real carrier that exists only at $n=2$.

## Summary

The coefficient-frame array of the left multiplication is the left regular matrix of the source, entry for entry, and for real coefficients it is real orthogonal of determinant one with trace $4q_t$. Its three generators are the signed permutations $L_x,L_y,L_z$, real and antisymmetric, with $L_k^2=-\mathrm I_4$, $[L_x,L_y]=2L_z$ and zero diagonal; all verified exactly.

The exponential is $\exp(\theta U)=\cos\theta\,\mathrm I_4+\sin\theta\,U$, onto the group and with kernel the spheres of radius $2\pi k$. The spectrum is $e^{\pm i\theta}$ each twice, and in the basis $(e_t,e_z,e_x,e_y)$ every generator is $\operatorname{diag}(R,R)$: the image is one of the two isoclinic copies of $S^3$ in $SO(4)$, and $\mathfrak{so}(4)=\mathfrak{g}_L\oplus\mathfrak{g}_R$ with $3+3=6$.

No element of $\mathfrak{g}_L$ is diagonal, because a real diagonal antisymmetric matrix is zero, while the $2\times2$ display has the diagonal generator $-i\sigma_3$. The mark on the third axis is the choice of a complex structure on the real four-space. The axis-free array makes no choice; it is the canonical representative, and it fixes no invariant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $q=(q_t,q_x,q_y,q_z)$ | real quaternion coefficients |
| $A=\mathsf M_2(q)$ | the $2\times2$ display |
| $L(q)$ | the coefficient-frame array of $Y\mapsto AY$ |
| $L_x,L_y,L_z$ | the three generators |
| $\mathfrak{g}_L$ | their real span |
| $R_k$ | the right regular generators |
| $U$ | a unit generator $u\cdot L$ |
| $\theta$ | the half angle |

## Further Reading

- [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices.html), for the source's full development of the left regular display and its pitfalls.
- [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html), for the passage from the group to a single rotor and its spin.
- [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html), for the array of a left multiplication and its Kronecker form.
- [Two-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-regular-sector-in-m2c.html), for the two-sided action of the same group.
- [The Axis-Free $4\times4$ Representation : Operators](m4c-axis-free-representation-operators.html), for the privilege of the axis-free array and its own boundary paragraph.
