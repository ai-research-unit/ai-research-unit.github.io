# __The Cartan Hermitian Pairing of the Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

The Cartan Hermitian pairing writes an invertible biquaternion as a positive Hermitian factor times a unitary factor,

$$
\tilde Q=\tilde H\tilde V,
\qquad
\tilde H=\bigl(\tilde Q\tilde Q^{*}\bigr)^{1/2},
\qquad
\tilde V=\tilde H^{-1}\tilde Q.
$$

It is the polar decomposition of the unit group, and it is available on the whole complement of the null cone. On the N-regular, spectrally degenerate sector it survives without a root, without an angle and without an eigenbasis. It is therefore the pairing that remains closest to the element when the spectral reading collapses.

The sector adds one rigid feature: the product $\tilde H\tilde V$ is unipotent. The factors are not. This article states the factorization, identifies the two factors in the polar word, and reads the unipotence as the sector condition.

## The Pairing

**Theorem (the Cartan pairing on $\Sigma_{10}$).** Let $\tilde Q\in\Sigma_{10}$ and let $\Rho$ be its modulus. Then

$$
\tilde Q=\tilde H\tilde V,
\qquad
\tilde H=r\tilde U_{\mathrm b},
\qquad
\tilde V=e^{i\alpha}\tilde u_{\mathrm r},
$$

with $\tilde H$ positive Hermitian of determinant $r^2$ and $\tilde V$ unitary. The factorization is unique.

*Proof.* The element is invertible, so $\tilde Q\tilde Q^{*}$ is positive and invertible, and its positive square root $\tilde H$ exists and is unique. The factor $\tilde V=\tilde H^{-1}\tilde Q$ satisfies $\tilde V\tilde V^{*}=\tilde H^{-1}\tilde Q\tilde Q^{*}\tilde H^{-1}=e_t$, so it is unitary. The identification with $r\tilde U_{\mathrm b}$ and $e^{i\alpha}\tilde u_{\mathrm r}$ is the polar word of *Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion*. $\square$

The pairing groups the scale with the boost and the phase with the rotor. This is the opposite grouping to the Hamilton root pairing, which puts the scale and the phase in the modulus. The Cartan grouping is the one that makes both factors lie in groups: $\tilde H$ in the positive Hermitian space and $\tilde V$ in the unitary group.

### The Matrix Form

In the matrix model,

$$
\mathsf M(\tilde Q)=\mathsf M(\tilde H)\,\mathsf M(\tilde V),
$$

with $\mathsf M(\tilde H)$ positive definite of determinant $r^2$ and $\mathsf M(\tilde V)$ unitary. The matrix factorization is the polar decomposition of $\mathrm{GL}_2(\mathbb{C})$. It does not require diagonalizability, which is why it survives on the Jordan part.

## The Unipotent Product

The element is unipotent up to its scalar. Let

$$
\tilde U=\frac{\tilde Q}{\Rho}=\varepsilon\bigl(e_t+\vec\Upsilon\bigr),
\qquad
\vec\Upsilon^2=0,
\qquad
\varepsilon=\frac{Q_t}{\Rho}=\pm1.
$$

Then

$$
\bigl(\tilde U-\varepsilon e_t\bigr)^2=\vec\Upsilon^2=0,
$$

so $\tilde U$ is $\varepsilon$ times a unipotent element. The product of the Cartan factors is

$$
\tilde H\tilde V=\Rho\tilde U=Q_t\bigl(e_t+\vec\Upsilon\bigr),
$$

which is $Q_t$ times a unipotent element. This is the sector condition in the pairing.

**Proposition (the factors are not unipotent).** On the Jordan part, neither $\tilde H$ nor $\tilde V$ is unipotent. The positive factor has eigenvalues $r e^{\pm\psi/2}$, and the unitary factor has eigenvalues $e^{i(\alpha\pm\theta/2)}$. Their product has the double eigenvalue $\varepsilon$.

*Proof.* The eigenvalues of $\tilde U_{\mathrm b}$ are $e^{\pm\psi/2}$ because it is positive of determinant one; the eigenvalues of $\tilde u_{\mathrm r}$ are $e^{\pm i\theta/2}$ because it is a unit real quaternion; the phase shifts them by $e^{i\alpha}$. The product is $\tilde U$, whose only eigenvalue is $\varepsilon$. $\square$

The factors are diagonalizable, and the product is not. They cannot commute: if they did, their product would be normal and hence diagonalizable, contradicting the non-scalar Jordan block. The non-commutativity of $\tilde H$ and $\tilde V$ is therefore exactly the defect of the element, read in the Cartan pairing.

## The Two Signs

The sign $\varepsilon$ is the scalar part of the unit factor. It is the only discrete datum of the pairing that the spectrum also carries. The two cases are:

| Case | $\operatorname{Sc}\tilde U$ | $\tilde H$ | $\tilde V$ | $\tilde H\tilde V$ |
|---|---|---|---|---|
| positive | $+1$ | $r\tilde U_{\mathrm b}$ | $e^{i\alpha}\tilde u_{\mathrm r}$ | $Q_t(e_t+\vec\Upsilon)$ |
| negative | $-1$ | $r\tilde U_{\mathrm b}$ | $e^{i\alpha}\tilde u_{\mathrm r}$ | $Q_t(e_t+\vec\Upsilon)$ |

The factors have the same shape in both cases; the sign is carried by the scalar $Q_t$ and by the branch of $\Rho$. The pairing does not need a separate sign convention.

## Worked Example

Take

$$
\tilde Q=e_t+\vec e_x+i\vec e_y.
$$

The Cartan factors are

$$
\tilde H=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde V=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The positive factor has determinant one and eigenvalues $\sqrt2$ and $1/\sqrt2$; the unitary factor has determinant one and eigenvalues $e^{\pm i\pi/4}$. Their product is

$$
\tilde H\tilde V
=\left(\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2}\right)\frac{e_t+\vec e_x}{\sqrt2}
=e_t+\vec e_x+i\vec e_y,
$$

which is unipotent:

$$
\bigl(\tilde H\tilde V-e_t\bigr)^2
=\bigl(\vec e_x+i\vec e_y\bigr)^2=0.
$$

The factors do not commute. Their commutator is nonzero, and its size measures the Jordan defect. The example is the smallest one in which the Cartan pairing is nontrivial: the positive factor is not scalar and the unitary factor is not central, while the product is defective.

## Comparison with the Other Pairings

| Property | Cartan pairing | Quaternion pairing | Hamilton pairing |
|---|---|---|---|
| first factor | positive Hermitian | real quaternion modulus | complex modulus |
| second factor | unitary | exponential of a real quaternion | exponential of a root times an angle |
| survives $\Sigma_{10}$ | yes, without change | yes, with orthogonal data | no, the root fails |
| product on $\Sigma_{10}$ | unipotent up to $Q_t$ | regrouping of the same word | exact exponential of a nilpotent |
| spectral input | none | none | root and angle |

The Cartan pairing is the one that needs no spectral data at all. It is defined by the Hermitian structure alone, and the sector condition appears only in the unipotence of the product.

## Summary

### Main Results

| Item | Value |
|---|---|
| factorization | $\tilde Q=\tilde H\tilde V$ |
| positive factor | $\tilde H=r\tilde U_{\mathrm b}$, determinant $r^2$ |
| unitary factor | $\tilde V=e^{i\alpha}\tilde u_{\mathrm r}$, determinant $e^{2i\alpha}$ |
| product | $\tilde H\tilde V=Q_t(e_t+\vec\Upsilon)$, unipotent up to $Q_t$ |
| factor eigenvalues | $r e^{\pm\psi/2}$ and $e^{i(\alpha\pm\theta/2)}$ |
| product eigenvalue | $\varepsilon$, double |
| commutator | nonzero on the Jordan part |
| availability | all of $\Sigma_{10}$ |

### What the Pairing Shows

- The Cartan factorization is the polar decomposition of the unit group; it does not use the eigenbasis.
- The product is unipotent, but the factors are not; the defect is carried by their commutator.
- The phase sits with the rotor, not with the scale; this is the difference from the Hamilton pairing.
- The pairing survives the wall without a limit process.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}$ | the reduced product |
| $B^2=\langle\vec Q,\vec Q\rangle_{\natural}$ | the vector form |
| $\Sigma_{10}$ | the N-regular, spectrally degenerate sector |
| $\Rho=r e^{i\alpha}$ | the modulus |
| $\tilde U=\varepsilon(e_t+\vec\Upsilon)$ | the unit factor |
| $\tilde H=r\tilde U_{\mathrm b}$ | the positive Hermitian factor |
| $\tilde V=e^{i\alpha}\tilde u_{\mathrm r}$ | the unitary factor |
| $\psi,\theta$ | the rapidity and the rotor angle |
| $\varepsilon=\pm1$ | the sign of the scalar part of the unit factor |

## Further Reading

- [The Cartan Hermitian Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), for the regular pairing.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the word and the exact logarithm.
- [The Quaternion Pairing of the Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](the-quaternion-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the regrouping that keeps the real quaternion modulus.
