# __The Feynman Propagator in Biquaternionic Form__

## Introduction

The companion article *Canonical Quantization of the Biquaternion Dirac Field* quantizes the biquaternion Dirac field on its spinor module: it promotes the field to an operator-valued distribution, imposes the equal-time anticommutators, expands the field in the plane-wave solutions, and builds the Fock space. It closes with an explicit accounting of what is standard and what remains open, and it concludes that the construction is a transcription of ordinary canonical quantization rather than a derivation from the algebra $\mathbb{B}$.

Natural units $\hbar=c=1$ are used throughout, so the four-momentum is $\tilde P=iE\,e_t+\vec p$ and the mass shell is $\tilde P\tilde P^\natural=-m^2$.

The dynamics is the one-sided chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,\qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R .
$$

The framework carries two equations called the Dirac equation, and they must not be read as one. The pair displayed above is the first: it is the definition. The gradient acts by left multiplication, the field lies in $\Delta=S\oplus S^{\mathrm{c}}$, and the mass is the off-diagonal pairing of the two chiral halves.

The second is the **two-sided** form of *The Dirac Equation in Biquaternionic Form*, a single equation on $\mathbb{B}$,

$$
\mathcal{N}F=\Big(i\frac{\partial}{\partial t'}+D_3\Big)F-mi\,\overline{F}\,\vec e_z=0,
$$

in which $D_3$ is the spatial Dirac operator of that article, the mass acts by right multiplication through $\vec e_z$, and the conjugation supplies the antilinear part. Because $i\partial/\partial t'+D_3=-\tilde\nabla^{\natural}$, the two-sided operator is

$$
\mathcal{N}=-\tilde\nabla^{\natural}-mi\,\overline{\,\cdot\,}\,\vec e_z .
$$

That display is the whole relation between the two equations, and it says three things. The leading term is the $\natural$-member of the pair, not a new operator. The mass sits on the far side, and it reaches the field only through its conjugate: comparing $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ with $\mathcal{N}F=0$ reads the second field as $\tilde\Psi_R=-i\overline{F}\,\vec e_z$, a conjugation and a fixed direction and nothing else. The price is that $\mathcal{N}$ is not left multiplication by an element of $\mathbb{B}$, which is why the two forms are not the same operator. The dictionary $A$ is a real-linear bijection, so the two forms describe the same field; what changes is the shape of the operator, not the physics. The conjugation in the mass term pairs $F$ with $\overline{F}$, so a solution carries both frequency branches at once; in the time-harmonic case the parent article exhibits exactly that, as a sum of two exponentials of opposite sign.

Everything below is written for the one-sided pair, whose spinor-module representative is the ordinary $(\slashed p-m)\psi=0$. That is the form written on the chiral halves $S$ and $S^{\mathrm{c}}$, which is the decomposition the chirality grading of section *The Legacy Pauli Gamma Formulation* labels.

This article is about the next object in that quantization: the **two-point function** of the quantized field on the spinor-module representative, the Feynman propagator

$$
\boxed{\;S_F(x-y)\;=\;\langle 0|\,T\,\psi^{\mathrm{fop}}(x)\,\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}^{\mathrm{axf}}(y)\,|0\rangle\;},
$$

with $T$ the fermionic time-ordering operator. The two-point function is where the boundary condition of the theory is stored. Its momentum-space amplitude is not a function but a distribution, and what makes it the *Feynman* amplitude rather than the retarded or advanced one is a contour prescription in the complex energy plane — the $i\epsilon$.

The specific question this article asks is a question about the algebra. The biquaternion framework already carries a complex structure: the scalar imaginary $i$ is a fixed central element with $i^2=-1$, it is what turns the material time coordinate into $ict'$, and it is what lets the mass shell be written as the single quadratic condition $\tilde P\tilde P^{\natural}=-m^2$ whose two roots in the energy are the positive- and negative-frequency branches (the particle and antiparticle modes in the standard interpretation). The Feynman prescription is also an insertion of $i$: $m^2\mapsto m^2-i\epsilon$. Are these the same $i$ doing the same work? Is the contour deformation the algebra's own complex structure, or is it an independent analytic input that the algebra can only write down?

We answer this on a concrete case, by computing the pole structure and the contour explicitly and by recomputing every displayed formula on a momentum chosen for the purpose. The finding is stated at the outset because it is the article's content.

**The algebra supplies the complex plane in which the contour is drawn, and a natural notation for the prescription — the deformed mass-shell scalar $\tilde P\tilde P^{\natural}+m^2-i\epsilon$, whose added term $-i\epsilon\,e_t$ is a central element along the $ict'$ axis of the material sector — but it does not select the contour.**

The deformation's *axis* is algebraically natural; its *orientation*, which is what distinguishes the Feynman propagator from the retarded and advanced ones, is an analytic boundary condition. In this problem the algebra adds notation and a home for the $i\epsilon$, not the physics that fixes it. If that is all it adds, we say so.

## The Two-Point Function of the Quantized Dirac Field

The quantized field of the companion article is

$$
\psi^{\mathrm{fop}}(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\vec p}}}
\sum_{r=1}^{2}\Big[a_r^{\mathrm{fop}}(\vec p)\,w^{(r)}(\vec p)\,\exp(-ip\cdot x)
+b_r^{\mathrm{fop}\dagger}(\vec p)\,v^{(r)}(\vec p)\,\exp(+ip\cdot x)\Big],
$$

with $E_{\vec p}=+\sqrt{\vec p^2+m^2}$. Its adjoint is $\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}^{\mathrm{axf}}=\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}^{\mathrm{axf}}$: the Hermitian conjugate, then the timelike cell of the reference frame.

Write $L_a\psi=a\psi$ and $R_b\psi=\psi b$ for the two multiplications of $\mathbb{B}$, and $\nu(t)=x$, $\nu(k)=y$ for the cells of the reference frame. The **momentum cell** is the signed sum of the frame cells contracted with the four-momentum. The sign vector of the frame is $(+,-,-,-)$, so the energy takes the timelike cell with a plus and each momentum component a spatial cell with a minus, and the sum is named rather than left to a repeated index:

$$
\slashed p\;:=\;iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}p_0-\sum_{k=1}^{3}iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_k
\;=\;iR_{\vec e_x}^{\mathrm{axf}}p_0-\sum_{k=1}^{3}iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_k ,
$$

the last step because $L_{e_t}^{\mathrm{axf}}$ is the identity. The two halves act on different sides — the energy from the right through $\vec e_x$, the momentum from the left through $\vec e_k$ together with a right multiplication by $\vec e_y$ — and that asymmetry is the reference frame's, not a slip of notation: it is what makes the cell square to the Lorentz square of the momentum. The four squares do *not* share a sign. The energy cell squares to $+1$, because two minus signs meet: $i^2=-1$ from the central unit and $\vec e_x^2=-\vec e_t$ from the quaternion,

$$
(iR_{\vec e_x}^{\mathrm{axf}}p_0)^2=i^2p_0^2\,R_{\vec e_x^2}^{\mathrm{axf}}=(-1)(-1)\,p_0^2\,\mathbf{1}=+p_0^2\,\mathbf{1},
$$

while each spatial cell squares to $-1$, because the same $i^2$ is now the only sign left, $\vec e_k^2$ and $\vec e_y^2$ cancelling one another,

$$
(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_k)^2=i^2p_k^2\,L_{\vec e_k^2}^{\mathrm{axf}}R_{\vec e_y^2}^{\mathrm{axf}}=(-1)(+1)\,p_k^2\,\mathbf{1}=-p_k^2\,\mathbf{1}.
$$

The cross terms vanish because

$$
\{iR_{\vec e_x}^{\mathrm{axf}},iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\}=-L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y\vec e_x+\vec e_x\vec e_y}^{\mathrm{axf}}=0,
$$

the two factors of $i$ multiplying to $-1$ and the quaternion relation $\vec e_y\vec e_x=-\vec e_x\vec e_y$ killing what is left; two distinct spatial cells cancel the same way on the left, $\{iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},iL_{\vec e_l}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\}=-L_{\vec e_k\vec e_l+\vec e_l\vec e_k}^{\mathrm{axf}}R_{\vec e_y^2}^{\mathrm{axf}}=0$ for $k\ne l$. Hence

$$
(\slashed p)^2=p^2\,\mathbf{1},\qquad p^2=p_0^2-\vec p^2 .
$$

The general statement behind the signs is the frame-cell anticommutator

$$
\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}\}=2\varepsilon_\mu\delta_{\mu\nu}\mathbf{1},
\qquad \varepsilon=(1,-1,-1,-1),\qquad \mathbf{1}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

with $\mathbf{1}$ the identity cell. The body is written in these cells; section *The Legacy Pauli Gamma Formulation* gives their standard names.

The mode operators obey

$$
\{a_r^{\mathrm{fop}}(\vec p),a_s^{\mathrm{fop}\dagger}(\vec k)\}
=\{b_r^{\mathrm{fop}}(\vec p),b_s^{\mathrm{fop}\dagger}(\vec k)\}
=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k),
$$

with all other anticommutators vanishing. The parent article's spinors satisfy

$$
\bar w^{(r)}w^{(s)}=2m\,\delta_{rs},\qquad \bar v^{(r)}v^{(s)}=-2m\,\delta_{rs},
$$

and the two spin sums

$$
\sum_{r=1}^2 w^{(r)}\bar w^{(r)}=\slashed p+m,\qquad
\sum_{r=1}^2 v^{(r)}\bar v^{(r)}=\slashed p-m ,
$$

the momentum cell being on the mass shell, $p_0=E_{\vec p}$.

Contracting the mode operators against the vacuum gives the two elementary two-point functions. The **positive-frequency** piece is

$$
W_+(x-y)\;=\;\langle 0|\,\psi^{\mathrm{fop}}(x)\,\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}^{\mathrm{axf}}(y)\,|0\rangle
=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\vec p}}\,\big(\slashed p+m\big)\,\exp(-ip\cdot(x-y)),
$$

in which only the $a^{\mathrm{fop}} a^{\mathrm{fop}\dagger}$ contraction survives, and the **negative-frequency** piece is

$$
W_-(x-y)\;=\;\langle 0|\,\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}^{\mathrm{axf}}(y)\,\psi^{\mathrm{fop}}(x)\,|0\rangle
=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\vec p}}\,\big(\slashed p-m\big)\,\exp(+ip\cdot(x-y)),
$$

in which only $b^{\mathrm{fop}} b^{\mathrm{fop}\dagger}$ survives. In both expressions the momentum cell is on shell, because the free mode expansion contains the on-shell modes and nothing else. These two objects are not yet the propagator; each is a boundary value of an analytic function, and it is the time ordering that combines them into $S_F$.

Time ordering for a fermion field carries the anticommutation sign:

$$
S_F(x-y)=\theta(x_0-y_0)\,W_+(x-y)-\theta(y_0-x_0)\,W_-(x-y).
$$

The relative minus is not a convention; it is the statement that the two field operators anticommute. Every sign in what follows traces back to it, and it is the quantity a recomputation must reproduce.

## The Pole Structure and the Contour

The two $\theta$ functions can be represented by a single four-dimensional integral. The standard result, and the object whose biquaternion form is the subject of this article, is

$$
\boxed{\;S_F(x-y)\;=\;i\int\!\frac{d^4p}{(2\pi)^4}\;
\exp(-ip\cdot(x-y))\;\frac{\slashed p+m}{p^2-m^2+i\epsilon},
\qquad \epsilon\to0^+\;}.
$$

The overall $i$ and the $i\epsilon$ are fixed by requiring that the $p_0$ integral reproduce the two branches, with the normalization of the time-ordered product and the fermionic relative sign. It is worth performing that check explicitly, because it is where a sign can silently go wrong.

Write the $p_0$ integral at fixed $\vec p$, and put $\Delta t=x_0-y_0$ and $\Delta\vec x=\vec x-\vec y$. Since

$$
p^2-m^2=p_0^2-\vec p^2-m^2=p_0^2-E_{\vec p}^2,
$$

the integrand has poles where

$$
\boxed{\;p_0^2-E_{\vec p}^2+i\epsilon=0,
\qquad\text{i.e.}\qquad
p_0=\pm\sqrt{E_{\vec p}^2-i\epsilon}
=\pm\Big(E_{\vec p}-\frac{i\epsilon}{2E_{\vec p}}\Big)+O(\epsilon^2)\;}.
$$

The sign is worth fixing once explicitly. Let $p_0=E_{\vec p}+\delta$. Then the denominator is $2E_{\vec p}\delta+i\epsilon$, and it vanishes at $\delta=-i\epsilon/(2E_{\vec p})$, which is **below** the axis. At $p_0=-E_{\vec p}+\delta$ the denominator is $-2E_{\vec p}\delta+i\epsilon$, and it vanishes at $\delta=+i\epsilon/(2E_{\vec p})$, which is **above** it.

This is the whole content of the prescription: the two poles are displaced in *opposite* directions. The decay of $\exp(-ip_0\Delta t)$ then selects one pole or the other:

- for $\Delta t>0$, close the contour in the lower half-plane and pick up the pole at $+E_{\vec p}$;
- for $\Delta t<0$, close in the upper half-plane and pick up the pole at $-E_{\vec p}$.

Write $p_+=(E_{\vec p},\vec p)$ and $p_-=(-E_{\vec p},\vec p)$. The residues are

$$
\mathrm{Res}_{p_0=+E_{\vec p}}\frac{\slashed p+m}{p_0^2-E_{\vec p}^2}
=\frac{\slashed p_++m}{2E_{\vec p}},
\qquad
\mathrm{Res}_{p_0=-E_{\vec p}}\frac{\slashed p+m}{p_0^2-E_{\vec p}^2}
=\frac{\slashed p_-+m}{-2E_{\vec p}},
$$

with $\slashed p_\pm=iR_{\vec e_x}^{\mathrm{axf}}(\pm E_{\vec p})-\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_k$.

The contour contributes $-2\pi i$ when it closes below and $+2\pi i$ when it closes above. With the residues above and the overall factor $i$ of $S_F$, the two cases are

$$
\Delta t>0:\quad i\,(-2\pi i)\,\frac{\slashed p_++m}{2E_{\vec p}}
=2\pi\,\frac{\slashed p_++m}{2E_{\vec p}},
$$

$$
\Delta t<0:\quad i\,(+2\pi i)\,\frac{\slashed p_-+m}{-2E_{\vec p}}
=2\pi\,\frac{\slashed p_-+m}{2E_{\vec p}},
$$

in both lines the product of the two imaginary units being $i^2=-1$.

Both carry the same **positive** weight: the sign of the half-plane and the sign inside the residue cancel, and the $2\pi$ cancels against the $1/(2\pi)$ of the $p_0$ measure, leaving $1/(2E_{\vec p})$, which is the normalisation of $W_\pm$. The fermionic minus is therefore not in the contour, and it must come from the numerator. For $\Delta t>0$ the $p_0$ integral is already the positive-frequency integrand of $W_+$. For $\Delta t<0$ it is

$$
\frac{\slashed p_-+m}{2E_{\vec p}}\,\exp(+iE_{\vec p}\Delta t+i\vec p\cdot\Delta\vec x).
$$

Now flip the integration variable, $\vec p\to-\vec p$: the measure and $E_{\vec p}$ are unchanged, and the spatial phase reverses. The cell is linear in the four-momentum, so flipping all four components flips its sign,

$$
\slashed p_-(-\vec p)=iR_{\vec e_x}^{\mathrm{axf}}(-E_{\vec p})-\sum_{k=1}^{3}iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}(-p_k)=-\slashed p_+(\vec p),
$$

and the numerator of the flipped expression becomes

$$
\slashed p_-(-\vec p)+m=-\big(\slashed p_+(\vec p)-m\big),
$$

which is the negative-frequency numerator of $W_-$ with a minus. The single covariant expression, with its single factor of $i$ in front, therefore reproduces both the time ordering and the fermionic minus.

Three things are conflated in the phrase "the $i\epsilon$ does the time ordering", and they are worth separating.

1. The $i\epsilon$ fixes which pole lies in which half-plane; that is the boundary condition, and its sign is the choice of propagator.
2. The overall $i$ fixes the normalization of the amplitude relative to the two $\theta$ terms.
3. The minus in front of $W_-$ is carried by the numerator, through the spin sums $\sum w\bar w=\slashed p+m$ and $\sum v\bar v=\slashed p-m$. It is the two-point form of the anticommutation, and it has no counterpart in the scalar case, where the two residues share one numerator and the time-ordered combination is $\theta W_++\theta W_-$.

**A recomputation on a case chosen for it.** Take $m=0.7$ and $\vec p=(0.3,-0.9,1.1)$, so that $|\vec p|=1.4525839046$ and $E_{\vec p}=1.6124515497$. Recomputing the spinors, the two equations $(\slashed p-m)w^{(r)}=0$ and $(\slashed p+m)v^{(r)}=0$, the normalizations and the spin sums gives a maximum deviation of $4.4\times10^{-16}$, and $1.7\times10^{-15}$ over nine further random on-shell momenta. The cell identity

$$
(\slashed p-m)(\slashed p+m)=(\slashed p)^2-m^2\,\mathbf{1}=(p^2-m^2)\,\mathbf{1}
$$

is an identity, not a coincidence: it is the square of the cell derived above, and it holds for off-shell $p$ as well. Evaluated numerically it deviates by $3.6\times10^{-15}$. For $\epsilon=10^{-3}$ the Feynman poles come out at

$$
p_0=+1.61245155-i\,3.10\times10^{-4}
\qquad\text{and}\qquad
p_0=-1.61245155+i\,3.10\times10^{-4},
$$

that is, one on each side of the real axis, as claimed. A direct numerical evaluation of the $p_0$ integral along the real axis — grid refined to $2\times10^{-4}$ within $|p_0|<6$ and cut at $|p_0|=10^3$ — reproduces all sixteen components of the $\theta$-combination for both signs of $\Delta t$ to $2.5\times10^{-3}$ at $\epsilon=10^{-2}$ and $2.9\times10^{-4}$ at $\epsilon=10^{-3}$; the residual tracks the resolution of the two poles, which sit a distance $\epsilon/(2E_{\vec p})$ from the real axis. The relative minus was verified by evaluating the two branches separately and comparing with $\theta(x_0-y_0)W_+-\theta(y_0-x_0)W_-$.

## Feynman, Retarded, and Advanced: What Selects the Contour

The pole structure makes the choice of propagator explicit. Three prescriptions are available, and they differ only in how the two poles are displaced:

| Prescription | Denominator | Poles (to first order in $\epsilon$) |
|---|---|---|
| Feynman | $p_0^2-E_{\vec p}^2+i\epsilon$ | $\pm E_{\vec p}\mp i\epsilon/(2E_{\vec p})$ (opposite sides) |
| Retarded | $(p_0+i\epsilon)^2-E_{\vec p}^2$ | $\pm E_{\vec p}-i\epsilon$ (both below) |
| Advanced | $(p_0-i\epsilon)^2-E_{\vec p}^2$ | $\pm E_{\vec p}+i\epsilon$ (both above) |

The three are distinguished by whether the displacements are **opposite** (Feynman) or **common** (retarded and advanced). The displacement in the first row is smaller by the factor $2E_{\vec p}$ because that prescription shifts the denominator by $i\epsilon$ while the other two shift $p_0$ by $\pm i\epsilon$; only the pattern of sides matters for the contour. For $\epsilon=10^{-3}$ and the same momentum, the retarded poles are at $1.61245155-i\,10^{-3}$ and $-1.61245155-i\,10^{-3}$, and the advanced poles at the same points with $+i\,10^{-3}$: both on the same side, as the table states. Closing the contour then shows at once why the retarded propagator vanishes for $x_0-y_0<0$ and the advanced one for $x_0-y_0>0$: with both poles on one side, one of the two half-planes contains no pole.

The companion *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form* lists the same three displacements in the frequency $\omega$ and with the denominator written as $\vec p^2+\mu^2-\omega^2$, the negative of the one here; the pole positions agree.

This is the physical content of the $i\epsilon$, and it is exactly the content the algebra does not supply. The Feynman choice encodes the time-ordered vacuum correlation; the retarded choice encodes causal response to a source; the advanced choice is its mirror. They solve the *same* differential equation off the source and differ only in support. A choice among them is a boundary condition on the distributional inverse, and boundary conditions are not algebraic data. *Maxwell's Equations in Biquaternionic Form* meets the same situation: it selects the retarded kernel as "the physically relevant" one, and it states that the retarded kernel is a different object from the elliptic Cauchy kernel of the analysis articles, the two being related by the Wick rotation. The selection there is made on physical grounds, not read off the algebra, and the same is true here.

## The Biquaternion Form of the Prescription

The Feynman denominator has a compact biquaternion form. With the four-momentum biquaternion $\tilde P=iE\,e_t+\vec p$, where $E$ denotes the timelike component, the same $p_0$ the contour integral runs over, and its quaternion conjugate $\tilde P^{\natural}=iE\,e_t-\vec p$, the quaternion product is

$$
\tilde P\tilde P^{\natural}=(iE)^2+\vec p^2=-E^2+\vec p^2=-p^2 .
$$

Two signs enter, and they come from two different places. The scalar one is $i^2=-1$, which takes $(iE)^2$ to $-E^2$. The vector one is a **plus**: the vector part multiplies $-\vec p$, and $\vec p\,(-\vec p)=+\vec p^2$, because the quaternion square of a vector is $\vec p\,\vec p=-\vec p^2$ with $\vec p^2=p_x^2+p_y^2+p_z^2$ the Euclidean square. The last step is $p^2=E^2-\vec p^2$.

The mass shell is then the single algebraic condition

$$
\tilde P\tilde P^{\natural}=-m^2
\;\Longleftrightarrow\;
-E^2+\vec p^2=-m^2
\;\Longleftrightarrow\;
E^2-\vec p^2=m^2
\;\Longleftrightarrow\;
E^2=\vec p^2+m^2 ,
$$

whose two frequency branches $E=\pm E_{\vec p}$ are the two poles $p_\pm$ of section *The Pole Structure and the Contour*. Substituting $\tilde P\tilde P^{\natural}=-p^2$ in the amplitude gives the biquaternion form,

$$
\boxed{\;S_F(p)\;=\;\frac{i(\slashed p+m)}{p^2-m^2+i\epsilon}
\;=\;-\,\frac{i(\slashed p+m)}{\tilde P\tilde P^{\natural}+m^2-i\epsilon}\;},
$$

the denominator being the **deformed mass-shell operator** $\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2$, shifted by $-i\epsilon$. The prescription is thus a deformation of the scalar on which the mass shell is defined, not an addition to the algebra.

The shift has a natural algebraic home. The deformation is $-i\epsilon\,e_t$: a central element, purely imaginary as a scalar coefficient and with no vector part. Being anti-Hermitian it lies on the material side, and being central it lies in $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$. Since $\epsilon$ is real, $-i\epsilon\,e_t=-\epsilon\,(ie_t)$, so it is a **real** multiple of the $ict'$ direction, the direction in which the framework writes the material time. Both statements describe one element: the shift is imaginary relative to the scalar unit $e_t$ and real relative to the time direction $ie_t$, exactly as $Q_t=ict'$ is.

One caveat belongs here, because it is the kind of sign that hides in prose. The Feynman term is **added to the scalar** $\mathcal{M}(\tilde P)$, and as an element it is anti-Hermitian. Displacing the four-momentum biquaternion is a different operation. With $\tilde P\to\tilde P+\delta e_t$,

$$
\tilde P\tilde P^{\natural}\;\longmapsto\;-p^2+2iE\delta+\delta^2 ,
$$

so reproducing the term requires $\delta=-\epsilon/(2E)$, which is **real**: the equivalent displacement of the momentum runs along the Hermitian direction, not the material one. The two readings agree on the pole positions to first order in $\epsilon$ and disagree on which sector the deformation lives in. The article's claim is the first: $\tilde P$ is not displaced, the central scalar is, and it is that added term which lies in $\mathbb{M}_-$. Read as a displacement of the momentum, the $i\epsilon$ would sit in the informational sector, because $\tilde P$ carries its energy through $i$.

The algebra therefore does three things here, and it is worth separating them:

1. It provides the complex plane in which the contour is drawn — the coefficient complex structure of $\mathbb{C}_{\mathbb{B}}$.
2. It locates the direction of the added term, the $ict'$ axis of $\mathbb{M}_-$.
3. It makes the undeformed mass shell a single algebraic condition $\tilde P\tilde P^{\natural}=-m^2$, so that the two poles are the two branches of one equation rather than two unrelated objects.

What it does not do is choose the orientation. Replacing $\epsilon$ by $-\epsilon$ reverses the pole displacements, turning the Feynman propagator into the anti-Feynman one; replacing the opposite displacement by a common one gives the retarded or advanced propagator. All three denominators are built from the same $\tilde P\tilde P^{\natural}+m^2$ and the same central $i$. The algebra cannot tell them apart, because the difference is not in the algebra; it is in which half-plane the contour closes, equivalently in which boundary condition defines the distribution. The $i\epsilon$ is therefore written *with* the algebra's complex structure and *lives in* its material sector, but it is not *produced* by either. The algebra names the axis; the physics chooses the direction.

The closest the complex structure comes to doing real work is the Wick rotation. On the material sector the d'Alembertian reads

$$
\Box=-\frac{\partial^2}{\partial t'^2}+\Delta ,
$$

a hyperbolic operator: one sign against three. The substitution $t'=-i\tau$ turns $\partial^2/\partial t'^2$ into $-\partial^2/\partial\tau^2$, so the same operator becomes

$$
\Box \;\longmapsto\; \frac{\partial^2}{\partial\tau^2}+\Delta ,
$$

which is elliptic: all four directions now carry the same sign, and that single sign flip is exactly what separates the hyperbolic reading from the elliptic one. The Euclidean Green's function of the elliptic operator is unique once one demands decay at infinity, and its analytic continuation back to real time is the Feynman propagator. In that route the complexification of time is exactly what makes the continuation available.

But the selection is still analytic, not algebraic. The step "continue the unique Euclidean Green's function" is the input: uniqueness rests on a decay condition in the Euclidean variables, and the direction of the rotation is a further choice, equivalent to the sign of $\epsilon$. Nothing in $\mathbb{B}$ prefers decaying-in-Euclidean over growing. So the Wick rotation exhibits the algebra's complex structure as a *necessary* carrier of the continuation, and the analytic input as the thing that fixes which continuation; it does not convert the algebra into a derivation of the Feynman prescription.

## The Propagator as a Distribution

It matters that $S_F$ is a distribution, and not only because the statement is true. The integral defining it converges for no real $p$ on the mass shell; the mass shell is precisely the pole set, and the unregulated amplitude $(\slashed p+m)/(p^2-m^2)$ is undefined there. The $i\epsilon$ is what turns the algebraic inverse of $\slashed p-m$ off the mass shell into a distributional inverse on all of momentum space.

The propagator on the spinor-module representative of the chiral pair satisfies

$$
(\mathbb{D}-m)\,S_F(x-y)=i\,\delta^{(4)}(x-y),
\qquad
S_F=(\mathbb{D}+m)\,G_F,
\qquad
(\Box-m^2)\,G_F=i\,\delta^{(4)},
$$

in the distributional sense, with $\mathbb{D}$ the pair operator of the conventions article, $\mathbb{D}\Psi=(\tilde\nabla\Psi_R,\tilde\nabla^{\natural}\Psi_L)$ and $\mathbb{D}^2=\Box$. The overall factor is a normalization: the conventions article writes the Green matrix $\mathcal{S}=(\mathbb{D}+m)G$ with $(\mathbb{D}-m)\mathcal{S}=\delta I$, whereas the time-ordered product of this article carries $S_F=i\mathcal{S}$; the companion Klein–Gordon article fixes $(\Box-\mu^2)G=-\delta^{(4)}$ at $\mu=m$, so its $G$ is $i$ times the $G_F$ here — the opposite sign to the conventions article's, which that article records as a convention compensated by a minus in the convolution. None of the three normalizations affects a pole position or a support. The differential equation holds for the Feynman, retarded, and advanced choices alike, because the difference between them is supported only on the mass shell and carries no additional source off it. The differential equation, therefore, does not determine the propagator. What determines it is the time-ordering prescription, which in momentum space is the contour and in configuration space is the split of support into $x_0>y_0$ and $x_0<y_0$.

This is the sharpest way to see why the question "does the algebra supply the $i\epsilon$?" cannot be answered by finding an $i$ in the algebra. The equation of motion supplies a differential operator, and a differential operator has many distributional inverses; the algebra supplies the operator $\tilde{\nabla}$ (or its second-order companion $\tilde{\nabla}\tilde{\nabla}^{\natural}$) and hence the same many inverses. Distinguishing the Feynman one requires a condition that is not an equation of motion. The complex structure enters when that condition is *represented* — as a contour in $\mathbb{C}_{\mathbb{B}}$, or as a point in the complexified time plane — and not when it is *chosen*.

## Relation to the Thermal Two-Point Function

One further structure is worth recording, because it is the place where the framework's complex time does carry a genuinely analytic condition. The companion article *The KMS Condition and the Biquaternion Framework* characterizes thermal equilibrium by the analyticity of the correlation function $F_{AB}(t')=\omega_\beta(A\,\alpha_{t'}(B))$ in the strip $0<\mathrm{Im}(t')<\beta$, with boundary relation $F_{AB}(t'+i\beta)=F_{BA}(-t')$; the imaginary-time direction is intrinsic to the material sector $\mathbb{M}_-$, and the companion quantization article shows that the anticommutator turns the boundary relation into the Fermi–Dirac distribution and the antiperiodic Matsubara frequencies $\omega_n=(2n+1)\pi/\beta$.

At finite temperature the time-ordered two-point function is not given by a vacuum contour integral but by the discrete Matsubara sum over the compact imaginary-time circle; the real-time retarded and advanced propagators still carry their own $\epsilon$ prescriptions, and they are obtained from the Matsubara sum by analytic continuation, not by an algebraic operation. The imaginary-time complexification that the algebra carries is a real feature of the thermal state — it is where the KMS analyticity lives — but it does not select the vacuum contour either. It is a consistency: the imaginary direction the framework already uses for the material time is the direction in which the thermal correlation functions are analytic, and the vacuum contour is recovered as the $\beta\to\infty$ limit rather than derived from the algebra.

## What the Algebra Adds and What It Does Not

**Standard field theory, transcribed.** The mode expansion and the mode anticommutators of the companion article; the two elementary two-point functions $W_+$ and $W_-$ and their spin sums; the covariant representation of $S_F$ with its contour; the identification of the pole displacements with the Feynman, retarded, and advanced propagators; the distributional equation $(\mathbb{D}-m)S_F=i\delta$; and the finite-temperature reduction to the Matsubara sum. None of this is new, and none of it depends on the biquaternion structure beyond the kinematical conventions already fixed by the read-list articles.

**What the biquaternion notation provides.** The deformed mass-shell scalar $\tilde P\tilde P^{\natural}+m^2-i\epsilon$; the pole set as the two branches of one algebraic condition; and a place for the added term in the centre $\mathbb{C}_{\mathbb{B}}$, along the $ict'$ axis of the material sector $\mathbb{M}_-$ — a place, not a necessity, for the reason recorded above.

**What remains open in the framework.**

- **The intrinsic operator.** Whether a genuinely $\mathbb{B}$-valued two-point function $\langle 0|T\tilde{\Psi}(\tilde{Q})\tilde{\Psi}^\flat(\tilde{Q}_2)|0\rangle$, paired with the $2\times2$ trace $2\,\mathrm{Sc}(\cdot)$ or the biquaternion norm, exists and reproduces the spinor-module $S_F$. The companion quantization article leaves the intrinsic field open; this article inherits that gap.
- **Whether the algebra can *select* the contour.** We have argued that it cannot, on the ground that Feynman, retarded, and advanced differ only by boundary condition. A derivation of the Feynman prescription from an algebraic property of $\mathbb{B}$ alone would contradict that argument; we record the contrary as a possibility but do not claim it, and we have found no candidate.
- **The meaning of the $\mathbb{M}_-$ location.** That the deformation lies along the $ict'$ direction may be a genuine structural fact — the same direction as the KMS strip — or an artifact of writing $\epsilon$ as a scalar. The alternative reading above, in which the same shift appears as a Hermitian displacement of $\tilde P$, is the concrete form of the doubt: the sector depends on whether one deforms the scalar or the momentum. We have not distinguished the two readings.
- **Empirical content.** As with the rest of the framework, whether any of this yields a prediction distinguishing it from standard quantum field theory is open, and the present article changes nothing about it.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5[\mathbb{M}_-]$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5[\mathbb{M}_-]$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

The body's momentum cell then reads

$$
\slashed p=\gamma_0[\mathbb{M}_-]p_0-\sum_k\gamma_k[\mathbb{M}_-]p_k ,
$$

the spatial signs being those of $\varepsilon=(1,-1,-1,-1)$. The frame satisfies the Clifford relation

$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}\mathbf{1},
$$

which is the frame-cell anticommutator of the body: $\gamma_\mu[\mathbb{M}_-]$ *is* the cell $iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$, so this is the same statement, given here in its named form. It is not an extra input. For $\mu\neq\nu$ the two products $\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]$ and $\gamma_\nu[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]$ differ by a single transposition — on the left when one index is $t$, on the right when both are spatial — and a transposition reverses a quaternion sign, so they cancel; for $\mu=\nu$ each square is $\pm\mathbf{1}$, the sign coming from $e_t^2=e_t$ and $\vec e_k^2=-e_t$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Feynman propagator of the biquaternion Dirac field is the time-ordered two-point function

$$
S_F(x-y)=\langle 0|\,T\,\psi^{\mathrm{fop}}(x)\,\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}^{\mathrm{axf}}(y)\,|0\rangle .
$$

Its content is the contour prescription, and the prescription is fixed by time ordering together with the fermionic anticommutation sign:

$$
S_F(x-y)=i\int\!\frac{d^4p}{(2\pi)^4}\,\exp(-ip\cdot(x-y))\frac{\slashed p+m}{p^2-m^2+i\epsilon},
\qquad \slashed p=iR_{\vec e_x}^{\mathrm{axf}}p_0-\sum_{k=1}^{3}iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_k .
$$

The $p_0$ integral has poles at $p_0=\pm\big(E_{\vec p}-i\epsilon/2E_{\vec p}\big)$: the positive pole below the real axis and the negative pole above it. Closing below for $x_0-y_0>0$ and above for $x_0-y_0<0$ gives the two branches with the same positive weight $1/(2E_{\vec p})$, the sign of the half-plane cancelling the sign inside the residue and the $2\pi$ cancelling the measure; the fermionic relative minus is carried by the numerator: after $\vec p\to-\vec p$ the negative-frequency numerator obeys $\slashed p_-(-\vec p)+m=-(\slashed p_+(\vec p)-m)$, which is the two-point form of the anticommutation.

Writing the four-momentum biquaternion $\tilde P=iE\,e_t+\vec p$, so that $\tilde P\tilde P^{\natural}=-p^2$, the propagator amplitude becomes

$$
S_F(p)=-\frac{i(\slashed p+m)}{\tilde P\tilde P^{\natural}+m^2-i\epsilon},
$$

and the prescription is a deformation of the mass-shell scalar. The added term $-i\epsilon\,e_t$ is central and lies along the $ict'$ axis of the material sector $\mathbb{M}_-$; read instead as a displacement of $\tilde P$, the same shift would be Hermitian, so what is fixed is the place of the term, not a direction of the momentum. The Feynman, retarded, and advanced propagators differ only in whether the two pole displacements are opposite or common; the algebra provides the complex plane and the axis of the added term but not its orientation, which is a boundary condition on the distributional inverse. The algebra therefore adds notation and a natural home for the $i\epsilon$, not the selection of the Feynman contour.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $e_t=1$, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, central, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | Centre of $\mathbb{B}$ |
| $L_a,R_b$ | Left and right multiplication, $L_a\psi=a\psi$, $R_b\psi=\psi b$, $L_aR_bL_cR_d=L_{ac}R_{db}$ |
| $\mathbf{1}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | Identity cell |
| $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ | Frame cell of the coordinate $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$ |
| $\varepsilon=(1,-1,-1,-1)$ | sign vector of the cells, $\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}\}=2\varepsilon_\mu\delta_{\mu\nu}\mathbf{1}$ |
| $\slashed p=iR_{\vec e_x}^{\mathrm{axf}}p_0-\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_k$ | Momentum cell, $(\slashed p)^2=p^2\mathbf{1}$ |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_k \vec e_k\partial/\partial Q_k$ | Biquaternionic gradient; $Q_t$ is the time coordinate, $ict'$ on $\mathbb{M}_-$ |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ | d'Alembertian |
| $\mathbb{D}$ | Pair operator of the conventions article, $\mathbb{D}\Psi=(\tilde\nabla\Psi_R,\tilde\nabla^{\natural}\Psi_L)$, $\mathbb{D}^2=\Box$ |
| $\mathcal{N}=-\tilde\nabla^{\natural}-mi\,\overline{\,\cdot\,}\,\vec e_z$ | Two-sided Dirac operator of *The Dirac Equation in Biquaternionic Form* |
| $\tilde{\Psi}=\tilde{\Psi}_L+\tilde{\Psi}_R$, $\tilde{\Psi}^\flat=-\tilde{\Psi}^{*}$ | Biquaternion Dirac field on $\Delta=S\oplus S^{\mathrm c}$ and its anti-Hermitian conjugate |
| $\psi$, $\psi^\dagger iR_{\vec e_x}^{\mathrm{axf}}$ | Spinor-module representative and its adjoint |
| $p_\mu=(E,\vec p)$, $p_\pm=(\pm E_{\vec p},\vec p)$, $p^2=E^2-\vec p^2$ | Four-momentum, the two pole momenta, and the Lorentz square |
| $\psi^{\mathrm{fop}}$, $a_r^{\mathrm{fop}}(\vec p)$, $b_r^{\mathrm{fop}}(\vec p)$ | Quantized field; particle and antiparticle modes |
| $w^{(r)}(\vec p),v^{(r)}(\vec p)$ | Positive- and negative-frequency plane-wave spinors |
| $\bar w^{(r)}w^{(s)}=2m\delta_{rs}$, $\bar v^{(r)}v^{(s)}=-2m\delta_{rs}$ | Spinor normalizations |
| $\sum_r w^{(r)}\bar w^{(r)}=\slashed p+m$, $\sum_r v^{(r)}\bar v^{(r)}=\slashed p-m$ | Spin sums, on shell |
| $W_\pm(x-y)$ | Positive- and negative-frequency two-point functions |
| $S_F(x-y)=\langle 0|T\,\psi^{\mathrm{fop}}(x)\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}^{\mathrm{axf}}(y)|0\rangle$ | Feynman propagator |
| $\tilde P=iE\,e_t+\vec p$ | Four-momentum biquaternion, $\tilde P\tilde P^{\natural}=-p^2$ |
| $\tilde P\tilde P^{\natural}=-m^2$ | Biquaternion mass-shell condition |
| $\mathcal{M}(\tilde P)=\tilde P\tilde P^{\natural}+m^2$ | Mass-shell operator; Feynman shift $\mathcal{M}(\tilde P)-i\epsilon\,e_t$ |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace reading of the plain form, in the $2\times2$ image ($\mathrm{Tr}$ is representation-specific) |
| $\beta=1/(k_BT)$, $\omega_\beta$, $\alpha_{t'}$ | Inverse temperature, thermal state, Heisenberg evolution |
| $F_{AB}(t'+i\beta)=F_{BA}(-t')$ | KMS condition |
| $\omega_n=(2n+1)\pi/\beta$ | Fermionic Matsubara frequencies |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the derivation of the Feynman propagator from the time-ordered product and the contour prescription.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the pole structure, the retarded and advanced Green's functions, and their relation to the Feynman one.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Dirac propagator in the convention used here, with the overall factor of $i$.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the distributional treatment of propagators and the role of boundary conditions.
- N. N. Bogoliubov and D. V. Shirkov, *Introduction to the Theory of Quantized Fields* (Interscience, 1959), for the analytic properties of the two-point functions and the connection to the Euclidean continuation.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), and J. I. Kapusta and C. Gale, *Finite-Temperature Field Theory* (Cambridge, 2006), for the Matsubara formalism and the relation of the vacuum contour to the thermal sum.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic setting in which propagators are distributions and states are functionals.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Clifford-algebraic background to the biquaternion and spinor structures.
