# __The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions__

## Introduction

The Cartan Hermitian pairing is the split of a biquaternion into a **positive Hermitian factor** and a **unitary factor**,

$$
\tilde Q=\tilde H\,\tilde U,
\qquad
\tilde H=\sqrt{\tilde Q\tilde Q^{*}},
\qquad
\tilde U=\tilde H^{-1}\tilde Q,
$$

with $\tilde H$ Hermitian positive definite and $\tilde U$ unitary. In the polar word,

$$
\tilde H=r\,\tilde U_{\mathrm b},
\qquad
\tilde U=\exp(i\alpha)\,\tilde u_{\mathrm r}.
$$

The Hermitian factor carries the scale and the boost; the unitary factor carries the phase and the rotor. The pairing is the matrix polar decomposition of $\mathrm{GL}(2,\mathbb{C})$, read in the algebra. It is the decomposition that separates the **stretch** of a linear map from its **turn**.

The article defines the two factors, identifies the pairing with the Cartan decomposition of the Lorentz group, gives the physical reading, records the domain and the boundary at the null cone, and works the three reference instances: a general element, a four-position and a pure Lorentz rotor.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and central $i$. An element is $\tilde Q=Q_te_t+\vec Q$, with complex coefficients. The Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$, the norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$, and the polar word is

$$
\tilde Q=r\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r},
\qquad
\rho=r\exp(i\alpha)=\sqrt{\langle\tilde Q\rangle_{\natural}},
$$

with $\tilde U_{\mathrm b}=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$ Hermitian positive of unit norm and $\tilde u_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ a unit real quaternion. The matrix model is $\mathsf M_2$, with $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$ and $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.

The physics articles write $B=\tilde U_{\mathrm b}$ and $\tilde q=\tilde u_{\mathrm r}$; the present article uses the mathematics glyphs.

## The Hermitian Factor

The Hermitian factor is

$$
\tilde H=\sqrt{\tilde Q\tilde Q^{*}}.
$$

The product $\tilde Q\tilde Q^{*}$ is Hermitian and positive semidefinite:

$$
(\tilde Q\tilde Q^{*})^{*}=\tilde Q\tilde Q^{*},
\qquad
\mathsf M_2(\tilde Q\tilde Q^{*})=\mathsf M_2(\tilde Q)\mathsf M_2(\tilde Q)^{\dagger}\succeq0.
$$

When the norm does not vanish, the matrix is invertible, so the product is positive definite and has a unique positive definite square root. That root is $\tilde H$.

In the polar word, $\tilde Q\tilde Q^{*}=r^{2}\tilde U_{\mathrm b}^{2}$, because $\tilde U_{\mathrm b}$ is Hermitian and $\tilde u_{\mathrm r}$ is unitary. Hence

$$
\tilde H=r\tilde U_{\mathrm b}.
$$

The Hermitian factor is the scale times the boost. It is positive definite, of determinant $r^{2}$, and its eigenvalues are $r\exp(\pm\psi/2)$.

**The trace and the Hilbert–Schmidt norm.** The trace of $\tilde H$ is

$$
\operatorname{tr}\tilde H=2r\cosh\frac{\psi}{2},
$$

and the Hilbert–Schmidt square is

$$
\operatorname{tr}(\tilde H^{2})=\operatorname{tr}(\tilde Q\tilde Q^{*})=2r^{2}\cosh\psi.
$$

The two are not the same function of the boost: the trace weights the two singular values additively, the Hilbert–Schmidt square weights their squares. The determinant is their product, $r^{2}$.

**The singular values.** The eigenvalues of $\tilde H$ are the singular values of $\mathsf M_2(\tilde Q)$,

$$
\sigma_{\pm}=r\exp(\pm\psi/2).
$$

The scale is their geometric mean, $r=\sqrt{\sigma_+\sigma_-}$; the boost is their ratio, $e^{\psi}=\sigma_+/\sigma_-$. The Hermitian factor is therefore the singular-value factor of the matrix, and the unitary factor is the orthogonal factor.

## The Unitary Factor

The unitary factor is

$$
\tilde U=\tilde H^{-1}\tilde Q.
$$

It is unitary:

$$
\tilde U\tilde U^{*}
=\tilde H^{-1}\tilde Q\tilde Q^{*}\tilde H^{-1}
=\tilde H^{-1}\tilde H^{2}\tilde H^{-1}
=e_t.
$$

In the polar word,

$$
\tilde U=\exp(i\alpha)\tilde u_{\mathrm r}.
$$

The unitary factor is the phase times the rotor. Its determinant is $\exp(2i\alpha)$, of modulus one; its eigenvalues are $\exp(i(\alpha\pm\theta/2))$. It is the compact factor of the decomposition.

**The two factors commute?** In general they do not. The Hermitian factor is a boost and the unitary factor is a phase times a rotor; the boost and the rotor do not commute. The product $\tilde H\tilde U$ is therefore ordered: the Hermitian factor acts first on the left, and the unitary factor on the right. The matrix polar decomposition is ordered in the same way, $A=HU$.

**The inverse order.** The product $\tilde U\tilde H$ is a different element unless the two factors commute. The two orders are related by conjugation,

$$
\tilde U\tilde H=\tilde H\,(\tilde H^{-1}\tilde U\tilde H),
$$

and the conjugated unitary factor is the unitary factor in the frame rotated by the Hermitian one. The polar decomposition is unique in the order $HU$; the other order is a different reading of the same factors.

## The Cartan Involution and the Decomposition

The Cartan involution of $\mathrm{GL}(2,\mathbb{C})$ is

$$
\theta(g)=(g^{\dagger})^{-1}.
$$

Its fixed group is the unitary group $\mathrm{U}(2)$, and its $-1$ eigenspace is the positive Hermitian cone. The Cartan decomposition writes every invertible $g$ as

$$
g=h\,u,
\qquad
h=\sqrt{gg^{\dagger}},
\qquad
u=h^{-1}g,
$$

with $h$ positive Hermitian and $u$ unitary. The decomposition is global: every invertible matrix has it, uniquely.

In the algebra, the same statement is

$$
\tilde Q=\tilde H\tilde U,
\qquad
\tilde H=\sqrt{\tilde Q\tilde Q^{*}},
\qquad
\tilde U=\tilde H^{-1}\tilde Q.
$$

The involution acts on the factors as

$$
\theta(\tilde H)=\tilde H^{-1},
\qquad
\theta(\tilde U)=\tilde U.
$$

The Hermitian factor is inverted and the unitary factor is fixed. The decomposition is the eigenspace decomposition of the involution at the group level: the positive cone is the $-1$ eigenspace, the unitary group is the fixed group.

**The relation to the polar word.** The polar word has four factors; the Cartan pairing groups them two by two:

$$
\tilde H=r\tilde U_{\mathrm b},
\qquad
\tilde U=\exp(i\alpha)\tilde u_{\mathrm r}.
$$

The scale and the boost are the Hermitian factor; the phase and the rotor are the unitary factor. The pairing is therefore the split between the **non-compact** and the **compact** data of the element, with the central phase on the compact side.

On the Lorentz group, $r=1$ and $\alpha=0$, so $\tilde H=\tilde U_{\mathrm b}$ and $\tilde U=\tilde u_{\mathrm r}$. The Cartan pairing is then the Cartan decomposition of $SL(2,\mathbb{C})$,

$$
\tilde U_L=\tilde U_{\mathrm b}\tilde u_{\mathrm r},
$$

with $\tilde U_{\mathrm b}$ positive definite. The positivity is exactly the condition that removes the sign ambiguity of the decomposition.

## The Physical Reading

The Cartan pairing is the **amplitude-phase** reading of the element.

- **The Hermitian factor is the amplitude.** It is positive, it carries the scale and the boost, and its eigenvalues are the singular values. In a quantum reading, it is the positive factor of a matrix acting on a state: the part that changes norms, not phases.
- **The unitary factor is the phase.** It is unitary, it carries the central phase and the rotor, and its eigenvalues are phases. In a quantum reading, it is the part that preserves the inner product: the gauge phase and the spin rotation.
- **The determinant is the product.** $\det\tilde H=r^{2}$ and $\det\tilde U=\exp(2i\alpha)$, so $\det\tilde Q=r^{2}\exp(2i\alpha)$. The scale is the modulus of the determinant, the phase is half its argument, and the boost and rotor are the anisotropy and the turn of the two factors.

In the relativistic reading, the Hermitian factor is the boost times the dilation, and the unitary factor is the rotation times the phase. The boost is the non-compact part, the rotation is the compact part, and the phase is the central part. The Cartan pairing is the group-level statement of the same split that the polar word makes factor by factor.

The reading is a dictionary. The mathematics is the matrix polar decomposition; the physics is the identification of the factors with the amplitude, the phase, the boost and the spin.

## The Domain and the Null Cone

The Cartan pairing exists exactly when $\langle\tilde Q\rangle_{\natural}\neq0$. At the null cone,

$$
\tilde Q\tilde Q^{*}
$$

is positive semidefinite of rank one, with a zero eigenvalue. The positive square root exists but is not positive definite, and the inverse $\tilde H^{-1}$ does not exist. The unitary factor is undefined.

The failure is the same failure as the polar word. On the material sector, the null cone is the light cone; on the informational sector, it is the cone of rank-one Hermitian matrices. The Hermitian factor is the density matrix of a pure state on that cone, and the unitary factor is the phase that the pure state does not have. The polar decomposition of an invertible matrix stops at the boundary.

At the boundary, the two factors can be separated in a limiting sense: $\tilde H$ tends to the rank-one positive matrix and $\tilde U$ tends to a unitary matrix defined only on the range. The limit is not unique, which is the algebraic form of the absence of a rest frame for a null vector.

## Worked Examples

### A General Element

Take

$$
\tilde Q=(1+i)e_t+\vec e_x+2\vec e_y.
$$

The norm is $5+2i$, so $\rho=2.320595787\exp(0.190253189i)$, $r=2.320595787$ and $\alpha=0.190253189$. The Hermitian product is

$$
\tilde Q\tilde Q^{*}=7e_t-2i\vec e_x-4i\vec e_y,
$$

whose positive square root is

$$
\tilde H=2.488489985\,e_t-0.401850120\,i\vec e_x-0.803700241\,i\vec e_y.
$$

The unitary factor is

$$
\tilde U=0.462100989+0.088992519i\,e_t+0.387479295+0.074621694i\,\vec e_x+0.774958590+0.149243388i\,\vec e_y,
$$

written with the scalar and vector parts separated. The product is $\tilde H\tilde U=\tilde Q$, and $\tilde U\tilde U^{*}=e_t$. The determinant of $\tilde H$ is $5.385164807=r^{2}$; its trace is $4.976979969=2r\cosh(\psi/2)$; its Hilbert–Schmidt square is $14=2r^{2}\cosh\psi$. The reconstruction holds to $7.1\times10^{-15}$.

### A Four-Position

Take $\tilde X=i e_t+0.6\vec e_x$. The norm is $-0.64$, so $r=0.8$ and $\alpha=\pi/2$. The Hermitian product is

$$
\tilde X\tilde X^{*}=0.64e_t-1.2i\vec e_x,
$$

and its positive square root is

$$
\tilde H=1.0e_t-0.6i\vec e_x.
$$

The unitary factor is $\tilde U=i$. Hence

$$
\tilde X=\tilde H\tilde U=(1.0-0.6i\vec e_x)i=i+0.6\vec e_x.
$$

The Hermitian factor is the four-velocity times the scale, and the unitary factor is the $ict$ phase. The determinant of $\tilde H$ is $0.64$, the interval; the phase is the argument of the determinant.

### A Pure Lorentz Rotor

Take $\tilde Q=\tilde U_L=\cosh(\psi/2)e_t+i\sinh(\psi/2)\vec e_x$ with $\psi=0.693147181$. The norm is one, so $r=1$ and $\alpha=0$. The Hermitian factor is $\tilde H=\tilde Q$, and the unitary factor is $\tilde U=e_t$. The Cartan pairing returns the boost alone. If the rotor is present,

$$
\tilde Q=\tilde U_{\mathrm b}\tilde u_{\mathrm r},
\qquad
\tilde H=\tilde U_{\mathrm b},
\qquad
\tilde U=\tilde u_{\mathrm r},
$$

and the pairing separates the boost from the rotation.

### A Null Element

Take $\tilde Q=i e_t+\vec e_x$. The norm is zero. The product $\tilde Q\tilde Q^{*}$ is rank one, with a zero eigenvalue; $\tilde H$ is not invertible, and $\tilde U$ is undefined. The element is a zero divisor and a lightlike four-vector. The Cartan pairing fails at the same point as the polar word.

## The Cartan Pairing and the Other Pairings

The Cartan pairing is the only one of the three pairings that is the matrix polar decomposition without a partial construction.

| pairing | factors | condition |
|---|---|---|
| quaternion | $\tilde q=r\tilde u_{\mathrm r}$ and $\exp(i\tilde\Psi)$ | $\tilde q_r\neq0$ and $N\neq0$ |
| Hamilton | $\rho$ and $\cos\Theta+\vec\Xi\sin\Theta$ | $\vec Q\cdot\vec Q\neq0$ and $N\neq0$ |
| Cartan | $\tilde H=r\tilde U_{\mathrm b}$ and $\tilde U=\exp(i\alpha)\tilde u_{\mathrm r}$ | $N\neq0$ |

The Cartan pairing needs only the norm. The quaternion pairing needs the real part; the Hamilton pairing needs the vector square. The three pairings are three readings of one word, and the Cartan pairing is the one that is defined on the whole complement of the null cone.

The Cartan pairing is also the one that is most directly the matrix polar decomposition. The Hermitian factor is the positive square root of $AA^{\dagger}$, and the unitary factor is $H^{-1}A$. The quaternion and Hamilton pairings are coordinate constructions in the algebra; the Cartan pairing is the geometric decomposition of the linear map.

## Summary

The Cartan Hermitian pairing writes a biquaternion as a positive Hermitian factor times a unitary factor, $\tilde Q=\tilde H\tilde U$, with $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ and $\tilde U=\tilde H^{-1}\tilde Q$. In the polar word, $\tilde H=r\tilde U_{\mathrm b}$ and $\tilde U=\exp(i\alpha)\tilde u_{\mathrm r}$: the Hermitian factor carries the scale and the boost, the unitary factor carries the phase and the rotor. The pairing is the matrix polar decomposition of $\mathrm{GL}(2,\mathbb{C})$ and the Cartan decomposition of $SL(2,\mathbb{C})$ on the unit-norm slice. It exists exactly off the null cone; at the cone the Hermitian factor becomes rank one and the unitary factor is undefined. The determinant gives the scale and the phase, the singular values give the scale and the boost, and the eigenvalues of the unitary factor give the phase and the rotation.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ | the positive Hermitian factor |
| $\tilde U=\tilde H^{-1}\tilde Q$ | the unitary factor |
| $\tilde H=r\tilde U_{\mathrm b}$ | the Hermitian factor in the polar word |
| $\tilde U=\exp(i\alpha)\tilde u_{\mathrm r}$ | the unitary factor in the polar word |
| $\sigma_\pm=r\exp(\pm\psi/2)$ | the singular values |
| $r,\alpha,\psi,\theta$ | the scale, phase, rapidity and rotation angle |
| $\theta(g)=(g^{\dagger})^{-1}$ | the Cartan involution |
| $B,\tilde q$ | the physics glyphs for the boost and the rotor |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_physics/the-polar-element-representation-of-biquaternions.md`), the polar word and its four factors.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), the mathematics reference.
- *The Quaternion Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.md`), the real-quaternion reading.
- *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.md`), the axis-angle reading.
- *The Polar Decomposition of Biquaternions in Practice* (`articles_physics/the-polar-decomposition-of-biquaternions-in-practice.md`), the algorithm.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), the matrix polar decomposition.
