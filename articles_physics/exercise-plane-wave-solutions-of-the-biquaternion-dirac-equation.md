# __Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation__

## Introduction

This is a worked exercise on the biquaternion Dirac equation, written **in the biquaternion algebra**. No gamma matrix and no four-component column is used: the symbols $\gamma^\mu$ and $\gamma_5$ below name left and right multiplications, not matrices. The parent article, *The Biquaternion Dirac Equation — Solutions and the Non-Relativistic Limit*, supplies the equation, the field, the two bases, and the mass shell. The present exercise re-derives the parent's results in the algebra and supplies what the parent leaves implicit: the explicit spinors, the normalisation in the biquaternion pairing, the spin sums as operator identities, the massless limit, the algebra of the generators and the change of basis.

The translation is a dictionary of operators. A Dirac spinor is a biquaternion $\tilde\Psi$. Write $R_a$ and $L_a$ for right and left multiplication,

$$
R_a(\tilde Q)=\tilde Q a,\qquad L_a(\tilde Q)=a\tilde Q .
$$

Then the Dirac generators and the chirality operator are

$$
\gamma^0=R_{i\vec e_x},\qquad \gamma^k=L_{i\vec e_k}R_{\vec e_y},\qquad \gamma_5=R_{-i\vec e_z}.
$$

The check is the algebra itself. Since $R$ and $L$ commute and $(i\vec e_x)^2=(i\vec e_k)^2=e_t$, while $\vec e_y^2=-e_t$,

$$
(\gamma^0)^2=R_{e_t}=1,\qquad (\gamma^k)^2=L_{e_t}R_{-e_t}=-1,
$$

$$
\gamma^0\gamma^k+\gamma^k\gamma^0=L_{i\vec e_k}\bigl(R_{i\vec e_z}+R_{-i\vec e_z}\bigr)=0,\qquad
\gamma^j\gamma^k+\gamma^k\gamma^j=L_{\vec e_j\vec e_k+\vec e_k\vec e_j}=0 .
$$

So $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$ with $g=\mathrm{diag}(+1,-1,-1,-1)$, without a matrix.

**The field and its two Peirce components.** Let

$$
\tilde\Pi_+=\frac{e_t+i\vec e_z}{2},\qquad \tilde\Pi_-=\frac{e_t-i\vec e_z}{2},
$$

be the Peirce idempotents, and let

$$
\vec\Upsilon_x=\frac{i\vec e_x-\vec e_y}{2},\qquad \vec\Upsilon_y=\frac{i\vec e_x+\vec e_y}{2}
$$

be the off-diagonal matrix units, so that $\{\tilde\Pi_+,\vec\Upsilon_y\}$ is a basis of $\mathbb{B}\tilde\Pi_+$ and $\{\vec\Upsilon_x,\tilde\Pi_-\}$ is a basis of $\mathbb{B}\tilde\Pi_-$. A two-component spinor $\chi=(\chi_1,\chi_2)$ is realised in the algebra by

$$
\Psi_+(\chi)=\chi_1\tilde\Pi_++\chi_2\vec\Upsilon_y\in\mathbb{B}\tilde\Pi_+,\qquad
\Psi_-(\chi)=\chi_1\vec\Upsilon_x+\chi_2\tilde\Pi_-\in\mathbb{B}\tilde\Pi_- .
$$

The field is

$$
\tilde\Psi=\Psi_+(\psi_+)+\Psi_-(\psi_-),
$$

with $\psi_\pm\in\mathbb{C}^2$ its two Peirce coordinates. The Peirce components are $\tilde\Psi_\pm=\tilde\Psi\tilde\Pi_\pm$. In the chiral basis they are the two chiralities, $\psi_+$ left-handed and $\psi_-$ right-handed, and they are selected by the projectors

$$
P_L=\frac{1-\gamma_5}{2}=R_{\tilde\Pi_+},\qquad P_R=\frac{1+\gamma_5}{2}=R_{\tilde\Pi_-},
\qquad \tilde\Psi_+=P_L\tilde\Psi,\quad \tilde\Psi_-=P_R\tilde\Psi .
$$

In the Dirac basis the same two components are the large and the small component; they are still the Peirce components, but there they are not the chirality projectors.

**The momentum-space operator.** For a plane wave of four-momentum $p^\mu=(E,\vec p)$, the Dirac operator is

$$
\not p=\gamma^0E-\gamma^k p_k=E\,R_{i\vec e_x}-p_k\,L_{i\vec e_k}R_{\vec e_y},
$$

and the equation is $\not p\,\tilde\Psi=m\tilde\Psi$. Written on the element,

$$
E\,\tilde\Psi\,i\vec e_x-(\vec p\cdot\vec e)\,\tilde\Psi\,\vec e_y=m\,\tilde\Psi .
$$

In Peirce coordinates this is the pair

$$
(E-\boldsymbol\sigma\cdot\vec p)\,\psi_-=m\,\psi_+,\qquad
(E+\boldsymbol\sigma\cdot\vec p)\,\psi_+=m\,\psi_- ,
$$

in the chiral basis, and

$$
(E-m)\,\psi_+=(\boldsymbol\sigma\cdot\vec p)\,\psi_-,\qquad
(E+m)\,\psi_-=(\boldsymbol\sigma\cdot\vec p)\,\psi_+
$$

in the Dirac basis. The two pairs are the same equation in the two bases.

**Conventions.** Natural units $\hbar=c=1$ in the solutions; $\hbar$ and $c$ are restored in Problem 6. The metric of the spacetime gradient is $\eta=\mathrm{diag}(-1,+1,+1,+1)$, and the Clifford metric of the generators is $g=-\eta$. The two-spinors are $\xi^{(1)}=(1,0)^T$, $\xi^{(2)}=(0,1)^T$, with $\xi^{(r)\dagger}\xi^{(s)}=\delta^{rs}$; $\chi_\pm$ are the helicity eigenspinors, $\boldsymbol\sigma\cdot\vec u_p\,\chi_\pm=\pm\chi_\pm$, with $\vec u_p=\vec p/|\vec p|$. The Hermitian conjugate $^*$ is the coefficient conjugation composed with the quaternion conjugation, $\tilde Q^*=\overline{\tilde Q^\natural}$, and under the matrix representation $\mathsf{M}_2$ it is the conjugate transpose.

The six problems are: **(1)** the spinors at rest and at general momentum; **(2)** the covariant normalisation and the orthogonality; **(3)** the spin sums; **(4)** the massless limit and the helicity–chirality locking; **(5)** the algebra of the generators and the change of basis; **(6)** the biquaternionic mass shell.

## Problem 1: The spinors at rest and at general momentum

**Statement.** Solve $\not p\,\tilde w=m\tilde w$ and $\not p\,\tilde v=-m\tilde v$ explicitly at rest and at general momentum, in the chiral and in the Dirac basis.

**Solution.** The equation was written above as a pair on the Peirce coordinates. In the **chiral basis** the pair is

$$
(E-\boldsymbol\sigma\cdot\vec p)\,\psi_-=m\psi_+,\qquad (E+\boldsymbol\sigma\cdot\vec p)\,\psi_+=m\psi_- .
$$

Eliminating $\psi_-$ gives $(E^2-\vec p^2)\psi_+=m^2\psi_+$, so the pair is soluble exactly on the mass shell $E^2=\vec p^2+m^2$. For the positive-frequency branch, take $\psi_+=\sqrt{E\mp|\vec p|}\,\chi_\pm$; the first equation gives $\psi_-=\sqrt{E\pm|\vec p|}\,\chi_\pm$. The helicity label is fixed by the sign: the two solutions are

$$
\boxed{\;\tilde w_\pm(\vec p)=\sqrt{E\mp|\vec p|}\;\Psi_+(\chi_\pm)+\sqrt{E\pm|\vec p|}\;\Psi_-(\chi_\pm)\;}
$$

For the negative-frequency branch, the same pair with $m\to-m$ gives $\psi_+=-\sqrt{E\mp|\vec p|}\,\chi_\pm$ and $\psi_-=\sqrt{E\pm|\vec p|}\,\chi_\pm$:

$$
\boxed{\;\tilde v_\pm(\vec p)=-\sqrt{E\mp|\vec p|}\;\Psi_+(\chi_\pm)+\sqrt{E\pm|\vec p|}\;\Psi_-(\chi_\pm)\;}
$$

**At rest.** With $\vec p=0$ and $E=m$, the two branches lie in the right ideals $\mathbb{B}\frac12(1\pm i\vec e_x)$:

$$
\tilde w(0)\,(1-i\vec e_x)=0,\qquad \tilde v(0)\,(1+i\vec e_x)=0 .
$$

Equivalently, the positive-frequency amplitude has equal Peirce coordinates and the negative-frequency amplitude has opposite ones:

$$
\tilde w_\pm(0)=\sqrt{m}\,\bigl(\Psi_+(\chi_\pm)+\Psi_-(\chi_\pm)\bigr),\qquad
\tilde v_\pm(0)=\sqrt{m}\,\bigl(-\Psi_+(\chi_\pm)+\Psi_-(\chi_\pm)\bigr).
$$

The two rest amplitudes are therefore the two eigenspaces of $R_{i\vec e_x}$; each is two-dimensional over $\mathbb{C}$, and the two spin states are the two choices of $\chi_\pm$.

**The Dirac basis.** The change of basis is right multiplication by the unit biquaternion

$$
\tilde W=\frac{e_t+\vec e_y}{\sqrt2},\qquad \tilde W^{-1}=\tilde W^{\natural}=\frac{e_t-\vec e_y}{\sqrt2},
$$

as Problem 5 shows. In the Dirac basis the pair is $(E-m)\psi_+=(\boldsymbol\sigma\cdot\vec p)\psi_-$ and $(E+m)\psi_-=(\boldsymbol\sigma\cdot\vec p)\psi_+$, and the solutions are

$$
\boxed{\;\tilde w^{(r)}(\vec p)=\sqrt{E+m}\;\Psi_+(\xi^{(r)})+\sqrt{E-m}\;\Psi_-(\boldsymbol\sigma\cdot\vec u_p\,\xi^{(r)})\;}
$$

$$
\boxed{\;\tilde v^{(r)}(\vec p)=\sqrt{E-m}\;\Psi_+(\boldsymbol\sigma\cdot\vec u_p\,\eta^{(r)})+\sqrt{E+m}\;\Psi_-(\eta^{(r)})\;}
$$

At rest these collapse to a single Peirce component,

$$
\tilde w^{(r)}(0)=\sqrt{2m}\,\Psi_+(\xi^{(r)}),\qquad
\tilde v^{(r)}(0)=\sqrt{2m}\,\Psi_-(\eta^{(r)}),
$$

which is the biquaternion statement that the large component of the rest spinor is the first Peirce component. Both formulas are the parent's, with the four-component column replaced by the pair of Peirce coordinates.

**Explicit components.** With $\vec u_p=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$ and the helicity spinors

$$
\chi_+=\begin{pmatrix}\cos(\theta/2)\\ e^{i\phi}\sin(\theta/2)\end{pmatrix},\qquad
\chi_-=\begin{pmatrix}-e^{-i\phi}\sin(\theta/2)\\ \cos(\theta/2)\end{pmatrix},
$$

the chiral solutions have the coordinate pairs

$$
(\psi_+,\psi_-)=\bigl(\sqrt{E\mp|\vec p|}\,\chi_\pm,\ \sqrt{E\pm|\vec p|}\,\chi_\pm\bigr),
$$

and the Dirac solutions have

$$
(\psi_+,\psi_-)=\bigl(\sqrt{E+m}\,\xi^{(r)},\ \sqrt{E-m}\,(\boldsymbol\sigma\cdot\vec u_p)\,\xi^{(r)}\bigr).
$$

These are the four-component spinors of the parent, read as coordinates in the two Peirce components rather than as entries of a column.

## Problem 2: Covariant normalisation and orthogonality

**Statement.** Verify $\bar w^{(r)}w^{(s)}=2m\delta^{rs}$, $\bar v^{(r)}v^{(s)}=-2m\delta^{rs}$, $\bar w^{(r)}v^{(s)}=0$, and the Hermitian products.

**Solution.** Write $\bar w w=\langle\tilde w,\tilde w\rangle_{\mathrm D}$ for the Dirac bilinear. The Dirac adjoint is the Hermitian pairing twisted by the representative of $\gamma^0$. In the chiral basis,

$$
\langle\tilde\Psi,\tilde\Phi\rangle_{\mathrm D}=\mathrm{Tr}\bigl(\tilde\Psi^{*}\tilde\Phi\,i\vec e_x\bigr)
=\psi_+^\dagger\phi_-+\psi_-^\dagger\phi_+ ,
$$

and in the Dirac basis the twist is $i\vec e_z$, the representative of $\gamma^0$ there. The single algebraic input is the unit-vector identity

$$
(i\vec u_p)^2=e_t,
$$

which is the biquaternion form of $(\boldsymbol\sigma\cdot\vec u_p)^2=I_2$.

For the chiral solutions, $\psi_+=\sqrt{E\mp|\vec p|}\,\chi_\pm$ and $\psi_-=\sqrt{E\pm|\vec p|}\,\chi_\pm$. The Hermitian product is diagonal,

$$
\mathrm{Tr}\bigl(\tilde w_\pm^{*}\tilde w_\pm\bigr)=\psi_+^\dagger\psi_++\psi_-^\dagger\psi_-=(E\mp|\vec p|)+(E\pm|\vec p|)=2E,
$$

and the Dirac pairing is

$$
\langle\tilde w_\pm,\tilde w_\pm\rangle_{\mathrm D}
=\psi_+^\dagger\psi_-+\psi_-^\dagger\psi_+
=\sqrt{E^2-\vec p^2}\,\chi_\pm^\dagger\chi_\pm+\sqrt{E^2-\vec p^2}\,\chi_\pm^\dagger\chi_\pm=2m .
$$

Opposite helicities are orthogonal, $\langle\tilde w_+,\tilde w_-\rangle_{\mathrm D}=0$. For the negative-frequency branch the first coordinate carries the minus sign, and the same computation gives $-2m$. The mixed term cancels because the two products are opposite:

$$
\langle\tilde w_\pm,\tilde v_\pm\rangle_{\mathrm D}
=\sqrt{E^2-\vec p^2}\,\chi_\pm^\dagger\chi_\pm-\sqrt{E^2-\vec p^2}\,\chi_\pm^\dagger\chi_\pm=0 .
$$

In the Dirac basis the same three statements hold with the twist $i\vec e_z$, and the spin labels $r,s$ replace the helicity labels. The Hermitian products are

$$
\mathrm{Tr}\bigl(\tilde w^{*}\tilde w\bigr)=2E,\qquad \mathrm{Tr}\bigl(\tilde v^{*}\tilde v\bigr)=2E,
$$

and the mixed Hermitian product vanishes at opposite momenta,

$$
\mathrm{Tr}\bigl(\tilde w^{(r)*}(\vec p)\,\tilde v^{(s)}(-\vec p)\bigr)=0,
$$

which is the parent's relation with the spin labels $r,s$.

The bilinear $\bar ww=\langle\tilde w,\tilde w\rangle_{\mathrm D}$ is a Lorentz scalar and its value $2m$ is the covariant normalisation; it is not the probability density, which is the positive quantity $\mathrm{Tr}(\tilde w^*\tilde w)=2E$. As a numerical check, for $m=1$ and $|\vec p|=0.6$, hence $E=1.166190$, direct evaluation gives $\bar ww=2.0000$, $\bar vv=-2.0000$, $\bar wv=0$, and $\mathrm{Tr}(\tilde w^*\tilde w)=\mathrm{Tr}(\tilde v^*\tilde v)=2.3324=2E$.

## Problem 3: The spin sums

**Statement.** Verify the completeness relations

$$
\sum_{\pm}\tilde w_\pm\,\langle\tilde w_\pm,\cdot\rangle_{\mathrm D}=\not p+m,\qquad
\sum_{\pm}\tilde v_\pm\,\langle\tilde v_\pm,\cdot\rangle_{\mathrm D}=\not p-m .
$$

**Solution.** The left-hand side is an operator on $\mathbb{B}$, not a matrix: for every $\tilde\Phi$,

$$
\sum_{\pm}\tilde w_\pm\,\langle\tilde w_\pm,\tilde\Phi\rangle_{\mathrm D}
=\sum_{\pm}\tilde w_\pm\bigl(\psi_{\pm,+}^\dagger\phi_-+\psi_{\pm,-}^\dagger\phi_+\bigr).
$$

On the chiral solutions, $\psi_{\pm,+}=\sqrt{E\mp|\vec p|}\,\chi_\pm$ and $\psi_{\pm,-}=\sqrt{E\pm|\vec p|}\,\chi_\pm$. The two-spinor completeness relations are $\sum_\pm\chi_\pm\chi_\pm^\dagger=I_2$ and $\sum_\pm(\pm1)\chi_\pm\chi_\pm^\dagger=\boldsymbol\sigma\cdot\vec u_p$. Substituting, the four Peirce blocks are

$$
\sum_\pm\psi_{\pm,+}\psi_{\pm,-}^\dagger=mI_2,\qquad
\sum_\pm\psi_{\pm,+}\psi_{\pm,+}^\dagger=EI_2-|\vec p|\,\boldsymbol\sigma\cdot\vec u_p,
$$

and their conjugates. Restoring the algebra, $E I_2-|\vec p|\,\boldsymbol\sigma\cdot\vec u_p$ is $E-p_k\sigma_k$ and $mI_2$ is $m$, so

$$
\sum_{\pm}\tilde w_\pm\,\langle\tilde w_\pm,\cdot\rangle_{\mathrm D}
=E\,R_{i\vec e_x}-p_k\,L_{i\vec e_k}R_{\vec e_y}+m=\not p+m .
$$

The negative-frequency sum is identical in structure with the roles of the two Peirce components interchanged, and gives $\not p-m$.

**The on-shell identity.** The two sums are consistent with the normalisations because the trace of $\not p+m$ over the four-dimensional amplitude space is $4m$, and because

$$
(\not p+m)(\not p-m)=\not p^2-m^2 .
$$

The operator $\not p$ squares to a multiple of the identity:

$$
\not p^2=E^2R_{(i\vec e_x)^2}-p_jp_kL_{i\vec e_j}R_{\vec e_y}L_{i\vec e_k}R_{\vec e_y}
=E^2-p_jp_kL_{-\vec e_j\vec e_k}R_{-e_t}
=E^2-\vec p^2 ,
$$

the cross terms vanishing because $R_{i\vec e_x}$ and $L_{i\vec e_k}R_{\vec e_y}$ anticommute. On the mass shell $\not p^2=m^2$, so the two branches close the amplitude space, exactly as $(\not p+m)(\not p-m)=0$ in the matrix language.

**Check in the Dirac basis.** The same relations hold with the spin index $r$ replacing the helicity index, once the Dirac-basis spinors of Problem 1 are used:

$$
\sum_{r=1}^{2}\tilde w^{(r)}\bigl\langle\tilde w^{(r)},\cdot\bigr\rangle_{\mathrm D}=\not p+m,\qquad
\sum_{r=1}^{2}\tilde v^{(r)}\bigl\langle\tilde v^{(r)},\cdot\bigr\rangle_{\mathrm D}=\not p-m .
$$

The proof uses $\sum_r\xi^{(r)}\xi^{(r)\dagger}=I_2$ in place of the helicity sums. A numerical evaluation at the same kinematics confirms both equalities on a basis of $\mathbb{B}$.

## Problem 4: The massless limit and helicity–chirality locking

**Statement.** Take $m=0$ and exhibit the helicity–chirality locking in the Peirce components.

**Solution.** In the chiral basis the massless equation $\not p\,\tilde\Psi=0$ splits into its two Peirce components,

$$
\bigl(\not p\,\tilde\Psi\bigr)\tilde\Pi_+=0,\qquad \bigl(\not p\,\tilde\Psi\bigr)\tilde\Pi_-=0,
$$

which are the two Weyl equations

$$
(E-\boldsymbol\sigma\cdot\vec p)\,\psi_-=0,\qquad (E+\boldsymbol\sigma\cdot\vec p)\,\psi_+=0 .
$$

For $m=0$ the dispersion is $E=|\vec p|$, and the positive-frequency solutions of Problem 1 become

$$
\tilde w_+(\vec p)=\sqrt{2E}\,\Psi_-(\chi_+),\qquad
\tilde w_-(\vec p)=\sqrt{2E}\,\Psi_+(\chi_-).
$$

The first has only the right-handed Peirce component, the second only the left-handed one. The two labels are locked: **positive helicity goes with right-handedness and negative helicity with left-handedness.** In the algebra this is the statement that $\tilde w_+$ is annihilated by $P_L$ and $\tilde w_-$ by $P_R$:

$$
P_L\tilde w_+=0,\qquad P_R\tilde w_-=0 .
$$

The mass term is the only term that couples the two Peirce components: in the chiral pair, $m\psi_+$ and $m\psi_-$ are the off-diagonal entries, and setting $m=0$ decouples them. At fixed momentum each Weyl equation selects one complex helicity state, and the two together give the two massless states; the Dirac equation is recovered as the pair. Restoring $c$ and $\hbar$ and passing to the time-dependent form gives the parent's Weyl equations $i\hbar\,\partial_{t'}\psi_R=c\,\boldsymbol\sigma\cdot\vec u_p\,\psi_R$ and $i\hbar\,\partial_{t'}\psi_L=-c\,\boldsymbol\sigma\cdot\vec u_p\,\psi_L$, with $p=-i\hbar\nabla$ in the operator equations.

## Problem 5: The algebra of the generators and the change of basis

**Statement.** Verify the Clifford relations in the algebra, identify $\gamma_5$, and determine how the generators change under the change of basis.

**Solution.** The relations were verified in the introduction from the multiplication table. The chirality operator is

$$
\gamma_5=R_{-i\vec e_z},\qquad \gamma_5^2=R_{(-i\vec e_z)^2}=1,
$$

and it anticommutes with every generator: with $\gamma^0=R_{i\vec e_x}$ and $\gamma^k=L_{i\vec e_k}R_{\vec e_y}$,

$$
\gamma_5\gamma^0+\gamma^0\gamma_5=R_{-i\vec e_z i\vec e_x+i\vec e_x(-i\vec e_z)}=0,
\qquad
\gamma_5\gamma^k+\gamma^k\gamma_5=L_{i\vec e_k}\bigl(R_{-i\vec e_z\vec e_y+\vec e_y(-i\vec e_z)}\bigr)=0 .
$$

The projectors are $P_L=R_{\tilde\Pi_+}$ and $P_R=R_{\tilde\Pi_-}$; they satisfy $P_L+P_R=1$, $P_LP_R=0$, and $P_L\gamma_5=-P_L$, $P_R\gamma_5=P_R$. They are the Peirce projectors of the algebra, not matrices.

**The change of basis.** Right multiplication by $\tilde W=(e_t+\vec e_y)/\sqrt2$ is a unit-norm biquaternion, and it sends the chiral basis to the Dirac basis:

$$
\tilde\Psi_d=\tilde\Psi_c\,\tilde W .
$$

The generators transform by conjugation. Since $\tilde W^{-1}i\vec e_x\tilde W=i\vec e_z$ and $\tilde W^{-1}(-i\vec e_z)\tilde W=i\vec e_x$,

$$
\gamma^0_d=R_{i\vec e_z},\qquad \gamma^k_d=\gamma^k=L_{i\vec e_k}R_{\vec e_y},\qquad \gamma_5^d=R_{i\vec e_x}.
$$

The spatial generators are unchanged because $\tilde W^{-1}\vec e_y\tilde W=\vec e_y$; only $\gamma^0$ and $\gamma_5$ change. In the Dirac basis $\gamma^0_d$ is diagonal on the Peirce components, which is why that basis separates the large and the small component in the non-relativistic limit. The $4\times4$ matrix $U$ of the parent is the regular representation of this right multiplication on the four-dimensional space of the two Peirce coordinates.

**The Lorentz generators.** The generators of the spinor representation are $S^{\mu\nu}=\frac i4[\gamma^\mu,\gamma^\nu]$. In the algebra they are again left and right multiplications:

$$
S^{0k}=\frac i4[\gamma^0,\gamma^k]=-\frac i2\,L_{i\vec e_k}R_{i\vec e_z},\qquad
S^{jk}=\frac i4[\gamma^j,\gamma^k]=\frac i2\,L_{\vec e_j\vec e_k}.
$$

Both are block diagonal on the Peirce components, so $[S^{\mu\nu},\gamma_5]=0$. The rotations $S^{jk}$ carry no chirality factor and act with the same sign on the two components; the boosts $S^{0k}$ carry the chirality sign, since $R_{i\vec e_z}=-\gamma_5$ and

$$
S^{0k}=\frac i2\,L_{i\vec e_k}\,\gamma_5 .
$$

This is the algebraic content of the parent's statement that rotations are chirality-even and boosts are chirality-odd. The signs are the ones of the exercise: the commutator $[\gamma^0,\gamma^k]$ is $-2L_{i\vec e_k}R_{i\vec e_z}$ with the present convention.

## Problem 6: The biquaternionic mass-shell condition

**Statement.** Verify the mass-shell condition of the parent and recover the relativistic energy–momentum relation.

**Solution.** The plane-wave ansatz carries the wave biquaternion

$$
\tilde P/\hbar=\frac{i\omega}{c}\,e_t+\vec k,\qquad \vec k=k_1\vec e_x+k_2\vec e_y+k_3\vec e_z ,
$$

an element of the material sector $\mathbb{M}_-$: imaginary scalar part and real vector part. The biquaternion norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$, so

$$
\langle\tilde P/\hbar\rangle_{\natural}=\left(\frac{i\omega}{c}\right)^2+k_1^2+k_2^2+k_3^2=-\frac{\omega^2}{c^2}+\vec k^2 .
$$

The dispersion relation is $\omega^2=c^2\vec k^2+m^2c^4/\hbar^2$. Substituting,

$$
\langle\tilde P/\hbar\rangle_{\natural}=-\frac{1}{c^2}\left(c^2\vec k^2+\frac{m^2c^4}{\hbar^2}\right)+\vec k^2=-\frac{m^2c^2}{\hbar^2},
$$

which is the parent's condition

$$
\boxed{\;\tilde P\tilde P^{\natural}=-m^2c^2\;}.
$$

Equivalently, with $E=\hbar\omega$ and $\vec p=\hbar\vec k$, the norm is quadratic, so $\langle\tilde P/\hbar\rangle_{\natural}=\langle\tilde P\rangle_{\natural}/\hbar^2=-m^2c^2/\hbar^2$. The mass shell is not a new postulate: it is the statement that the four-wavevector is a timelike element of $\mathbb{M}_-$ with the same biquaternion norm as the four-momentum.

The two roots $\omega=\pm\sqrt{c^2\vec k^2+m^2c^4/\hbar^2}$ are the two frequency branches, and they are the two families $\tilde w$ and $\tilde v$ constructed above; the two spin labels within each branch give the four-dimensional complex solution space. As a numerical check, for an electron ($mc^2=0.510998950\ \mathrm{MeV}$) at $|\vec p|=1\ \mathrm{MeV}/c$, the dispersion gives $E=1.122996\ \mathrm{MeV}$ and $E^2-\vec p^2c^2=0.261120\ \mathrm{MeV}^2=(mc^2)^2$; the wave biquaternion has $\langle\tilde P/\hbar\rangle_{\natural}=-6.706054\times10^{24}\ \mathrm{m}^{-2}$, agreeing with $-m^2c^2/\hbar^2$ to the digits shown.

## Summary

The six problems test the parent's plane-wave solutions and confirm them in the algebra.

1. **The spinors.** In the chiral basis, $\tilde w_\pm=\sqrt{E\mp|\vec p|}\,\Psi_+(\chi_\pm)+\sqrt{E\pm|\vec p|}\,\Psi_-(\chi_\pm)$ and $\tilde v_\pm=-\sqrt{E\mp|\vec p|}\,\Psi_+(\chi_\pm)+\sqrt{E\pm|\vec p|}\,\Psi_-(\chi_\pm)$; in the Dirac basis, $\tilde w^{(r)}=\sqrt{E+m}\,\Psi_+(\xi^{(r)})+\sqrt{E-m}\,\Psi_-(\boldsymbol\sigma\cdot\vec u_p\,\xi^{(r)})$ and $\tilde v^{(r)}=\sqrt{E-m}\,\Psi_+(\boldsymbol\sigma\cdot\vec u_p\,\eta^{(r)})+\sqrt{E+m}\,\Psi_-(\eta^{(r)})$. At rest the positive-frequency amplitude has equal Peirce coordinates and the negative-frequency amplitude opposite ones; in the Dirac basis each sits in a single Peirce component.
2. **Normalisation.** The covariant values $2m$, $-2m$ and $0$ follow from the single identity $(i\vec u_p)^2=e_t$; the Hermitian products are $2E$.
3. **Spin sums.** The completeness relations $\sum\tilde w\,\langle\tilde w,\cdot\rangle_{\mathrm D}=\not p+m$ and $\sum\tilde v\,\langle\tilde v,\cdot\rangle_{\mathrm D}=\not p-m$ hold as operator identities on $\mathbb{B}$, and $(\not p+m)(\not p-m)=0$ on shell.
4. **Massless limit.** Each helicity eigenstate becomes a single Peirce component, with positive helicity right-handed and negative helicity left-handed; the mass term is the only coupling of the two components.
5. **Generators.** The Clifford algebra is the multiplication table: $\gamma^0=R_{i\vec e_x}$, $\gamma^k=L_{i\vec e_k}R_{\vec e_y}$, $\gamma_5=R_{-i\vec e_z}$; the change of basis is right multiplication by $\tilde W=(e_t+\vec e_y)/\sqrt2$, which sends $\gamma^0$ to $R_{i\vec e_z}$ and leaves $\gamma^k$ unchanged; the Lorentz generators are $S^{0k}=-\frac i2L_{i\vec e_k}R_{i\vec e_z}$ and $S^{jk}=\frac i2L_{\vec e_j\vec e_k}$.
6. **Mass shell.** The condition $\tilde P\tilde P^{\natural}=-m^2c^2$ is the biquaternion-norm statement $\langle\tilde P/\hbar\rangle_{\natural}=-m^2c^2/\hbar^2$, and reproduces $E^2=\vec p^2c^2+m^2c^4$.

Two objects are needed by the exercise and are not displayed in the parent: the chiral negative-frequency spinors $\tilde v_\pm$ (Problem 1) and the change-of-basis biquaternion $\tilde W$ (Problem 5). The constructions above reproduce the parent's stated results.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $R_a,L_a$ | Right and left multiplication, $R_a(\tilde Q)=\tilde Q a$, $L_a(\tilde Q)=a\tilde Q$ |
| $\gamma^0=R_{i\vec e_x}$, $\gamma^k=L_{i\vec e_k}R_{\vec e_y}$ | The Dirac generators as algebra operations |
| $\gamma_5=R_{-i\vec e_z}$ | Chirality operator |
| $\tilde\Pi_\pm=\frac12(e_t\pm i\vec e_z)$ | Peirce idempotents; $P_{L,R}=R_{\tilde\Pi_\pm}$ |
| $\vec\Upsilon_x,\vec\Upsilon_y$ | Off-diagonal matrix units |
| $\Psi_\pm(\chi)$ | Spinor realised in $\mathbb B\tilde\Pi_\pm$ |
| $\tilde\Psi=\Psi_+(\psi_+)+\Psi_-(\psi_-)$ | The Dirac field as a biquaternion |
| $\langle\tilde\Psi,\tilde\Phi\rangle_{\mathrm D}=\mathrm{Tr}(\tilde\Psi^*\tilde\Phi\,i\vec e_x)$ | Dirac pairing in the chiral basis |
| $\not p=E R_{i\vec e_x}-p_kL_{i\vec e_k}R_{\vec e_y}$ | Momentum-space Dirac operator |
| $\tilde W=(e_t+\vec e_y)/\sqrt2$ | Change of basis, chiral $\to$ Dirac |
| $S^{0k}=-\frac i2L_{i\vec e_k}R_{i\vec e_z}$, $S^{jk}=\frac i2L_{\vec e_j\vec e_k}$ | Lorentz generators |
| $\tilde P/\hbar=i\omega/c\,e_t+\vec k$ | Wave biquaternion |
| $\tilde P\tilde P^{\natural}=-m^2c^2$ | Mass-shell condition |

## Further Reading

- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the plane-wave spinors, the normalisations, and the spin sums in the standard notation.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the spin sums, the chiral and Dirac representations, and the Lorentz generators.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the two representations, the spinor normalisation, and the completeness relations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford algebra and the spinor representations.
- The parent article of this exercise: [The Biquaternion Dirac Equation — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), and its companions [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) and [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html).
