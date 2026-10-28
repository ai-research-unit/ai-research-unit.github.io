# __The Exponential Polar Decomposition of $M_4(\mathbb{C})$__

## Introduction

**Every invertible $A\in M_4(\mathbb{C})$ factors as $A=e^H e^{iK}$ with $H,K$ Hermitian; this is the left polar decomposition $A=P'U'$ written in exponential form.** The Hermitian factor $H$ is unique, the $*$-unitary factor $e^{iK}$ is unique, and the eigenvalues of $K$ are determined modulo $2\pi\mathbb{Z}$. The factorisation is different from the right polar decomposition $A=UP=e^{iK'}e^{H'}$: the two share the $*$-unitary factor, and their positive factors are conjugate by it. The two orderings coincide exactly when $A$ is normal, equivalently when $[H,K]=0$.

The article proves the exponential polar decomposition, relates it to the right polar decomposition, characterises the normal case, describes the Cartan decomposition and the singular case, and compares it with the chiral decomposition of the mass block.

The right polar decomposition is *The Polar Decomposition of $M_4(\mathbb{C})$*; the exponential is *The Exponential and the Lie Group of $M_4(\mathbb{C})$*; the chiral mass block is *The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$*; the spectral theory is *Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$*.

## The Left Polar Decomposition

**Theorem (left polar decomposition).** Every invertible $A\in M_4(\mathbb{C})$ has a unique decomposition

$$
A=P'U',
$$

with $P'$ positive definite Hermitian and $U'$ $*$-unitary:

$$
P'=(AA^*)^{1/2},\qquad
U'=P'^{-1}A.
$$

**Proof.** The matrix $AA^*$ is positive definite, so $P'=(AA^*)^{1/2}$ is positive definite and invertible. Set $U'=P'^{-1}A$. Then

$$
U'^*U'=A^*P'^{-2}A=A^*(AA^*)^{-1}A=I,
$$

so $U'$ is $*$-unitary. The decomposition is unique: $P'^2=AA^*$ forces $P'=(AA^*)^{1/2}$, and then $U'=P'^{-1}A$.

**The right polar decomposition.** The same $A$ has the right polar decomposition

$$
A=UP,\qquad
P=(A^*A)^{1/2},\qquad
U=AP^{-1}.
$$

**The relation between the two.** The $*$-unitary factors agree:

$$
U'=U,
$$

and the positive factors are conjugate:

$$
P'=UPU^*.
$$

**Proof.** From $A=UP$,

$$
AA^*=UPPU^*=UP^2U^*,
$$

so

$$
P'=(AA^*)^{1/2}=UPU^*,
$$

and

$$
U'=P'^{-1}A=(UPU^*)^{-1}UP=UP^{-1}U^*UP=U.
$$

**The two factors.** The left polar is the **positive-$*$-unitary** order $P'U'$; the right polar is the **$*$-unitary-positive** order $UP$. Both are canonical once the side is chosen.

## The Exponential Form

**The Hermitian logarithms.** Every positive definite $P'$ has a unique Hermitian logarithm:

$$
P'=e^{H},\qquad H=H^*,\qquad H=\log P'.
$$

Every $*$-unitary $U'$ has a Hermitian logarithm:

$$
U'=e^{iK},\qquad K=K^*,
$$

whose eigenvalues are determined modulo $2\pi\mathbb{Z}$. The principal logarithm chooses the eigenvalues in $(-\pi,\pi]$.

**Theorem (exponential polar decomposition).** Every invertible $A$ can be written as

$$
A=e^H e^{iK},
$$

with $H,K$ Hermitian. The factor $H$ is unique, the factor $e^{iK}$ is unique, and the eigenvalues of $K$ are determined modulo $2\pi\mathbb{Z}$.

**Proof.** Apply the left polar decomposition $A=P'U'$ and set $P'=e^H$, $U'=e^{iK}$. The uniqueness of $P'$ gives the uniqueness of $H$; the uniqueness of $U'$ gives the uniqueness of $e^{iK}$; the logarithm $K$ is unique modulo the lattice of periods of the exponential.

**The right exponential form.** The right polar decomposition gives

$$
A=e^{iK'}e^{H'},
$$

with

$$
H'=U^*HU,\qquad K'=K,
$$

because $P=U^*P'U=U^*e^HU=e^{U^*HU}$. The two exponential forms share the $*$-unitary factor and differ by the conjugation of the Hermitian factor.

**Example.** For a positive definite Hermitian $A=P$, the left and right polar decompositions are $A=P\cdot I$; the exponential form is $A=e^H$ with $K=0$. For a $*$-unitary $A=U$, the decomposition is $A=I\cdot U$; the exponential form is $A=e^{iK}$. For a scalar $A=re^{i\theta}$ with $r>0$, $A=e^{\log r}e^{i\theta}$, the two Hermitian factors are real scalars and commute.

## The Normal Case

**Theorem.** For invertible $A$ with exponential polar decomposition $A=e^H e^{iK}$, the following are equivalent:

1. $A$ is normal: $AA^*=A^*A$;
2. $H$ and $K$ commute: $[H,K]=0$;
3. the left and right exponential forms coincide: $H'=H$ and $K'=K$;
4. the left and right positive factors coincide: $P'=P$.

**Proof.** If $[H,K]=0$, then

$$
AA^*=e^He^{iK}e^{-iK}e^H=e^{2H},
\qquad
A^*A=e^{-iK}e^He^He^{iK}=e^{2H},
$$

so $A$ is normal. Conversely, if $A$ is normal, the right polar factors $U$ and $P$ commute; then $P'=UPU^*=P$, so $H'=H$ and $K'=K$, and $H$ and $K$ commute because they are functions of the commuting normal matrix $A$ (the spectral theorem). The equivalence of 2, 3 and 4 is immediate from $H'=U^*HU$ and $K'=K$.

**The spectral form.** If $A$ is normal, there is a $*$-unitary $V$ and diagonal real matrices $\Lambda,\Theta$ with

$$
A=Ve^{\Lambda}e^{i\Theta}V^*=e^{V\Lambda V^*}e^{iV\Theta V^*}.
$$

The Hermitian factors are simultaneously diagonalisable, and the eigenvalues of $A$ are $e^{\lambda_k+i\theta_k}$.

**The non-normal case.** For a non-normal $A$, the Hermitian factors do not commute, and the left and right exponential forms are genuinely different. The commutator $[H,K]$ is the obstruction to the two orderings coinciding.

## The Cartan Decomposition

**The group decomposition.** The exponential polar decomposition is the **left Cartan decomposition**

$$
GL_4(\mathbb{C})=\exp(\operatorname{Herm}_4)\,U(4),
$$

and the right polar decomposition is the **right Cartan decomposition**

$$
GL_4(\mathbb{C})=U(4)\,\exp(\operatorname{Herm}_4).
$$

Both maps

$$
P_+\times U(4)\longrightarrow GL_4,\qquad
(e^H,U)\longmapsto e^HU,
$$

$$
U(4)\times P_+\longrightarrow GL_4,\qquad
(U,e^H)\longmapsto Ue^H,
$$

are diffeomorphisms.

**The Lie algebra.** At the level of Lie algebras,

$$
\mathfrak{gl}_4=\operatorname{Herm}_4\oplus\mathfrak{u}(4),
$$

the Cartan decomposition with Cartan involution $\theta(X)=-X^*$. The exponential polar decomposition is the global form of the decomposition of the group, and the right polar decomposition is the other global form.

**The symmetric space.** The quotient

$$
GL_4/U(4)\cong P_+
$$

is the symmetric space of positive definite Hermitian matrices; the exponential map $\operatorname{Herm}_4\to P_+$ is a diffeomorphism. The left polar gives the trivialization $GL_4\cong P_+\times U(4)$, $g=P'U'\mapsto(P',U')$; the right polar gives the other trivialization $g=UP\mapsto(P,U)$. The two trivializations differ by the conjugation action of $U(4)$ on $P_+$.

**The uniqueness of the decomposition.** The factors $P'$ and $U'$ are unique. The exponent $K$ is not: different Hermitian logarithms of $U'$ differ by a Hermitian matrix whose eigenvalues lie in $2\pi\mathbb{Z}$ and which commutes with $U'$.

## The Singular Case

**No exponential polar for singular matrices.** If $A$ is singular, it has no factorisation $A=e^He^{iK}$ with $H,K$ Hermitian, because $e^H$ is invertible and $e^{iK}$ is $*$-unitary, so their product is invertible. The exponential polar decomposition exists exactly on $GL_4$.

**The polar decomposition survives.** The right polar decomposition $A=UP$ exists for every $A$, with $P$ positive semidefinite and $U$ a partial isometry; the left polar decomposition $A=P'U'$ exists with $P'=(AA^*)^{1/2}$ positive semidefinite and $U'$ a partial isometry. The exponential form requires the invertibility of $P$ and $P'$.

**The limit.** For a family $A(t)$ of invertible matrices tending to a singular $A(0)$, the Hermitian factor $H(t)=\log P(t)$ tends to $-\infty$ in the direction of the kernel; the $*$-unitary factor may have a limit or not. The exponential polar decomposition degenerates at the singular set, while the polar decomposition with the partial isometry continues.

**The singular values.** The singular values of $A$ are $e^{h_k}$, where $h_k$ are the eigenvalues of $H'$ in the right exponential form $A=e^{iK'}e^{H'}$. The exponential polar decomposition writes the singular values as exponentials of the Hermitian eigenvalues; the $*$-unitary factor carries the phases. At a zero singular value, the logarithm diverges.

## The Chiral Mass Block

**The chiral decomposition.** For the mass block $M\in M_2(\mathbb{C})$ of the rank-two split,

$$
M=U_L\Sigma U_R^*,
$$

with $U_L,U_R\in U(2)$ and $\Sigma$ diagonal nonnegative. This is the singular value decomposition of the block, not the exponential polar decomposition of the full algebra.

**The relation.** The full algebra's exponential polar decomposition applies to the $4\times4$ matrix; the chiral decomposition applies to the $2\times2$ mass block and uses two independent unitaries, one for each chirality. The two decompositions answer different questions: the exponential polar is the Cartan decomposition of $GL_4$; the chiral polar is the singular value decomposition of a map between the two chiral planes.

**The exponential form of the mass block.** For invertible $M$, the left polar decomposition is

$$
M=e^{H_M}e^{iK_M},
$$

with $H_M,K_M$ Hermitian $2\times2$ matrices. It is the $GL_2$ analogue of the full algebra's decomposition; the chiral decomposition is the $U(2)\times U(2)$ version.

## The Biquaternion Case

**At $n=2$ the theorem is the same.** For invertible $A\in M_2(\mathbb{C})$,

$$
A=e^He^{iK},\qquad H,K\in\operatorname{Herm}_2,
$$

with $H$ unique and $K$ unique modulo the choice of Hermitian logarithm. The left polar decomposition is $A=P'U'$ with $P'=(AA^*)^{1/2}$; the right polar is $A=UP$ with $P=(A^*A)^{1/2}$; the $*$-unitary factors agree and the positive factors are conjugate.

**The normal case.** For $M_2$, the exponential polar factors commute exactly when $A$ is normal; the spectral form is $A=Ve^{\Lambda}e^{i\Theta}V^*$ with $V\in U(2)$.

**The comparison.** The full algebra's exponential polar decomposition is the $4\times4$ version; the biquaternion algebra's is the $2\times2$ version. The positive definite cone and the $*$-unitary group are the same objects of the respective dimensions; the Cartan decomposition is the same theorem.

## Summary

Every invertible $A\in M_4(\mathbb{C})$ has a unique left polar decomposition $A=P'U'$ with $P'=(AA^*)^{1/2}$ positive definite and $U'=P'^{-1}A$ $*$-unitary. Writing $P'=e^H$ and $U'=e^{iK}$ gives the exponential polar decomposition

$$
A=e^He^{iK},
$$

with $H$ Hermitian unique and $K$ Hermitian with eigenvalues determined modulo $2\pi\mathbb{Z}$. The right polar decomposition is $A=UP=e^{iK'}e^{H'}$, with $U'=U$, $P'=UPU^*$, $H'=U^*HU$, $K'=K$. The two orderings coincide exactly when $A$ is normal, equivalently when $[H,K]=0$; then $A$ is unitarily diagonalisable with eigenvalues $e^{\lambda_k+i\theta_k}$. The decomposition is the left Cartan decomposition $GL_4=\exp(\operatorname{Herm}_4)U(4)$, the other global form being $GL_4=U(4)\exp(\operatorname{Herm}_4)$; both are diffeomorphisms $P_+\times U(4)\to GL_4$ and $U(4)\times P_+\to GL_4$. The exponential polar decomposition exists exactly on $GL_4$; it degenerates at the singular set, where the Hermitian logarithm diverges. The chiral mass block uses the singular value decomposition $M=U_L\Sigma U_R^*$, not the full algebra's exponential polar decomposition.

$$
\boxed{\ A=e^He^{iK}=P'U',\quad P'=(AA^*)^{1/2},\quad U'=P'^{-1}A,\quad H=H^*,\quad K=K^*,\quad [H,K]=0\iff A\text{ normal}. }
$$

| Object | Formula |
|---|---|
| Left polar | $A=P'U'$, $P'=(AA^*)^{1/2}$ |
| Right polar | $A=UP$, $P=(A^*A)^{1/2}$ |
| Relation | $U'=U$, $P'=UPU^*$ |
| Exponential polar | $A=e^He^{iK}$ |
| Right exponential | $A=e^{iK'}e^{H'}$, $H'=U^*HU$ |
| Normal case | $[H,K]=0$ |
| Cartan decomposition | $GL_4=\exp(\operatorname{Herm}_4)U(4)$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P'=(AA^*)^{1/2}$ | the left positive factor |
| $U'=P'^{-1}A$ | the left $*$-unitary factor |
| $P=(A^*A)^{1/2}$ | the right positive factor |
| $U=AP^{-1}$ | the right $*$-unitary factor |
| $H=\log P'$ | the Hermitian exponent of the positive factor |
| $K=-i\log U'$ | the Hermitian exponent of the $*$-unitary factor |
| $[H,K]$ | the commutator measuring non-normality |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the left and right polar decompositions and the normal case.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the Cartan decomposition and the symmetric space.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the exponential and the Cartan decomposition of $GL_4$.
- [The Polar Decomposition of $M_4(\mathbb{C})$](the-polar-decomposition-of-m4c.html), for the right polar decomposition and the singular value decomposition.
- [The Exponential and the Lie Group of $M_4(\mathbb{C})$](the-exponential-and-the-lie-group-of-m4c.html), for the matrix exponential and the Lie group structure.
- [The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$](the-mass-block-and-the-chiral-polar-decomposition-of-m4c.html), for the chiral decomposition of the mass block.
- [Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m4c.html), for the normal case and the spectral theorem.
