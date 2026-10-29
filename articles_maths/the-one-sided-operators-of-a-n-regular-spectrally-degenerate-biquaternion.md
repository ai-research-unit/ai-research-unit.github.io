# __The One-Sided Operators of a N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

The biquaternion algebra acts on itself by left and right multiplication. For a parameter $\tilde Q$ the two one-sided operators are

$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,
\qquad
R_{\tilde Q}(\tilde X)=\tilde X\tilde Q.
$$

On the N-regular, spectrally degenerate sector the parameter is $Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$. The one-sided operator is therefore a scalar times a unipotent operator. That single fact organizes the whole article: on the Jordan part the operator has one eigenvalue and two Jordan blocks, and a polar word whose factors are not unipotent individually.

The article reads the one-sided operator through the polar word and through the Jordan structure. The exponential of the operator and the locked angles are the companion *The One-Sided Operator Exponential of a N-Regular, Spectrally Degenerate Biquaternion*. It does not repeat the general theory of *The One-Sided Operators of a N-Regular, Spectrally Regular Biquaternion*; it states what the wall changes.

## The One-Sided Operators

The elementary properties are the same as in the regular sector:

$$
L_{\tilde Q}\circ L_{\tilde Q'}=L_{\tilde Q\tilde Q'},
\qquad
R_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'\tilde Q},
\qquad
L_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'}\circ L_{\tilde Q},
$$

and both are invertible exactly when $\tilde Q$ is a unit. On the sector, $\tilde Q$ is a unit, so both are invertible.

With the polar word $\tilde Q=\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}$,

$$
L_{\tilde Q}=L_{\Rho}\circ L_{\tilde U_{\mathrm b}}\circ L_{\tilde u_{\mathrm r}},
\qquad
R_{\tilde Q}=R_{\tilde u_{\mathrm r}}\circ R_{\tilde U_{\mathrm b}}\circ R_{\Rho},
$$

and $L_{\Rho}=R_{\Rho}=\Rho\,\mathrm{id}$. The modulus is central and acts by the same scalar on either side.

## The Jordan Structure

Let

$$
\tilde Q=Q_t\bigl(e_t+\vec\Upsilon\bigr),
\qquad
\vec\Upsilon^2=0,
\qquad
\vec\Upsilon\neq0.
$$

Then

$$
L_{\tilde Q}=Q_t\bigl(I+L_{\vec\Upsilon}\bigr),
\qquad
L_{\vec\Upsilon}^2=0,
\qquad
L_{\vec\Upsilon}\neq0.
$$

**Proposition (the two blocks).** The operator $L_{\vec\Upsilon}$ has rank two and kernel of dimension two. The operator $L_{\tilde Q}$ has the single eigenvalue $Q_t$, minimal polynomial $(X-Q_t)^2$, geometric multiplicity two and two Jordan blocks of size two. The same statements hold for $R_{\tilde Q}$.

*Proof.* The image of $L_{\vec\Upsilon}$ is the left ideal $\mathbb{B}\vec\Upsilon$, of complex dimension two because $\vec\Upsilon\neq0$ and $\vec\Upsilon^2=0$; the kernel is the right annihilator of $\vec\Upsilon$, also of complex dimension two. The square is zero, so the image lies in the kernel and both have dimension two. A nilpotent of index two on a four-dimensional space with rank two has two blocks of size two. Adding the scalar $Q_t$ shifts the eigenvalue and preserves the blocks.

The determinant and the trace follow from the matrix model:

$$
\det_{\mathbb{C}}L_{\tilde Q}=Q_t^4,
\qquad
\operatorname{tr}L_{\tilde Q}=4Q_t.
$$

The determinant is the fourth power of the scalar, not the square, because the left multiplication acts on the four-dimensional algebra. The trace is four times the scalar because the diagonal of $L_{\tilde Q}$ has the four entries $Q_t$.

## The Word One-Sided

The polar word splits the operator into four one-sided factors. The modulus is the scalar $\Rho\,\mathrm{id}$. The positive factor and the rotor act by left multiplication:

$$
L_{\tilde U_{\mathrm b}}(\tilde X)=\tilde U_{\mathrm b}\tilde X,
\qquad
L_{\tilde u_{\mathrm r}}(\tilde X)=\tilde u_{\mathrm r}\tilde X.
$$

Their product is the left multiplication by the unit factor,

$$
L_{\tilde U}=L_{\tilde U_{\mathrm b}}\circ L_{\tilde u_{\mathrm r}},
\qquad
\tilde U=\varepsilon\bigl(e_t+\vec\Upsilon\bigr).
$$

The product is unipotent up to $\varepsilon$, while the two factors are not. This is the one-sided form of the Cartan phenomenon: the operator $L_{\tilde U}$ has a double eigenvalue and two Jordan blocks, and its two polar factors are left multiplications by a positive element and a rotor, each with distinct eigenvalues.

The one-sided operator therefore sees the defect more directly than the element. The element is defective but scalar; the operator is defective on a four-dimensional space and exhibits the two blocks explicitly.

## Worked Example

Take $\tilde Q=e_t+\vec e_x+i\vec e_y$. In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$,

$$
\mathsf M(L_{\tilde Q})=
\begin{pmatrix}
1 & -1 & -i & 0\\
1 & 1 & 0 & i\\
i & 0 & 1 & -1\\
0 & -i & 1 & 1
\end{pmatrix},
\qquad
\mathsf M(L_{\vec\Upsilon})=
\begin{pmatrix}
0 & -1 & -i & 0\\
1 & 0 & 0 & i\\
i & 0 & 0 & -1\\
0 & -i & 1 & 0
\end{pmatrix}.
$$

The second matrix squares to zero and has rank two. The first is the identity plus the second, so it has the single eigenvalue $1$, two Jordan blocks of size two, determinant $1$ and trace $4$.

The polar factors are left multiplications by

$$
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

Their left multiplication matrices are not unipotent. Their product is the unipotent matrix above. The example shows the same contrast as the element-level article: the factors are diagonalizable, the product is not.



## The Image and the Kernel

Because $\tilde Q$ is a unit, $L_{\tilde Q}$ is invertible: its image is the whole algebra and its kernel is zero. The interesting image and kernel are those of $L_{\vec\Upsilon}$, not of $L_{\tilde Q}$.

The image of $L_{\vec\Upsilon}$ is the left ideal generated by $\vec\Upsilon$,

$$
\operatorname{im}L_{\vec\Upsilon}=\mathbb{B}\vec\Upsilon
=\mathbb{C}\{\vec\Upsilon,\vec\Upsilon\vec e_x,\vec\Upsilon\vec e_y,\vec\Upsilon\vec e_z\},
$$

of dimension two. The kernel is the right annihilator

$$
\ker L_{\vec\Upsilon}=\{\tilde X:\vec\Upsilon\tilde X=0\},
$$

also of dimension two. The kernel is the generalized eigenspace of $L_{\tilde Q}$ at $Q_t$; the image is the left ideal inside it. The Jordan blocks live on a complement to the kernel.

## Summary

### Main Results

| Item | Value |
|---|---|
| parameter | $\tilde Q=Q_t(e_t+\vec\Upsilon)$, $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$ |
| operator | $L_{\tilde Q}=Q_t(I+L_{\vec\Upsilon})$ |
| square | $L_{\vec\Upsilon}^2=0$ |
| rank of $L_{\vec\Upsilon}$ | $2$ |
| spectrum of $L_{\tilde Q}$ | $Q_t$, algebraic multiplicity four, geometric multiplicity two |
| Jordan form | two blocks of size two |
| determinant | $Q_t^4$ |
| trace | $4Q_t$ |
| polar word | $L_{\Rho}\circ L_{\tilde U_{\mathrm b}}\circ L_{\tilde u_{\mathrm r}}$ |
| defect | the factors are not unipotent; their product is |

At $\vec\Upsilon=0$ the element is $Q_t e_t$ and $L_{\tilde Q}=Q_t I_4$: spectrum $Q_t$ with algebraic and geometric multiplicity four, Jordan type $1+1+1+1$. The table describes the Jordan part.

### What the Operator Shows

- On the Jordan part the one-sided operator is unipotent up to the scalar, with two explicit Jordan blocks.
- The polar factors are left multiplications by a positive element and a rotor; neither is unipotent.
- The defect of the element is visible as the non-commutativity of the factors and as the off-diagonal entries of the blocks.
- The image and kernel of the nilpotent part are left and right ideals of dimension two.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}$ | the reduced product |
| $B^2=\langle\vec Q,\vec Q\rangle_{\natural}$ | the vector form |
| $\Sigma_{10}$ | the N-regular, spectrally degenerate sector |
| $\vec\Upsilon=\vec Q/Q_t$ | the null vector of the normal form |
| $L_{\tilde Q},R_{\tilde Q}$ | left and right multiplication by $\tilde Q$ |
| $\Rho$ | the modulus |
| $\tilde U_{\mathrm b},\tilde u_{\mathrm r}$ | the positive factor and the rotor |
| $\psi,\theta$ | the rapidity and the rotor angle |
| $\vec A,\vec B$ | the real and imaginary parts of $\vec\Upsilon$ |
| $a$ | the null parameter, $\lvert\vec A\rvert=\lvert\vec B\rvert=a$ |
| $L_{\vec\Upsilon}$ | left multiplication by the null vector |

## Further Reading

- [The One-Sided Operators of a N-Regular, Spectrally Regular Biquaternion](the-one-sided-operators-of-a-n-regular-spectrally-regular-biquaternion.html), for the general one-sided theory.
- [The One-Sided Operator Exponential of a N-Regular, Spectrally Degenerate Biquaternion](the-one-sided-operator-exponential-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the shear, the exact exponent and the locked angles.
- [The Sandwich of a N-Regular, Spectrally Degenerate Biquaternion](the-sandwich-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the sandwich.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the word and the exact logarithm.
