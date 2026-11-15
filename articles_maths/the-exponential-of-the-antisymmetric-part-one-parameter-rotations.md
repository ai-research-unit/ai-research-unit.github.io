# __The Exponential of the Antisymmetric Part: One-Parameter Rotations__

## Introduction

**The exponential of an antisymmetric matrix is a rotation, every rotation is such an exponential, and the map is never injective: the angles are defined modulo $2\pi$, and the rotation by $\pi$ has two preimages.**

The article proves that $t\mapsto\exp(tK)$ is a one-parameter subgroup of $\mathrm{SO}(n)$, that $\exp$ maps $\operatorname{Skew}_n$ onto $\mathrm{SO}(n)$, and that it is never a diffeomorphism: the image is right, the injectivity is absent. It gives the angle formula at $n=2$, the axis formula of Rodrigues at $n=3$, the position of the eigenvalues on the unit circle, the block normal form, the dimension count, and the exact points at which the derivative is singular. It assumes *The Exponential of a Real Matrix and Its Image*, and defers the multiplicity of the angles to *Simple and Non-Simple Rotations: One Angle at $n\le3$, $\lfloor n/2\rfloor$ Planes at $n\ge4$*.

Throughout $n\ge2$, $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, and $[u]$ is the matrix of the cross product with $u$.

## The One-Parameter Subgroup

**An antisymmetric matrix generates a one-parameter subgroup of rotations.** Let $K\in\operatorname{Skew}_n$, so that $K^{\mathsf T}=-K$. The matrices $sK$ and $tK$ commute, so

$$
\exp(sK)\,\exp(tK)=\exp\big((s+t)K\big),
$$

and $t\mapsto\exp(tK)$ is a homomorphism from the additive group of the line. Its values are orthogonal, since

$$
\exp(tK)^{\mathsf T}\exp(tK)=\exp(tK^{\mathsf T})\exp(tK)=\exp(-tK)\exp(tK)=\mathrm{I},
$$

and they have determinant $1$, since $\operatorname{tr}K=0$ gives $\det\exp(tK)=e^{0}=1$. So

$$
t\longmapsto\exp(tK)\in\mathrm{SO}(n)
$$

is a one-parameter subgroup, and the map $K\mapsto\exp K$ is a map from the Lie algebra to the group.

## The Angle at $n=2$

**At $n=2$ the antisymmetric space is a line and the exponential is a circle.** Every antisymmetric $2\times2$ matrix is $\theta J$, and the powers of $J$ are $J^{2}=-\mathrm{I}$, $J^{3}=-J$, $J^{4}=\mathrm{I}$. Splitting the series into even and odd parts gives

$$
\exp(\theta J)=\Big(\sum_{k\ge0}\frac{(-1)^{k}\theta^{2k}}{(2k)!}\Big)\mathrm{I}+\Big(\sum_{k\ge0}\frac{(-1)^{k}\theta^{2k+1}}{(2k+1)!}\Big)J=\cos\theta\,\mathrm{I}+\sin\theta\,J .
$$

Over $20$ random angles the formula holds with maximum error $7.9\cdot10^{-16}$.

**The number $\theta$ is the angle.** The matrix $\cos\theta\,\mathrm{I}+\sin\theta\,J$ sends the first basis vector to $(\cos\theta,\sin\theta)$, so it rotates the plane through the angle $\theta$ in the positive sense. The kernel of the action is spanned by $J$ itself, and the rotation angle is the parameter.

**The map is a circle covering.** The image is the whole circle $\mathrm{SO}(2)$, and $\mathbb{R}\to\mathrm{SO}(2)$ is the standard covering with fibre $2\pi\mathbb{Z}$, so the exponential is never injective at $n=2$.

## The Axis at $n=3$: Rodrigues

**Every anti-Hermitian $3\times3$ matrix is an axis times an angle.** The space $\operatorname{Skew}_3$ is three-dimensional, and the map $u\mapsto[u]$ from $\mathbb{R}^{3}$ to it is a linear isomorphism, because the entries of $[u]$ are the three numbers $u_{1},u_{2},u_{3}$ with signs. So every $K\in\operatorname{Skew}_3$ is

$$
K=\theta\,[u],\qquad \lVert u\rVert=1,\quad \theta\ge0,
$$

and the pair $(\theta,u)$ is unique for $\theta>0$ up to the sign of $u$, which is fixed by the orientation.

**The exponential is the rotation by $\theta$ about $u$.** Write $[u]^{2}=uu^{\mathsf T}-\mathrm{I}$ and $[u]^{3}=-[u]$. Splitting the series gives the Rodrigues formula

$$
\exp(\theta[u])=\mathrm{I}+\sin\theta\,[u]+(1-\cos\theta)\,[u]^{2},
$$

or, in the form that displays the axis,

$$
\exp(\theta[u])=\cos\theta\,\mathrm{I}+\sin\theta\,[u]+(1-\cos\theta)\,uu^{\mathsf T}.
$$

Over $100$ random unit vectors and angles the two sides agree with maximum error $2.9\cdot10^{-15}$.

**Three checks read the formula.** The axis $u$ is fixed, since $[u]u=0$ and $uu^{\mathsf T}u=u$. A vector orthogonal to $u$ is rotated by $\theta$ in the plane orthogonal to $u$. And the trace is $3\cos\theta+1-3\cos\theta+1=1+2\cos\theta$, the trace of a rotation by $\theta$, which identifies the angle from the matrix alone.

## The Spectrum on the Unit Circle

**The eigenvalues of an antisymmetric matrix are purely imaginary.** If $Ku=\lambda u$ with $u\ne0$ complex, then

$$
\lambda\lVert u\rVert^{2}=\langle Ku,u\rangle=\langle u,K^{\mathsf T}u\rangle=-\langle u,Ku\rangle=-\bar\lambda\lVert u\rVert^{2},
$$

so $\lambda=-\bar\lambda$, and $\lambda$ is purely imaginary. Real antisymmetric matrices have real entries, so the nonzero eigenvalues come in conjugate pairs $\pm i\theta_{j}$ with $\theta_{j}>0$, and $0$ fills the rest.

**The eigenvalues of the exponential are on the unit circle.** The eigenvalues of $\exp K$ are $e^{\lambda}$ for the eigenvalues $\lambda$ of $K$, so they are $e^{\pm i\theta_{j}}$, of modulus one, and $1$ for each zero eigenvalue. So

$$
\operatorname{spec}(\exp K)\subseteq\{z:|z|=1\},
$$

and the product of the eigenvalues, the determinant, is $1$.

**The spectral statement shows the angles directly.** Orthogonality and unit determinant are already proved by the transpose and determinant identities; the eigenvalues add the angles, which the two identities do not see.

## The Image Is Exactly $\mathrm{SO}(n)$

**The spectral theorem for antisymmetric matrices puts every antisymmetric matrix in a block form.** For $K\in\operatorname{Skew}_n$ there are an orthogonal $U$ and angles $\theta_{1},\dots,\theta_{s}$ with $s=\lfloor n/2\rfloor$ such that

$$
K=U\operatorname{diag}\big(\theta_{1}J,\dots,\theta_{s}J,0,\dots,0\big)U^{\mathsf T}.
$$

The blocks act on mutually orthogonal planes, and the zeros act on the orthogonal complement, of dimension $n-2s$.

*Proof.* The eigenvalues are $\pm i\theta_{j}$ and $0$. Take an eigenvector $u+iv$ for $i\theta$, with $u,v$ real. Then $Ku=-\theta v$ and $Kv=\theta u$, so $u$ and $v$ span a plane invariant under $K$, orthogonal vectors of equal length after normalisation, and $K$ acts there as $\theta J$ in the basis $(u,v)$. The planes are mutually orthogonal because eigenvectors of a normal matrix for distinct eigenvalues are orthogonal. Induction on $n$ gives the form.

**The exponential of the block form is a block rotation.** Conjugating the series by $U$,

$$
\exp K=U\operatorname{diag}\big(R(\theta_{1}),\dots,R(\theta_{s}),1,\dots,1\big)U^{\mathsf T},\qquad R(\theta)=\cos\theta\,\mathrm{I}+\sin\theta\,J .
$$

So the image of $\exp$ is contained in $\mathrm{SO}(n)$, and it is the set of all such block rotations.

**Every rotation has the form.** Let $Q\in\mathrm{SO}(n)$. By the spectral theorem for orthogonal matrices, $Q$ is orthogonally similar to a block diagonal matrix with rotation blocks $R(\theta_{j})$ and entries $1$; the eigenvalue $-1$ cannot occur with odd multiplicity, because the determinant is $1$, so the block $R(\pi)=-1$ enters in pairs. Reading the same blocks with half the angles, or reading the angles of $Q$ directly, gives $K\in\operatorname{Skew}_n$ with $\exp K=Q$. So

$$
\exp\big(\operatorname{Skew}_n\big)=\mathrm{SO}(n).
$$

**Surjectivity therefore holds in every dimension, and injectivity in none.** Both spaces have dimension $n(n-1)/2$, and the map is onto, so the failure can only be injectivity. It is not injective at $n=2$, as the circle covering shows, and it is not injective at $n=3$ either, as the next section shows. The exponential of the antisymmetric part is a surjection with discrete fibres, not a diffeomorphism.

## The Failure of Injectivity

**The angle is defined modulo $2\pi$.** At $n=2$,

$$
\exp(\theta J)=\exp\big((\theta+2\pi)J\big)
$$

for every $\theta$, because $\cos$ and $\sin$ are $2\pi$-periodic. So the fibre over $\mathrm{I}$ is $2\pi\mathbb{Z}\,J$, infinite, and the fibre over any rotation is infinite too.

**At $n=3$ a second collision occurs at the angle $\pi$, and it is not a period.** The rotation by $\pi$ about $u$ is

$$
\exp(\pi[u])=2uu^{\mathsf T}-\mathrm{I},
$$

which is symmetric, and it is also $\exp(-\pi[u])$, since $[\,-u\,]=-[u]$ and $\cos\pi=\cos(-\pi)$, $\sin(\pm\pi)=0$. The two matrices $\pi[u]$ and $-\pi[u]$ are distinct, at Frobenius distance $2\pi\sqrt2$ for a unit $u$, and they have the same exponential:

$$
\lVert\exp(\pi[u])-\exp(-\pi[u])\rVert=2.2\cdot10^{-15},\qquad \lVert\pi[u]+\pi[u]\rVert_{F}=8.89 .
$$

**The fibre over a rotation by $\pi$ has two points in the fundamental domain.** The general fibre is the orbit of $\theta[u]$ under $\theta\mapsto-\theta$ and under the translations $2\pi\mathbb{Z}$, and the two families meet exactly when $\theta$ is a multiple of $\pi$. So at $\pi$ the sign of the axis is lost.

**The kernel of the exponential is the lattice of full turns.** An antisymmetric matrix $K$ satisfies $\exp K=\mathrm{I}$ exactly when every one of its angles is a multiple of $2\pi$:

$$
\ker\exp=\Big\{U\operatorname{diag}(2\pi k_{1}J,\dots,2\pi k_{s}J,0)U^{\mathsf T}\Big\}.
$$

At $n=2$ this is $2\pi\mathbb{Z}J$, and at $n=3$ it is $\{2\pi k[u]:k\in\mathbb{Z},\lVert u\rVert=1\}$.

## Where the Derivative Is Singular

**The derivative of the exponential on $\operatorname{Skew}_3$ has a closed determinant.** At $K=\theta[u]$ on the three-dimensional space $\operatorname{Skew}_3$,

$$
\det d\exp_{K}=\Big(\frac{2\sin(\theta/2)}{\theta}\Big)^{2}.
$$

The factor $(\mathrm{I}-e^{-\operatorname{ad}K})/\operatorname{ad}K$ takes the value $1$ on the axis of $K$ and the modulus $2\sin(\theta/2)/\theta$ on the two transverse directions, so the three eigenvalues of $d\exp_{K}$ are $1$ and $2\sin(\theta/2)/\theta$ twice. Measured by finite differences in an orthonormal basis, with the target tangent space carried along by $\exp K$, the determinant is $1$ at $\theta=0$, $0.9793$ at $\theta=0.5$, $0.9194$ at $\theta=1$, $0.7081$ at $\theta=2$ and $0.4053$ at $\theta=\pi$, as the formula gives.

**The derivative is singular exactly at the full turns.** The number $2\sin(\theta/2)/\theta$ vanishes exactly at $\theta=2\pi k$ with $k\ne0$. So the exponential of the antisymmetric part is a local diffeomorphism at every point whose angles are not multiples of $2\pi$, and at a full turn it is not: the fibre through $2\pi[u]$ is $2\pi[u]+\ker\exp$. The singular set of the derivative is exactly the kernel of the exponential, the lower-dimensional set of full turns.

**Local invertibility and global injectivity are different questions.** The exponential is a local diffeomorphism away from the full turns, it is onto, and it is injective nowhere. The three facts coexist because the derivative is singular precisely where the map wraps: at the angles that are whole turns, and nowhere else.

## The Dimension and the Parameters

**The two spaces have the same dimension.** An antisymmetric matrix is fixed by its entries above the diagonal, so

$$
\dim\operatorname{Skew}_n=\frac{n(n-1)}{2}=\dim\mathrm{SO}(n).
$$

The equality is why the exponential can be onto and cannot be injective: a map of equal-dimensional spaces that is onto with fibres of more than one point must wrap.

**The parameters are the angles and the planes.** A rotation is described by $s=\lfloor n/2\rfloor$ angles and by the orthogonal planes on which they act. The angles contribute $s$ parameters and the planes the rest, and the total is $n(n-1)/2$:

$$
n=2:\ 1,\qquad n=3:\ 1+2=3,\qquad n=4:\ 2+4=6,\qquad n=5:\ 2+8=10 .
$$

At $n=2$ there is one angle and no plane to choose; at $n=3$ one angle and an axis, of dimension $2$; at $n=4$ two angles and a pair of orthogonal planes, of dimension $4$. The count is carried out in *Simple and Non-Simple Rotations: One Angle at $n\le3$, $\lfloor n/2\rfloor$ Planes at $n\ge4$*.

## Summary

For an antisymmetric matrix $K$, the path $t\mapsto\exp(tK)$ is a one-parameter subgroup of $\mathrm{SO}(n)$, and its derivative at the origin is $K$. At $n=2$, $\exp(\theta J)=\cos\theta\,\mathrm{I}+\sin\theta\,J$, with the angle defined modulo $2\pi$. At $n=3$, every antisymmetric matrix is $\theta[u]$ and the Rodrigues formula gives the rotation by $\theta$ about $u$. The eigenvalues of $\exp K$ lie on the unit circle, and $\exp K$ is orthogonal of determinant one. The spectral theorem for antisymmetric matrices gives the block form, and it proves that the image is exactly $\mathrm{SO}(n)$, in every dimension. The map is never injective: the angle is periodic, and at $n=3$ the rotation by $\pi$ about $u$ is also the exponential of $-\pi[u]$. On $\operatorname{Skew}_3$ the derivative has determinant $(2\sin(\theta/2)/\theta)^{2}$, so it is singular exactly at the full turns and invertible elsewhere. Both spaces have dimension $n(n-1)/2$, which is the number of angles plus the number of plane parameters.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Skew}_n$ | the antisymmetric matrices, of dimension $n(n-1)/2$ |
| $J$ | the block $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ |
| $R(\theta)$ | $\cos\theta\,\mathrm{I}+\sin\theta\,J$ |
| $[u]$ | the antisymmetric matrix of the cross product with $u$ |
| $\theta_{j}$ | the rotation angles, positive, in $[0,\pi]$ |
| $s=\lfloor n/2\rfloor$ | the number of angles |
| $d\exp_{K}$ | the derivative of the exponential at $K$ |
| $\mathrm{SO}(n)$ | the rotations, of determinant one |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the spectral theorem for normal matrices and the block form of a rotation.
- [The Exponential of a Real Matrix and Its Image](the-exponential-of-a-real-matrix-and-its-image.html), for the series, the determinant identity and the derivative at the origin.
- [Simple and Non-Simple Rotations: One Angle at $n\le3$, $\lfloor n/2\rfloor$ Planes at $n\ge4$](simple-and-non-simple-rotations-one-angle-at-n-le-3-floor-n-2-planes-at-n-ge-4.html), for the angles and the planes.
- [The Rotor as a Square Root of a Rotation: $\mathrm{Spin}(n)\to\mathrm{SO}(n)$](the-rotor-as-a-square-root-of-a-rotation-spin-n-to-so-n.html), for the two-to-one cover of the rotations.
