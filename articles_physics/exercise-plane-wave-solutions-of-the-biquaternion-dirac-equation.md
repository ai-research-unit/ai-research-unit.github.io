# __Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation__

## Introduction

This is one of the worked exercises on the biquaternion Dirac equation. It exists to test its parent article, *The Biquaternion Dirac Equation — Solutions and Non-Relativistic Limit*, which supplies the field, the two natural spinor bases, the plane-wave solution structure, the covariant normalisations, the spin sums, and the biquaternionic mass-shell condition.

We assume the parent article throughout and do not re-derive the equation. We take over from it: the spinor-module form of the equation, $(i\gamma^\mu\partial_\mu-m)\psi=0$; the two bases, **chiral** and **Dirac**; the plane-wave branches $\psi=w(\vec p)\exp(-i(Et'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)))$ and $\psi=v(\vec p)\exp(+i(Et'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)))$ with $E=+\sqrt{\vec p^2+m^2}$; the momentum-space equations $(\not p-m)w=0$ and $(\not p+m)v=0$; the wave biquaternion and the mass-shell condition. The value of an exercise of this kind lies in the worked solutions, so each problem is carried to a definite answer.

The six problems are: **(1)** write out $w^{(r)}(\vec p)$ and $v^{(r)}(\vec p)$ explicitly at rest and at general momentum; **(2)** verify the covariant normalisations $\bar w w=2m$, $\bar v v=-2m$ and the orthogonality $\bar w v=0$; **(3)** verify the spin sums; **(4)** take the massless limit and exhibit the helicity–chirality locking; **(5)** verify the gamma-matrix algebra in the two representations and determine how the Lorentz generators change basis; **(6)** verify the biquaternionic mass-shell condition.

$$
g=\mathrm{diag}(+1,-1,-1,-1),\qquad \{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4,
$$

so that with the four-momentum $p^\mu=(E,\vec p)$ and $p_\mu=(E,-\vec p)$, the slash is $\not p=\gamma^\mu p_\mu=\gamma^0E-\boldsymbol\gamma\cdot\vec p$. This $g$ is **not** the spacetime metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$ carried by the $ict'$ gradient; the two are negatives, $g=-\eta$, and they yield the same $\Box$. The Dirac adjoint is $\bar\psi=\psi^\dagger\gamma^0$. In the solution sections we use natural units $\hbar=c=1$, restoring $\hbar$ and $c$ in Problem 6. The two-spinors are $\xi^{(1)}=(1,0)^T$, $\xi^{(2)}=(0,1)^T$, with $\xi^{(r){}^{*}}\xi^{(s)}=\delta^{rs}$ and the same for $\eta^{(r)}$, and $\chi_\pm$ are the helicity eigenspinors $\boldsymbol\sigma\cdot\vec u_p\,\chi_\pm=\pm\chi_\pm$.

## Problem 1: The spinors at rest and at general momentum

**Statement.** Starting from $(\not p-m)w=0$ and $(\not p+m)v=0$, write out $w^{(r)}(\vec p)$ and $v^{(r)}(\vec p)$ explicitly at rest and at general momentum.

**Solution.** In the Dirac basis, $\gamma^0=\mathrm{diag}(I_2,-I_2)$ and $\gamma^k=\begin{pmatrix}0&\sigma_k\\-\sigma_k&0\end{pmatrix}$, so

$$
\not p-m=\begin{pmatrix}(E-m)I_2 & -\boldsymbol\sigma\cdot\vec p\\[2pt] \boldsymbol\sigma\cdot\vec p & -(E+m)I_2\end{pmatrix}.
$$

Writing $w=(w_A,w_B)$, the equation $(\not p-m)w=0$ becomes the pair

$$
(E-m)w_A=\boldsymbol\sigma\cdot\vec p\,w_B,\qquad (E+m)w_B=\boldsymbol\sigma\cdot\vec p\,w_A .
$$

The second equation gives $w_B=\dfrac{\boldsymbol\sigma\cdot\vec p}{E+m}w_A$, and the first is then satisfied automatically on the mass shell $E^2=\vec p^2+m^2$; the upper two-spinor $w_A$ is free. Choosing $w_A=\sqrt{E+m}\,\xi^{(r)}$ and using $\dfrac{\boldsymbol\sigma\cdot\vec p}{E+m}=\dfrac{\boldsymbol\sigma\cdot\vec p}{\sqrt{E+m}\sqrt{E+m}}$ together with $\sqrt{E^2-m^2}=|\vec p|$ gives the parent's positive-frequency spinors,

$$
\boxed{\;w^{(r)}(\vec p)=\begin{pmatrix}\sqrt{E+m}\,\xi^{(r)}\\[2pt] \sqrt{E-m}\,(\boldsymbol\sigma\cdot\vec u_p)\,\xi^{(r)}\end{pmatrix},\qquad \vec u_p=\frac{\vec p}{|\vec p|} }.
$$

For the negative-frequency branch, $(\not p+m)v=0$ reads, in the same basis,

$$
(E+m)v_A=\boldsymbol\sigma\cdot\vec p\,v_B,\qquad (E-m)v_B=\boldsymbol\sigma\cdot\vec p\,v_A,
$$

so $v_A=\dfrac{\boldsymbol\sigma\cdot\vec p}{E+m}v_B$, and with $v_B=\sqrt{E+m}\,\eta^{(r)}$,

$$
\boxed{\;v^{(r)}(\vec p)=\begin{pmatrix}\sqrt{E-m}\,(\boldsymbol\sigma\cdot\vec u_p)\,\eta^{(r)}\\[2pt] \sqrt{E+m}\,\eta^{(r)}\end{pmatrix} }.
$$

**At rest.** Setting $\vec p=0$, $E=m$, the general formulas collapse to

$$
w^{(r)}(0)=\sqrt{2m}\begin{pmatrix}\xi^{(r)}\\0\end{pmatrix},\qquad v^{(r)}(0)=\sqrt{2m}\begin{pmatrix}0\\\eta^{(r)}\end{pmatrix},
$$

that is,

$$
w^{(1)}(0)=\sqrt{2m}\begin{pmatrix}1\\0\\0\\0\end{pmatrix},\quad w^{(2)}(0)=\sqrt{2m}\begin{pmatrix}0\\1\\0\\0\end{pmatrix},\quad v^{(1)}(0)=\sqrt{2m}\begin{pmatrix}0\\0\\1\\0\end{pmatrix},\quad v^{(2)}(0)=\sqrt{2m}\begin{pmatrix}0\\0\\0\\1\end{pmatrix}.
$$

At rest the positive-frequency spinors live entirely in the upper pair of components and the negative-frequency spinors entirely in the lower pair.

**At general momentum.** Writing $\vec u_p=(\sin\theta\cos\phi,\ \sin\theta\sin\phi,\ \cos\theta)$,

$$
\boldsymbol\sigma\cdot\vec u_p=\begin{pmatrix}\cos\theta & \exp(-i\phi)\sin\theta\\[2pt] \exp(i\phi)\sin\theta & -\cos\theta\end{pmatrix}.
$$

Substituting into the boxed formulas gives the explicit components

$$
w^{(1)}=\begin{pmatrix}\sqrt{E+m}\\0\\ \sqrt{E-m}\cos\theta\\ \sqrt{E-m}\,\exp(i\phi)\sin\theta\end{pmatrix},\qquad
w^{(2)}=\begin{pmatrix}0\\ \sqrt{E+m}\\ \sqrt{E-m}\,\exp(-i\phi)\sin\theta\\ -\sqrt{E-m}\cos\theta\end{pmatrix},
$$

$$
v^{(1)}=\begin{pmatrix}\sqrt{E-m}\cos\theta\\ \sqrt{E-m}\,\exp(i\phi)\sin\theta\\ \sqrt{E+m}\\0\end{pmatrix},\qquad
v^{(2)}=\begin{pmatrix}\sqrt{E-m}\,\exp(-i\phi)\sin\theta\\ -\sqrt{E-m}\cos\theta\\0\\ \sqrt{E+m}\end{pmatrix}.
$$

At $\vec p=0$ these reduce to the rest forms, and they solve the momentum-space equations identically for all $\vec p$. The two free two-spinors give the two spin states of the particle (for $w$) and of the antiparticle (for $v$), so the positive- and negative-frequency solution spaces are each two-dimensional over $\mathbb C$, and together they span the four-dimensional amplitude space.

## Problem 2: Covariant normalisation and orthogonality

**Statement.** Verify $\bar w^{(r)}w^{(s)}=2m\,\delta^{rs}$, $\bar v^{(r)}v^{(s)}=-2m\,\delta^{rs}$, and $\bar w^{(r)}v^{(s)}=0$, together with the Hermitian products.

**Solution.** The Dirac adjoint in the Dirac basis is $\bar w=w^\dagger\gamma^0=(w_A^\dagger,-w_B^\dagger)$, so $\bar w\,w=w_A^\dagger w_A-w_B^\dagger w_B$. The single algebraic input is the identity for unit $\vec u_p$,

$$
(\boldsymbol\sigma\cdot\vec u_p)^2=|\vec u_p|^2I_2=I_2.
$$

Then

$$
\bar w^{(r)}w^{(s)}
=(E+m)\,\xi^{(r){}^{*}}\xi^{(s)}-(E-m)\,\xi^{(r){}^{*}}(\boldsymbol\sigma\cdot\vec u_p)^2\xi^{(s)}
=(E+m)\delta^{rs}-(E-m)\delta^{rs}=2m\,\delta^{rs}.
$$

For the negative-frequency branch the order of the two terms is reversed,

$$
\bar v^{(r)}v^{(s)}
=(E-m)\,\eta^{(r){}^{*}}(\boldsymbol\sigma\cdot\vec u_p)^2\eta^{(s)}-(E+m)\,\eta^{(r){}^{*}}\eta^{(s)}
=(E-m)\delta^{rs}-(E+m)\delta^{rs}=-2m\,\delta^{rs}.
$$

This relative minus sign is the standard signature of the negative-frequency branch. For the cross term,

$$
\bar w^{(r)}v^{(s)}
=\sqrt{E^2-m^2}\,\xi^{(r){}^{*}}(\boldsymbol\sigma\cdot\vec u_p)\eta^{(s)}
-\sqrt{E^2-m^2}\,\xi^{(r){}^{*}}(\boldsymbol\sigma\cdot\vec u_p)\eta^{(s)}=0,
$$

since $\boldsymbol\sigma\cdot\vec u_p$ is Hermitian and the two terms cancel exactly. The Hermitian products follow from the same formulas without the $\gamma^0$:

$$
w^{(r){}^{*}}w^{(s)}=(E+m)\delta^{rs}+(E-m)\delta^{rs}=2E\,\delta^{rs},
$$

$$
v^{(r){}^{*}}v^{(s)}=(E-m)\delta^{rs}+(E+m)\delta^{rs}=2E\,\delta^{rs}.
$$

Finally, the mixed Hermitian product of the parent article requires opposite momenta and likewise vanishes:

$$
w^{(r){}^{*}}(\vec p)\,v^{(s)}(-\vec p)
=\sqrt{E^2-m^2}\,\xi^{(r){}^{*}}(\boldsymbol\sigma\cdot\vec u_p)\eta^{(s)}
-\sqrt{E^2-m^2}\,\xi^{(r){}^{*}}(\boldsymbol\sigma\cdot\vec u_p)\eta^{(s)}=0 .
$$

The bilinear $\bar w w$ is a Lorentz scalar, and its value $2m$ is the covariant normalisation; $\bar w w$ is not the probability density, which is the positive quantity $w^\dagger w=2E$. As a numerical check, for $m=1$, $|\vec p|=0.6$ (hence $E=1.16619$), direct evaluation gives $\bar w w=2.0000$, $\bar v v=-2.0000$, $\bar w v=0$, and $w^\dagger w=v^\dagger v=2.3324=2E$, all to machine precision.

## Problem 3: The spin sums

**Statement.** Verify the completeness relations (spin sums) $\sum_{r=1}^{2}w^{(r)}\bar w^{(r)}=\not p+m$ and $\sum_{r=1}^{2}v^{(r)}\bar v^{(r)}=\not p-m$.

**Solution.** The spin sum is the outer product $w\bar w$, which is a $4\times4$ matrix. Using $\bar w=(w_A^\dagger,-w_B^\dagger)$ and the two-spinor completeness $\sum_r\xi^{(r)}\xi^{(r){}^{*}}=I_2$,

$$
w^{(r)}\bar w^{(r)}
=\begin{pmatrix}w_Au_A^\dagger & -w_Au_B^\dagger\\[2pt] w_Bu_A^\dagger & -w_Bu_B^\dagger\end{pmatrix}
\;\xrightarrow[\text{sum over }r]{}\;
\begin{pmatrix}(E+m)I_2 & -(\boldsymbol\sigma\cdot\vec p)\\[2pt] \boldsymbol\sigma\cdot\vec p & -(E-m)I_2\end{pmatrix},
$$

where in the off-diagonal blocks we used $\sum_r\xi^{(r)}\xi^{(r){}^{*}}(\boldsymbol\sigma\cdot\vec u_p)=\boldsymbol\sigma\cdot\vec u_p$ and its Hermitian conjugate. In the Dirac basis,

$$
\not p+m=\gamma^0E-\boldsymbol\gamma\cdot\vec p+m
=\begin{pmatrix}(E+m)I_2 & -\boldsymbol\sigma\cdot\vec p\\[2pt] \boldsymbol\sigma\cdot\vec p & -(E-m)I_2\end{pmatrix},
$$

since $-\boldsymbol\gamma\cdot\vec p=\begin{pmatrix}0&-\boldsymbol\sigma\cdot\vec p\\ \boldsymbol\sigma\cdot\vec p&0\end{pmatrix}$ and $-E+m=-(E-m)$. This is exactly the matrix obtained above, so

$$
\sum_{r=1}^{2}w^{(r)}(\vec p)\,\bar w^{(r)}(\vec p)=\not p+m .
$$

The negative-frequency sum is identical in structure with the roles of the two blocks interchanged. Carrying it out with $\sum_r\eta^{(r)}\eta^{(r){}^{*}}=I_2$,

$$
\sum_{r=1}^{2}v^{(r)}(\vec p)\,\bar v^{(r)}(\vec p)
=\begin{pmatrix}-(E-m)I_2 & -\boldsymbol\sigma\cdot\vec p\\[2pt] \boldsymbol\sigma\cdot\vec p & -(E+m)I_2\end{pmatrix}
=\not p-m .
$$

The two spin sums are consistent with the normalisations of Problem 2, since taking the trace of $\sum w\bar w$ over the particle space returns $4m$, the trace of $\not p+m$, and the projectors annihilate one another on shell:

$$
(\not p+m)(\not p-m)=\not p^2-m^2=(p_\mu p_\nu\gamma^\mu\gamma^\nu)-m^2=(p^2-m^2)I_4=0,
$$

using $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$ and $p^2=E^2-\vec p^2=m^2$. This is the algebraic statement that the two branches close the amplitude space.

**Check in the chiral basis.** The same relations hold in the chiral basis with the helicity index $\pm$ replacing $r$, once the negative-frequency chiral spinors of Problem 4 are used: $\sum_\pm w_\pm\bar w_\pm=\not p+m$ and $\sum_\pm v_\pm\bar v_\pm=\not p-m$, where the sums use $\sum_\pm\chi_\pm\chi_\pm^\dagger=I_2$ and $\sum_\pm(\pm1)\chi_\pm\chi_\pm^\dagger=\boldsymbol\sigma\cdot\vec u_p$. A numerical evaluation at the same kinematics confirms both equalities to machine precision.

## Problem 4: The massless limit and helicity–chirality locking

**Statement.** In the chiral basis, exhibit the massless limit and show how helicity locks to chirality.

**Solution.** In the chiral basis, $\gamma^0=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix}$, $\gamma^k=\begin{pmatrix}0&\sigma_k\\-\sigma_k&0\end{pmatrix}$, so

$$
\not p=\begin{pmatrix}0 & E-\boldsymbol\sigma\cdot\vec p\\[2pt] E+\boldsymbol\sigma\cdot\vec p & 0\end{pmatrix},\qquad
\not p-m=\begin{pmatrix}-m & E-\boldsymbol\sigma\cdot\vec p\\[2pt] E+\boldsymbol\sigma\cdot\vec p & -m\end{pmatrix}.
$$

The parent article gives the positive-frequency chiral spinors, indexed by helicity,

$$
w_\pm(\vec p)=\begin{pmatrix}\sqrt{E\mp|\vec p|}\;\chi_\pm\\[2pt] \sqrt{E\pm|\vec p|}\;\chi_\pm\end{pmatrix},
$$

with the upper block left-handed and the lower block right-handed. Verifying the equation is immediate: the upper component of $(\not p-m)w_\pm$ is $-m\sqrt{E\mp|\vec p|}+(E\mp|\vec p|)\sqrt{E\pm|\vec p|}$, which vanishes because $(E\mp|\vec p|)\sqrt{E\pm|\vec p|}=m\sqrt{E\mp|\vec p|}$; the lower component vanishes identically by the same identity.

The parent article displays the chiral positive-frequency spinors but does not write the chiral negative-frequency spinors; we construct them here, since the massless limit needs them. With the ansatz $v_\pm=(a\chi_\pm,b\chi_\pm)$, the equation $(\not p+m)v_\pm=0$ requires $ma=-(E\mp|\vec p|)b$ and $mb=-(E\pm|\vec p|)a$. The choice $b=\sqrt{E\pm|\vec p|}$ gives $a=-\sqrt{E\mp|\vec p|}$, so

$$
v_\pm(\vec p)=\begin{pmatrix}-\sqrt{E\mp|\vec p|}\,\chi_\pm\\[2pt] \sqrt{E\pm|\vec p|}\,\chi_\pm\end{pmatrix}.
$$

The relative minus sign is fixed by the normalisation $\bar v_\pm v_\pm=-2m$; with it, the chiral spinors reproduce all the results of Problems 2 and 3.

**Massless limit.** Set $m=0$, so that $E=|\vec p|$. Then

$$
w_+(\vec p)\longrightarrow\sqrt{2E}\begin{pmatrix}0\\\chi_+\end{pmatrix},\qquad
w_-(\vec p)\longrightarrow\sqrt{2E}\begin{pmatrix}\chi_-\\0\end{pmatrix},
$$

and likewise for $v_\pm$. Each solution becomes a single Weyl spinor of definite chirality, and the two labels are locked: **positive helicity goes with right-handedness and negative helicity with left-handedness**. This is the precise sense of the parent's statement that a massless fermion of definite helicity has definite chirality. The locking is what the mass term destroys: in the chiral basis the mass term is the off-diagonal entry $-m$ in $\not p-m$, and it is the only term in the equation that couples the two chiralities.

**The Weyl equations.** On shell, $\not p\,\psi=0$ splits into the two equations $(E-\boldsymbol\sigma\cdot\vec p)\psi_R=0$ and $(E+\boldsymbol\sigma\cdot\vec p)\psi_L=0$. With $E=|\vec p|$ these read

$$
\boldsymbol\sigma\cdot\vec u_p\,\psi_R=+\psi_R,\qquad \boldsymbol\sigma\cdot\vec u_p\,\psi_L=-\psi_L,
$$

which is the helicity–chirality locking again. Restoring $c$ and $\hbar$ and passing to the time-dependent form gives the parent's Weyl equations $i\hbar\,\partial/\partial t'\psi_R=c\,\boldsymbol\sigma\cdot\vec u_p\,\psi_R$ and $i\hbar\,\partial/\partial t'\psi_L=-c\,\boldsymbol\sigma\cdot\vec u_p\,\psi_L$, where $p$ is the momentum operator (the parent writes the unit direction $\vec u_p$ in the plane-wave formulas; in the operator equations the momentum is $p=-i\hbar\nabla$). Each Weyl equation has a two-dimensional solution space, and the Dirac equation is recovered as the pair.

## Problem 5: The gamma-matrix algebra and the change of basis

**Statement.** Verify the Clifford algebra in the chiral and Dirac representations, identify $\gamma_5$, and determine how the Lorentz generators change basis.

**Solution.** In both representations the gamma matrices have the block forms

$$
\text{chiral:}\quad \gamma^0_c=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix},\quad \gamma^k_c=\begin{pmatrix}0&\sigma_k\\-\sigma_k&0\end{pmatrix};
$$

$$
\text{Dirac:}\quad \gamma^0_d=\begin{pmatrix}I_2&0\\0&-I_2\end{pmatrix},\quad \gamma^k_d=\begin{pmatrix}0&\sigma_k\\-\sigma_k&0\end{pmatrix}.
$$

The spatial generators are the **same** in the two representations; only $\gamma^0$ differs. Direct multiplication gives $(\gamma^0)^2=I_4$, $(\gamma^k)^2=-I_4$, $\gamma^0\gamma^k=-\gamma^k\gamma^0$, and $\gamma^j\gamma^k=-\gamma^k\gamma^j$ for $j\neq k$ (the last because $\sigma_j\sigma_k=-\sigma_k\sigma_j$ off diagonal). Hence $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4$ with $g=\mathrm{diag}(+1,-1,-1,-1)$ in both bases, as the parent states. The chirality operator is

$$
\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3:
\qquad \gamma_5^c=\begin{pmatrix}-I_2&0\\0&I_2\end{pmatrix},\qquad
\gamma_5^d=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix}.
$$

In both bases $\gamma_5^2=I_4$ and $\gamma_5$ anticommutes with every generator, $\{\gamma_5,\gamma^\mu\}=0$; the projectors $P_L=\tfrac12(1-\gamma_5)$, $P_R=\tfrac12(1+\gamma_5)$ select the chiralities, and in the chiral basis they are simply the two diagonal blocks.

**Change of basis.** The parent states that the two bases are related by a fixed $*$-unitary transformation but does not exhibit it; we construct it here. Define

$$
U=\frac{1}{\sqrt2}\begin{pmatrix}I_2&I_2\\-I_2&I_2\end{pmatrix},\qquad
U^\dagger=\frac{1}{\sqrt2}\begin{pmatrix}I_2&-I_2\\I_2&I_2\end{pmatrix}.
$$

Then $U^\dagger U=I_4$, so $U$ is $*$-unitary, and a direct computation gives

$$
U\gamma^\mu_c\,U^\dagger=\gamma^\mu_d,\qquad U\gamma_5^c\,U^\dagger=\gamma_5^d .
$$

The two ingredients are that $U$ commutes with each spatial $\gamma^k_c$, so the spatial generators are unchanged, and that $U\gamma^0_cU^\dagger$ produces the diagonal $\gamma^0_d$ and swaps the diagonal $\gamma_5^c$ for the off-diagonal $\gamma_5^d$. Since $\gamma^\mu_d=U\gamma^\mu_cU^\dagger$, the spinor transforms as $\psi_d=U\psi_c$.

**The Lorentz generators.** The generators of the spinor representation are $S^{\mu\nu}=\tfrac{i}{4}[\gamma^\mu,\gamma^\nu]$, related to the parent's tensor bilinear by $\sigma^{\mu\nu}=\tfrac i2[\gamma^\mu,\gamma^\nu]=2S^{\mu\nu}$. In the chiral basis they evaluate to

$$
S^{jk}_c=\tfrac12\epsilon^{jkl}\begin{pmatrix}\sigma_l&0\\0&\sigma_l\end{pmatrix}
=\tfrac12\epsilon^{jkl}\,\sigma_l\otimes I_2,
\qquad
S^{tk}_c=\tfrac i2\begin{pmatrix}-\sigma_k&0\\0&\sigma_k\end{pmatrix}
=\tfrac i2\,\gamma_5^c\,(\sigma_k\otimes I_2).
$$

Both are block diagonal, so both preserve chirality, $[S^{\mu\nu},\gamma_5]=0$; but they differ in their action on the two chiralities. The rotation generators are **even**: they act with the same sign on the left- and right-handed blocks. The boost generators are **odd**: they act with opposite signs, which is the algebraic reason a boost rotates the two chiralities in opposite senses while leaving each in its own chirality. For a general change of basis the generators transform by conjugation, $S^{\mu\nu}_d=U S^{\mu\nu}_c U^\dagger$, and here explicitly

$$
S^{jk}_d=S^{jk}_c,\qquad
S^{tk}_d=\tfrac i2\,\gamma_5^d\,(\sigma_k\otimes I_2)
=\tfrac i2\begin{pmatrix}0&\sigma_k\\\sigma_k&0\end{pmatrix}.
$$

In the Dirac basis the rotation generators are again block diagonal, while the boost generators are block **off-diagonal**; this is the representation in which the non-relativistic reduction separates large and small components (the next exercise). Finally, the structure matches the geometric-algebra dictionary of the companion articles: the chirality-even generators are built from $\sigma_l$ alone and correspond to the real-quaternion rotation generators in $\mathbb H_{\mathbb B}$, whereas the chirality-odd boost generators carry the extra factor $\gamma_5$ and correspond to the Hermitian (boost) generators in $\mathbb M_+$.

## Problem 6: The biquaternionic mass-shell condition

**Statement.** Verify the biquaternionic mass-shell condition of the parent article and recover the relativistic energy–momentum relation.

**Solution.** The parent's plane-wave ansatz carries the wave biquaternion $\tilde P/\hbar$, which the parent identifies with the four-wavevector

$$
\tilde P/\hbar=\frac{i\omega}{c}\,e_t+\vec k,\qquad \vec k=k_1\vec e_x+k_2\vec e_y+k_3\vec e_z .
$$

This is an element of the material sector $\mathbb M_-$: imaginary scalar part, real vector part. Since the biquaternion norm of $\mathbb B$ is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$,

$$
\langle\tilde P/\hbar\rangle_{\natural}=\tilde P\tilde P^{\natural}/\hbar^{2}=\left(\frac{i\omega}{c}\right)^2+k_1^2+k_2^2+k_3^2=-\frac{\omega^2}{c^2}+\vec k^2 .
$$

The relativistic dispersion relation is $\omega^2=c^2\vec k^2+\dfrac{m^2c^4}{\hbar^2}$, so

$$
\langle\tilde P/\hbar\rangle_{\natural}=-\frac{1}{c^2}\left(c^2\vec k^2+\frac{m^2c^4}{\hbar^2}\right)+\vec k^2=-\frac{m^2c^2}{\hbar^2},
$$

which is exactly the parent's condition

$$
\boxed{\;\tilde P\tilde P^{\natural}=-m^2c^2\;}.
$$

Equivalently, with $E=\hbar\omega$ and $\vec p=\hbar\vec k$, the wave biquaternion is $\tilde P/\hbar$; the biquaternion norm being quadratic, $\langle\tilde P/\hbar\rangle_{\natural}=\langle\tilde P\rangle_{\natural}/\hbar^2=-m^2c^2/\hbar^2$, exactly as $\langle\tilde P\rangle_{\natural}=\tilde P\tilde P^{\natural}=-m^2c^2$ in the companion kinematics. The mass-shell condition is therefore not a new postulate: it is the statement that the four-wavevector is a timelike vector of $\mathbb M_-$ with the same biquaternion norm as the four-momentum.

The two roots of the dispersion relation, $\omega=\pm\sqrt{c^2\vec k^2+m^2c^4/\hbar^2}$, are the two frequency branches, and they are precisely the positive- and negative-frequency spinors $w$ and $v$ constructed above; the two spin labels within each branch give the four-dimensional complex solution space that the parent article quotes for the massive equation. As a numerical check, for an electron ($mc^2=0.510998950\ \mathrm{MeV}$) at $|\vec p|=1\ \mathrm{MeV}/c$, the dispersion relation gives $E=1.122996\ \mathrm{MeV}$ and $E^2-\vec p^2c^2=0.261120\ \mathrm{MeV}^2=(mc^2)^2$; the corresponding wave biquaternion has $\langle\tilde P/\hbar\rangle_{\natural}=-6.706054\times10^{24}\ \mathrm{m}^{-2}$, agreeing with $-m^2c^2/\hbar^2$ to one part in $10^{15}$.

## Summary

The six problems test the parent article's plane-wave solutions and confirm them.

1. **The spinors.** In the Dirac basis the solutions are $w^{(r)}=\big(\sqrt{E+m}\,\xi^{(r)},\ \sqrt{E-m}\,(\boldsymbol\sigma\cdot\vec u_p)\xi^{(r)}\big)^T$ and $v^{(r)}=\big(\sqrt{E-m}\,(\boldsymbol\sigma\cdot\vec u_p)\eta^{(r)},\ \sqrt{E+m}\,\eta^{(r)}\big)^T$, with explicit rest and general-momentum forms.
2. **Normalisation.** The covariant normalisations $\bar w^{(r)}w^{(s)}=2m\delta^{rs}$, $\bar v^{(r)}v^{(s)}=-2m\delta^{rs}$, and the orthogonality $\bar w^{(r)}v^{(s)}=0$ all follow from the single identity $(\boldsymbol\sigma\cdot\vec u_p)^2=I_2$; the Hermitian products are $2E\delta^{rs}$.
3. **Spin sums.** The completeness relations $\sum_r w^{(r)}\bar w^{(r)}=\not p+m$ and $\sum_r v^{(r)}\bar v^{(r)}=\not p-m$ follow from the two-spinor completeness relation, and satisfy $(\not p+m)(\not p-m)=0$ on shell.
4. **Massless limit.** In the chiral basis each helicity eigenstate becomes a single Weyl spinor, with positive helicity locking to right-handedness and negative helicity to left-handedness; the mass term is the only term coupling the two chiralities.
5. **Basis change.** The chiral and Dirac representations obey the same Clifford algebra with $g=\mathrm{diag}(+1,-1,-1,-1)$; the $*$-unitary $U=\tfrac{1}{\sqrt2}\left(\begin{smallmatrix}I_2&I_2\\-I_2&I_2\end{smallmatrix}\right)$ interpolates between them, and the Lorentz generators transform by conjugation, rotations acting chirality-even and boosts chirality-odd.
6. **Mass shell.** The biquaternionic condition $\tilde P\tilde P^{\natural}=-m^2c^2$ is the biquaternion-norm statement $\langle\tilde P/\hbar\rangle_{\natural}=-m^2c^2/\hbar^2$, and reproduces $E^2=\vec p^2c^2+m^2c^4$.

Two items needed in this exercise are not displayed in the parent article: the chiral negative-frequency spinors $v_\pm$ (constructed in Problem 4) and the explicit change-of-basis matrix $U$ (constructed in Problem 5). The parent states the existence of both but does not exhibit them; the constructions above are the ones that reproduce its stated results.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\gamma^\mu$, $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$ | Gamma matrices and chirality operator |
| $g=\mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric of the generators; $g=-\eta$ |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | Spacetime metric of the $ict'$ gradient |
| $\not p=\gamma^0E-\boldsymbol\gamma\cdot\vec p$ | Feynman slash of $p^\mu=(E,\vec p)$ |
| $\bar\psi=\psi^\dagger\gamma^0$ | Dirac adjoint |
| $w^{(r)}(\vec p),\,v^{(r)}(\vec p)$ | Positive- and negative-frequency spinors (Dirac basis) |
| $w_\pm(\vec p),\,v_\pm(\vec p)$ | Helicity-indexed spinors (chiral basis) |
| $\xi^{(r)},\eta^{(r)}$; $\chi_\pm$ | Two-spinors; helicity eigenspinors, $\boldsymbol\sigma\cdot\vec u_p\chi_\pm=\pm\chi_\pm$ |
| $U=\tfrac{1}{\sqrt2}\left(\begin{smallmatrix}I_2&I_2\\-I_2&I_2\end{smallmatrix}\right)$ | $*$-Unitary change of basis, $\gamma^\mu_d=U\gamma^\mu_cU^\dagger$ |
| $S^{\mu\nu}=\tfrac i4[\gamma^\mu,\gamma^\nu]$ | Lorentz generators of the spinor representation |
| $\tilde P/\hbar=i\omega/c\,e_t+\vec k$ | Wave biquaternion (four-wavevector) |
| $\tilde P\tilde P^{\natural}=-m^2c^2$ | Biquaternionic mass-shell condition |

## Further Reading

- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the plane-wave spinors, the normalisations, and the spin sums in the standard notation.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the spin sums, the chiral and Dirac representations, and the Lorentz generators.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the two representations, the spinor normalisation, and the completeness relations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford algebra and the spinor representations.
- The parent article of this exercise: *The Biquaternion Dirac Equation — Solutions and Non-Relativistic Limit*, and its companion [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html).
