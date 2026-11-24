# __The Fierz–Kofink Identities and the Classification of Spinors in $M_2(\mathbb{C})$__

## Introduction

**The question.** A spinor here is a matrix. Which operators of the module does it see, how many real numbers do they produce, which identities do those numbers satisfy, and how many types of spinor do the identities allow?

**Why it is the same statement.** This is the in-depth matrix reading of [The Fierz–Kofink Identities and the Classification of Spinors](the-fierz-kofink-identities-and-the-classification-of-spinors.html). The source's frame operators $\Gamma_0=iR_{\vec e_x}$, $\Gamma_k=iL_{\vec e_k}R_{\vec e_y}$, $\Gamma_5=-iR_{\vec e_z}$ act on the biquaternion algebra; in the display the module is $M_2(\mathbb{C})$ and the same operators act by left and right multiplication,
$$
\Gamma_0(Y)=iYE_x,\qquad \Gamma_k(Y)=iE_kYE_y,\qquad \Gamma_5(Y)=-iYE_z,
$$
with $E_k=-i\sigma_k$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The five operators as explicit $4\times4$ arrays in the coefficient basis, and the Clifford relations. The Hilbert–Schmidt form and the self-adjointness pattern. The sixteen covariants and their completeness. The Fierz–Kofink identities, scalar and tensor, with residuals. The Fierz aggregate as a rank-one matrix and its seven identities. The classification, with an explicit $2\times2$ matrix in each of the six classes. The two halves.

**What the article does not do.** It does not treat the internal, two-dimensional Fierz identity, which is [Bilinear Operators on a Hermitian Module with Hermitian Adjoint](bilinear-operators-on-a-hermitian-module-with-hermitian-adjoint.html); it does not treat the spinor spaces themselves, which is [Spinors and Dirac Spinors in the Biquaternion Algebra in $M_2(\mathbb{C})$](spinors-and-dirac-spinors-in-the-biquaternion-algebra-in-m2c.html).

**Conventions.** $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$. The coefficient basis is $\mathcal B=(\mathrm I_2,E_x,E_y,E_z)$ with $E_k=-i\sigma_k$, orthonormal for $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$. An operator on the module is a $4\times4$ array in $\mathcal B$. The sign vector is $\varepsilon=(1,-1,-1,-1)$, and indices run $0,1,2,3$ with $\Gamma_k$ the spacelike three.

**The arrays are coordinates.** The operators $\Gamma_\mu$ are canonical: each is left or right multiplication by a unit. The arrays printed below are their coordinates in $\mathcal B$, and they change if the basis changes. No array here is used to define an operator.

**Boundaries.** The operator algebra as a whole is [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure in $M_2(\mathbb{C})$](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure-in-m2c.html). The two-sided action is [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html). The chirality operator is [Operator Chirality on the Biquaternion Algebra in $M_2(\mathbb{C})$](operator-chirality-on-the-biquaternion-algebra-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $Ξ_{\mathrm{wfn}}$ a spinor, $E_\mu$ the basis with $E_0=\mathrm I_2$, $G_\mu$ the array of $\Gamma_\mu$, $Z$ the aggregate, $\sigma,\omega,J,K,S$ the covariants.

## The Frame Operators

**The five arrays.** In the order $(\mathrm I_2,E_x,E_y,E_z)$,
$$
G_0=\begin{pmatrix}0&-i&0&0\\ i&0&0&0\\0&0&0&i\\0&0&-i&0\end{pmatrix},\quad
G_1=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&-i&0&0\\ i&0&0&0\end{pmatrix},\quad
G_2=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},
$$
$$
G_3=\begin{pmatrix}0&-i&0&0\\ -i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},\quad
G_5=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix}.
$$

**The relations.** Verified exactly:
$$
G_0^2=\mathrm I_4,\qquad G_k^2=-\mathrm I_4,\qquad G_5^2=\mathrm I_4,\qquad G_\mu G_\nu+G_\nu G_\mu=0\ (\mu\neq\nu),\qquad G_5=iG_0G_1G_2G_3 .
$$

**Why they hold.** $R_{E_x}^2=R_{E_x^2}=R_{-\mathrm I_2}=-\mathrm{id}$, so $\Gamma_0^2=+1$; $L_{E_k}R_{E_y}$ squares to $L_{E_k^2}R_{E_y^2}=+\mathrm{id}$, so $\Gamma_k^2=-1$; and $\Gamma_5^2=+1$. Two distinct frame operators anticommute because the units anticommute on the side where they differ.

**The form.** $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$ is positive definite, and $\mathcal B$ is orthonormal. In this form $G_0$ and $G_5$ are Hermitian and the three $G_k$ are skew-Hermitian, verified: $\lVert G_k^{\dagger}+G_k\rVert=0$. Every covariant below is $\langleΞ_{\mathrm{wfn}},MΞ_{\mathrm{wfn}}\rangle$ with $M$ Hermitian, hence real.

## The Bilinear Covariants

**The definitions.**
$$
\sigma=\langleΞ_{\mathrm{wfn}},\Gamma_0Ξ_{\mathrm{wfn}}\rangle,\quad \omega=i\langleΞ_{\mathrm{wfn}},\Gamma_0\Gamma_5Ξ_{\mathrm{wfn}}\rangle,\quad J_0=\langleΞ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}}\rangle,\quad J_k=\langleΞ_{\mathrm{wfn}},\Gamma_0\Gamma_kΞ_{\mathrm{wfn}}\rangle,
$$
$$
K_0=-\langleΞ_{\mathrm{wfn}},\Gamma_0\Gamma_5\Gamma_0Ξ_{\mathrm{wfn}}\rangle,\quad K_k=-\langleΞ_{\mathrm{wfn}},\Gamma_0\Gamma_5\Gamma_kΞ_{\mathrm{wfn}}\rangle,\quad S_{\mu\nu}=\langleΞ_{\mathrm{wfn}},\Gamma_0\Sigma_{\mu\nu}Ξ_{\mathrm{wfn}}\rangle,\quad \Sigma_{\mu\nu}=\tfrac{i}{2}[\Gamma_\mu,\Gamma_\nu].
$$

**The count.** $1+1+4+4+6=16$ real numbers.

**The completeness.** The sixteen products $\mathrm{id}$, $\Gamma_\mu$, $\Gamma_\mu\Gamma_\nu$ ($\mu<\nu$), $\Gamma_5\Gamma_\mu$, $\Gamma_5$ are a basis of $\operatorname{End}_\mathbb{C}(M_2)$, of complex dimension sixteen; in the display this is the identity $\operatorname{End}_\mathbb{C}(M_2)\cong M_2\otimes M_2$ read on a basis. So every sesquilinear form is $\digamma_{\mathrm{map}}\mapsto\langle\digamma_{\mathrm{map}},MΞ_{\mathrm{wfn}}\rangle$ for one operator $M$, and the covariants are the coefficients of $M$.

**The matrix form of the completeness.** A linear operator on $M_2(\mathbb{C})$ is a sum of terms $Y\mapsto AYB$; the sixteen products above are the sixteen pairs $(A,B)$ in a suitable order, which is the statement that $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$.

## The Fierz–Kofink Identities

**The scalar identities.** With $J^2=J_0^2-J_1^2-J_2^2-J_3^2$ and the same for $K$ and $J\cdot K$,
$$
J^2=\sigma^2+\omega^2,\qquad J^2=-K^2,\qquad J\cdot K=0 .
$$
Verified on random spinors: the three residuals are $0$ to machine precision, and the first identity is the one that makes $J$ timelike for a regular spinor and null for a singular one.

**The tensor identity.** With the dual $\tilde S_{\mu\nu}=\tfrac12\sum_{\rho,\sigma}\varepsilon_\rho\varepsilon_\sigma\epsilon_{\mu\nu\rho\sigma}S_{\rho\sigma}$ and $\epsilon_{0123}=+1$,
$$
J_\mu K_\nu-J_\nu K_\mu=\omega S_{\mu\nu}+\sigma\tilde S_{\mu\nu}.
$$
Verified on random spinors to $0$ exactly; the opposite sign in the second term fails by a residual of order $10$, so the sign is not a convention here but a fact of the display.

**Why the tensor identity holds.** It is the antisymmetric part of the product of two rank-one operators. In matrix terms $J_\mu K_\nu-J_\nu K_\mu$ is the antisymmetrisation of $\langleΞ_{\mathrm{wfn}},\Gamma_\muΞ_{\mathrm{wfn}}\rangle\langleΞ_{\mathrm{wfn}},\Gamma_5\Gamma_\nuΞ_{\mathrm{wfn}}\rangle$, and the Fierz rearrangement of four spinor factors into two pairs gives the two scalars $\sigma$ and $\omega$ multiplying the two possible antisymmetric tensors, $S$ and its dual.

**The reading.** For a regular spinor $\sigma^2+\omega^2=J^2\neq0$, so $S$ is determined by $J$ and $K$. For a singular spinor $J$ is null and the identity becomes $J_\mu K_\nu=J_\nu K_\mu$: the axial vector is parallel to the null vector whenever it does not vanish.

## The Fierz Aggregate

**The operator.** $Z\eta=4Ξ_{\mathrm{wfn}}\langleΞ_{\mathrm{wfn}},\Gamma_0\eta\rangle$, which in the module is the rank-one matrix
$$
Z=4\,Ξ_{\mathrm{wfn}}\,Ξ_{\mathrm{wfn}}^{\dagger}\Gamma_0 .
$$
Its trace is $4\sigma$, and its image is the line $\mathbb{C}Ξ_{\mathrm{wfn}}$.

**The seven identities.** Verified on random spinors to $10^{-13}$:
$$
Z^2=4\sigma Z,\quad Z\Gamma_0Z=4J_0Z,\quad Z\Gamma_kZ=4J_kZ,\quad iZ\Gamma_5Z=4\omega Z,
$$
$$
Z\Gamma_0\Gamma_5Z=4K_0Z,\quad Z\Gamma_k\Gamma_5Z=4K_kZ,\quad Z\Sigma_{\mu\nu}Z=4S_{\mu\nu}Z .
$$
The first is one line: $Z^2=16Ξ_{\mathrm{wfn}}(Ξ_{\mathrm{wfn}}^{\dagger}\Gamma_0Ξ_{\mathrm{wfn}})Ξ_{\mathrm{wfn}}^{\dagger}\Gamma_0=4\sigma Z$.

**The inversion.** For a fixed $\zeta$ with $\langleΞ_{\mathrm{wfn}},\Gamma_0\zeta\rangle\neq0$, $Ξ_{\mathrm{wfn}}=Z\zeta/\left(4\langleΞ_{\mathrm{wfn}},\Gamma_0\zeta\rangle\right)$: the aggregate returns the spinor, which is Lounesto's boomerang. In the matrix reading it is the statement that a rank-one matrix is its own image.

## The Classification

**The six classes.** With the same conditions as the source: regular when $\sigma^2+\omega^2\neq0$, singular otherwise, and the singular ones separated by the vanishings of the vector $K$ and the tensor $S$.

| class | conditions | a representative matrix in the display |
|---|---|---|
| $1$ | $\sigma\neq0$, $\omega\neq0$ | $\begin{pmatrix}1&1-i\\1+i&1\end{pmatrix}$ |
| $2$ | $\sigma\neq0$, $\omega=0$ | $\tfrac12\begin{pmatrix}-1-i&-1-i\\1+i&1+i\end{pmatrix}$ |
| $3$ | $\sigma=0$, $\omega\neq0$ | $\tfrac12\begin{pmatrix}-1-i&1-i\\1-i&1+i\end{pmatrix}$ |
| $4$ | $\sigma=\omega=0$, $K\neq0$, $S\neq0$ | $\begin{pmatrix}0&-\tfrac12-\tfrac32 i\\ \tfrac12-\tfrac12 i&0\end{pmatrix}$ |
| $5$ | $\sigma=\omega=0$, $K=0$, $S\neq0$ | $\tfrac12\begin{pmatrix}1-i&0\\0&-1+i\end{pmatrix}$ |
| $6$ | $\sigma=\omega=0$, $K\neq0$, $S=0$ | $\begin{pmatrix}0&0\\1-i&0\end{pmatrix}$ |

**The values.** Verified on each representative: class $1$ has $\sigma=2$, $\omega=2$; class $2$ has $\sigma=1$, $\omega=0$; class $3$ has $\sigma=0$, $\omega=-1$; class $4$ has $K=(1,0,0,1)$ and $S\neq0$; class $5$ has $K=0$ and $S\neq0$; class $6$ has $K=(-1,0,0,-1)$ and $S=0$.

**The test that fails.** In classes $4$ and $6$ the vector $K$ is null, $K^2=0$, so a test on $K^2$ cannot separate class $6$ from class $5$. The test must be on the vector $K$ itself.

**The two halves.** With $P_\pm=\tfrac12(\mathrm{id}\pm\Gamma_0)$, the halves $\chi=P_+Ξ_{\mathrm{wfn}}$ and $\digamma_{\mathrm{map}}=P_-Ξ_{\mathrm{wfn}}$ give
$$
\sigma=\lVert\chi\rVert^2-\lVert\digamma_{\mathrm{map}}\rVert^2,\qquad \omega=2\operatorname{Im}\langle\chi,\Gamma_5\digamma_{\mathrm{map}}\rangle .
$$
So a spinor is regular exactly when the two halves have unequal lengths or a relative phase.

**A comparison of two splittings.** The halves $P_\pm$ are the eigenspaces of $\Gamma_0$ and have complex dimension two each; the Peirce halves $M_2P$ and $M_2P_{\perp}$ are also two-dimensional. They are different splittings of the same four-dimensional module: $\Gamma_0$ is $iR_{E_x}$, an operator of the two-sided algebra, and $P$ is a projection of the one-sided ideal structure.

## Where $n=2$ Differs

**The size of the module.** At $n=2$ the ambient module has complex dimension four, the frame operators are $4\times4$, and the sixteen products are a basis of $M_4(\mathbb{C})$. The classification is therefore a classification of four-component spinors, which is exactly the size the display provides.

**The Clifford algebra.** At $n=2$ the frame operators generate $\mathrm{Cl}_{1,3}$ acting on four complex dimensions, and the chirality operator $\Gamma_5$ is the product of the four. At order $n$ the module has dimension $n^2$ and the same five operators act on it; the covariants number $n^4$, and the six classes are not enough to classify them.

**What does not differ.** The five frame operators, their Clifford relations, the sixteen-term completeness, and the FPK identities are the same at every order, because they are statements about left and right multiplication by four units.

## Summary

The five frame operators are left and right multiplications by the units, $iR_{E_x}$, $iL_{E_k}R_{E_y}$, $-iR_{E_z}$; their arrays in the coefficient basis are printed above and satisfy the Clifford relations $G_0^2=G_5^2=\mathrm I_4$, $G_k^2=-\mathrm I_4$ and pairwise anticommutation.

A spinor produces sixteen real covariants $\sigma,\omega,J,K,S$, the coefficients of the sixteen basis operators of $\operatorname{End}_\mathbb{C}(M_2)$. They satisfy $J^2=\sigma^2+\omega^2=-K^2$, $J\cdot K=0$ and $J_\mu K_\nu-J_\nu K_\mu=\omega S_{\mu\nu}+\sigma\tilde S_{\mu\nu}$, all verified to machine precision. The aggregate $Z=4Ξ_{\mathrm{wfn}}Ξ_{\mathrm{wfn}}^{\dagger}\Gamma_0$ is rank one and satisfies the seven identities, and it inverts to the spinor.

The identities allow exactly six classes, regular and singular, and each is realised by an explicit $2\times2$ matrix; the singular classes are separated by the vector $K$ and the tensor $S$, not by $K^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma_0,\Gamma_k,\Gamma_5$ | the five frame operators |
| $G_\mu$ | their $4\times4$ arrays in $\mathcal B$ |
| $\sigma,\omega,J,K,S$ | scalar, pseudoscalar, vector, axial vector, tensor |
| $Z=4Ξ_{\mathrm{wfn}}Ξ_{\mathrm{wfn}}^{\dagger}\Gamma_0$ | the Fierz aggregate |
| $\tilde S$ | the Hodge dual of $S$ |
| $P_\pm=\tfrac12(\mathrm{id}\pm\Gamma_0)$ | the two halves |

## Further Reading

- [The Fierz–Kofink Identities and the Classification of Spinors](the-fierz-kofink-identities-and-the-classification-of-spinors.html), for the source's gamma reading and its literature.
- [Bilinear Operators on a Hermitian Module with Hermitian Adjoint](bilinear-operators-on-a-hermitian-module-with-hermitian-adjoint.html), for the internal two-dimensional Fierz identity.
- [Spinors and Dirac Spinors in the Biquaternion Algebra in $M_2(\mathbb{C})$](spinors-and-dirac-spinors-in-the-biquaternion-algebra-in-m2c.html), for the three levels of a spinor in the display.
- [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html), for the operators $Y\mapsto AYB$ that the frame operators are built from.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure in $M_2(\mathbb{C})$](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure-in-m2c.html), for $\operatorname{End}(M_2)\cong M_2\otimes M_2$.
- [Operator Chirality on the Biquaternion Algebra in $M_2(\mathbb{C})$](operator-chirality-on-the-biquaternion-algebra-in-m2c.html), for the chirality operator and its two eigenspaces.
