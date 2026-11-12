# __Spin-Velocity Locking on the Degenerate Sector__

## Introduction

**On the spectrally degenerate sector the fluid's speed is a function of its spin angle, and the function is fixed by the algebra.** That is the article's whole result. The sector is defined by $B^{2}=0$ with $N\neq0$; on it the two axes of the two frames are orthogonal and the two angles satisfy

$$
\cosh\frac{\theta_{\mathrm{rpd}}}{2}\,\cos\frac{\theta_{\mathrm{axr}}}{2}=\varepsilon,
\qquad \varepsilon=\pm1,
$$

so a field that fixes its spin angle has no freedom left in its rapidity. The velocity is locked to the spin and the lock is not a choice: it is the condition that the element be spectrally degenerate.

**The consequence for the fluid is a one-parameter family of states.** A generic element has eight parameters, four of them angles and axes. On the sector the two angles collapse to one and the two axes are constrained to be orthogonal, so the fluid has a single angle and a single direction to play with besides its scale and phase. Speed, Lorentz factor and helicity are then all functions of that one angle, and the table below is the whole kinematics.

**The lock has two ends and one of them is singular.** At a vanishing spin angle the field is at rest and its spin is along the declared axis. At a spin angle of a half turn the constraint has no finite solution: the rapidity diverges, the velocity tends to the speed of light, and the sector's chart degenerates. Between the two ends the speed is monotonically increasing, and the fully helical state sits at a Lorentz factor of exactly three.

**What the article does not claim.** It does not claim that the sector is realised by any solution of the Dirac equation; it describes the sector and leaves the question of which fields lie on it to the corpus's dynamics. It does not claim that the lock extends off the sector; it holds only where $B^{2}=0$. It does not claim that the lock is a consequence of the field equation; it is a consequence of the algebraic condition.

**The lemma it uses is proved in the companion.** The closed form of $B^{2}$ on the word is [The Sign ε and the Rigidity Constraint on Σ₁₀](the-sign-epsilon-and-the-rigidity-constraint-on-sigma-10.html)'s, and this article quotes it. What this article adds is what the lemma does to the fluid.

## The Sector

### The Definition

**The sector is the set of elements that are invertible and spectrally degenerate.** In the corpus's notation $\Sigma_{10}$ is the set with $N\neq0$ and $B^{2}=0$: the norm does not vanish and the two eigenvalues coincide. [Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra](physical-interpretation-of-spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html) defines it and gives its physical reading as the defective unit, the element that is reversible without a mode basis.

**The two conditions are independent and both are needed.** $N=Q_t^{2}+B^{2}$ so a vanishing $B^{2}$ with a non-vanishing $N$ requires a non-vanishing $Q_t$: the element is a unit whose vector part is nilpotent. A vanishing $N$ with a vanishing $B^{2}$ is the origin, which is the doubly degenerate sector and a different object.

### Two Conditions on Eight Parameters

**The sector is the intersection of two real conditions and therefore has six dimensions.** The first condition is that the two axes be orthogonal, $\kappa=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$, and it is one real equation on the pair of unit vectors. The second is the locking identity, and it is one real equation on the two angles. Both are proved in the next section.

| parameter | generic element | on $\Sigma_{10}$ |
| --- | --- | --- |
| scale $r$ | free | free |
| phase $\theta_{\mathrm{pha}}$ | free | free |
| rapidity $\theta_{\mathrm{rpd}}$ | free | a function of $\theta_{\mathrm{axr}}$ |
| boost axis $\vec u_{\mathrm b}$ | free unit vector | free unit vector |
| rotor angle $\theta_{\mathrm{axr}}$ | free | the independent one |
| rotor axis $\vec u_{\mathrm r}$ | free unit vector | orthogonal to $\vec u_{\mathrm b}$ |
| total | 8 | 6 |

**The count is the sector's dimension and the fluid's degrees of freedom at once.** Six real parameters, of which two are the scale and the phase that no motion uses, leave four for the motion: one angle, one direction, and the two components of the transverse rotor axis that the orthogonality leaves.

## The Locking Identity

### The Lemma

**The closed form of $B^{2}$ on the word contains the sign $\varepsilon$ and a term that is purely imaginary.**

*Lemma.* With $\kappa=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ and the shorthand $c_b=\cosh\frac{\theta_{\mathrm{rpd}}}{2}$, $s_b=\sinh\frac{\theta_{\mathrm{rpd}}}{2}$, $c_a=\cos\frac{\theta_{\mathrm{axr}}}{2}$, $s_a=\sin\frac{\theta_{\mathrm{axr}}}{2}$,

$$
\frac{B^{2}}{\Rho^{2}}=1-\lvert\varepsilon\rvert^{2}+2i\kappa\,c_bc_a\,s_bs_a,
\qquad
\lvert\varepsilon\rvert^{2}=c_b^{2}c_a^{2}+\kappa^{2}s_b^{2}s_a^{2}.
$$

*Proof.* Write $\tilde\Xi=\Rho\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ and multiply the two units out. With $\vec u_{\mathrm b}=\vec u$, $\vec u_{\mathrm r}=\vec v$ and $\vec w=\vec u\times\vec v$,

$$
\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}
=\bigl(c_bc_a-i\kappa s_bs_a\bigr)e_t
+c_bs_a\,\vec v+is_bc_a\,\vec u+is_bs_a\,\vec w,
$$

so the scalar part is $\varepsilon$ and the vector part is $\vec Q=c_bs_a\vec v+is_bc_a\vec u+is_bs_a\vec w$. Then

$$
\vec Q\cdot\vec Q
=c_b^{2}s_a^{2}-s_b^{2}c_a^{2}-s_b^{2}s_a^{2}\lvert\vec u\times\vec v\rvert^{2}+2i\kappa\,c_bs_as_bc_a,
$$

and $\lvert\vec u\times\vec v\rvert^{2}=1-\kappa^{2}$. Replacing $s_a^{2}$ by $1-c_a^{2}$ in the first term turns $c_b^{2}s_a^{2}-s_b^{2}$ into $1-c_b^{2}c_a^{2}$, and the $\kappa^{2}$ term absorbs into $\lvert\varepsilon\rvert^{2}$ as written.

**Checked on six random configurations.** With $\vec u_{\mathrm b}=\vec e_x$, $\vec u_{\mathrm r}$ at cosine $\kappa$, and six random triples of $(\theta_{\mathrm{rpd}},\theta_{\mathrm{axr}},\kappa)$, the computed $B^{2}$ agrees with the display to every printed digit. Two of the six: at $\theta_{\mathrm{rpd}}=0.971$, $\theta_{\mathrm{axr}}=0.935$, $\kappa=0.302$ the value is $0.004741+0.137403i$; at $\theta_{\mathrm{rpd}}=0.217$, $\theta_{\mathrm{axr}}=3.322$, $\kappa=-0.269$ it is $0.992595+0.005292i$.

### The Theorem

**The sector is exactly the orthogonal locus with the identity's two solutions.**

*Theorem.* $\tilde\Xi$ lies on $\Sigma_{10}$ if and only if $\kappa=0$ and $c_b^{2}c_a^{2}=1$.

*Proof.* By the lemma, $B^{2}=0$ needs both the real and the imaginary parts of $1-\lvert\varepsilon\rvert^{2}+2i\kappa c_bc_as_bs_a$ to vanish. The imaginary part is $2\kappa c_bc_as_bs_a$, and $c_b>0$ always, so it vanishes exactly when $\kappa=0$ or $s_a=0$ or $s_b=0$. Take the three cases.

- $\kappa=0$: the imaginary part vanishes identically and the real part is $1-c_b^{2}c_a^{2}$, so $B^{2}=0$ is the identity $c_b^{2}c_a^{2}=1$.
- $s_a=0$, that is $\theta_{\mathrm{axr}}=0$ or $\pi$: the imaginary part vanishes, and the real part is $1-c_b^{2}c_a^{2}$ with $c_a^{2}=1$, which is $1-c_b^{2}=-s_b^{2}$, vanishing only at $\theta_{\mathrm{rpd}}=0$. That is the scalar line, which is one point of the first case.
- $s_b=0$, that is $\theta_{\mathrm{rpd}}=0$: the imaginary part vanishes, the real part is $1-c_a^{2}=s_a^{2}$, vanishing only at $\theta_{\mathrm{axr}}=0$. That is again the scalar line.

So on the complement of the scalar line the imaginary part forces $\kappa=0$, and then the real part forces the identity. The scalar line itself is contained in the first case.

**The theorem's content is that the sector has no skew configurations.** A spectrally degenerate unit cannot have two frames whose axes are at any angle other than a right angle. That is a strong statement and it is what makes the sector a two-parameter family rather than a four-parameter one.

### The Identity's Two Branches

**The identity $c_bc_a=\pm1$ has one branch per sign, and the branches are the two sheets of the sector.** Since $c_b\ge1$ and $\lvert c_a\rvert\le1$, the identity forces $\lvert c_a\rvert\le1$ to be exactly $1/c_b$, so the spin angle and the rapidity are tied monotonically on each sheet.

- **The branch with $c_a>0$** is $\theta_{\mathrm{axr}}\in[0,\pi)$, and the spin angle runs through the forward half turn.
- **The branch with $c_a<0$** is $\theta_{\mathrm{axr}}\in(\pi,2\pi]$, and the same rapidity is reached by the spin angle on the other side of $\pi$.

**The two sheets are the two signs of $\varepsilon$ and they are not related by a symmetry of the algebra.** [The Sign ε and the Rigidity Constraint on Σ₁₀](the-sign-epsilon-and-the-rigidity-constraint-on-sigma-10.html) treats the sign's range and its complex extension; here only the consequence matters, that the two sheets cover different halves of the spin angle and give the same speed.

## The Kinematics

### Speed Is a Function of the Spin Angle

**Eliminating the rapidity gives the Lorentz factor directly in the spin angle.** From $c_bc_a=\pm1$, $c_b=1/\lvert c_a\rvert$ and $\cosh\theta_{\mathrm{rpd}}=2c_b^{2}-1$, so

$$
\gamma=2\sec^{2}\frac{\theta_{\mathrm{axr}}}{2}-1,
\qquad
\frac{v}{c}=\tanh\theta_{\mathrm{rpd}},
\qquad
\beta=\sqrt{1-\frac{1}{\gamma^{2}}}.
$$

**The table is the kinematics of the sector.** Each row is a spin angle, and the speed is not a free entry.

| $\theta_{\mathrm{axr}}$ | $\cos\frac{\theta_{\mathrm{axr}}}{2}$ | $\theta_{\mathrm{rpd}}$ | $\gamma$ | $v/c$ |
| --- | --- | --- | --- | --- |
| $0$ | $1$ | $0$ | $1$ | $0$ |
| $\pi/2$ | $0.707107$ | $1.76275$ | $3$ | $0.942809$ |
| $2\pi/3$ | $0.5$ | $2.63392$ | $7$ | $0.989743$ |
| $5\pi/6$ | $0.258819$ | $4.05518$ | $28.8564$ | $0.999399$ |
| $\pi$ | $0$ | $\infty$ | $\infty$ | $1$ |

**The numbers are exact where they look exact.** The Lorentz factors $1$, $3$ and $7$ are $2\sec^{2}-1$ at cosines $1$, $2^{-1/2}$ and $1/2$, and the corresponding speeds are $0$, $2\sqrt{2}/3$ and $10\sqrt{2}/7$. Checked against the word: at $\theta_{\mathrm{axr}}=\pi/2$ the computed $B^{2}$ is $4.4\times10^{-16}$ and $\varepsilon=1.000000$, and at $\theta_{\mathrm{axr}}=2\pi/3$ they are $2.2\times10^{-16}$ and $1.000000$, so the locking identity holds to machine zero.

**The monotonicity is the theorem's second face.** Speed rises with the spin's rotation angle, from rest at zero to the speed of light at the half turn, and it does so without bound in the rapidity. A sector field cannot be fast and slowly spinning.

### Helicity in the Aligned Configuration

**With the declared axis orthogonal to the rotor axis, the spin direction is a fixed combination of the declared axis and the direction of motion.** Write $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ and take $\vec e_z\perp\vec u_{\mathrm r}$. Then

$$
\hat s=\cos\theta_{\mathrm{axr}}\,\vec e_z+\sin\theta_{\mathrm{axr}}\,\vec u_{\mathrm r}\times\vec e_z,
$$

and with $\vec u_{\mathrm b}\perp\vec u_{\mathrm r}$ the second vector is along $\vec u_{\mathrm b}$ up to the sign of the triple product. In the configuration where $\vec u_{\mathrm r}\times\vec e_z=\vec u_{\mathrm b}$,

$$
\frac{\hat s\cdot\vec v}{\lvert\vec v\rvert}=\sin\theta_{\mathrm{axr}},
\qquad
\lvert\hat s_{\perp}\rvert=\lvert\cos\theta_{\mathrm{axr}}\rvert.
$$

**Checked on three sector elements.** At $\theta_{\mathrm{axr}}=0.5$ the spin is $(0.4794,0,0.8776)$ and $\hat s\cdot\hat v=+0.479426$; at $\pi/2$ it is $(1,0,0)$ and $+1.000000$; at $2.0$ it is $(0.9093,0,-0.4161)$ and $+0.909297$. The values are $\sin\theta_{\mathrm{axr}}$ in each case.

**So the sector's fully helical state is at $\gamma=3$ and not at the speed of light.** At $\theta_{\mathrm{axr}}=\pi/2$ the spin is entirely along the motion and the speed is $0.9428c$. That is the article's sharpest physical statement: on this sector the maximum helicity is attained at a definite subluminal speed, because higher speeds belong to larger spin angles whose spin is turning back out of alignment.

**The general configuration has the same structure with a different projection.** Without $\vec e_z\perp\vec u_{\mathrm r}$ the helicity is $\cos\theta_{\mathrm{axr}}(\vec e_z\cdot\hat v)+\sin\theta_{\mathrm{axr}}((\vec u_{\mathrm r}\times\vec e_z)\cdot\hat v)$, so the two terms are weighted by the frame's orientation and the maximum is not attained at $\pi/2$. The lock on the speed is unaffected, because it does not involve the declared axis.

## The Antipode

**At a spin angle of a half turn the constraint has no finite solution.** The identity reads $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}=\pm1$, and at $\theta_{\mathrm{axr}}=\pi$ the second factor is zero while the first is at least one, so no rapidity satisfies it.

**The failure is a divergence and not a jump.** As the spin angle approaches $\pi$, the rapidity grows without bound and the velocity tends to $c$. Checked directly on $B^{2}$: at $\theta_{\mathrm{axr}}=\pi$ and $\vec u_{\mathrm r}\perp\vec u_{\mathrm b}$, the value is $+1$ at $\theta_{\mathrm{rpd}}=2$, $+1$ at $8$ and $+1$ at $20$ — the element moves further and further from the sector as the rapidity grows, and $B^{2}$ stays at the value $1-c_b^{2}c_a^{2}=1$ that the theorem predicts.

**The limit is null in the motion and not in the element.** The norm of the element is $\Rho^{2}$ for every rapidity, so the element stays a unit at the antipode's approach: it is the *velocity* that becomes null, not the field. That distinction matters for the reading, because it says that the sector's far end is a massless limit of the motion at a fixed element and not a massless element.

**What sits at the far end is a transverse spin at the speed of light.** At $\theta_{\mathrm{axr}}=\pi$ the spin direction is $-\vec e_z$, orthogonal to the motion, and the helicity is zero. A massless particle of the standard theory has helicity $\pm1$; this limit has helicity zero, so the sector's far end is not the standard massless state. It is the chart's degeneracy, and the article records it as such.

## What the Locking Does Not Give

### It Does Not Impose the Frenkel Condition

**The lock says nothing about the spin's transversality to the flow, and on this sector the spin is generally not transverse.** The corpus's Frenkel condition is a statement about the spin tensor, $S^{\mu\nu}v_{\Phi,\nu}=0$, and it is automatic for a spin carried by a real vector: it constrains the tensor and not the vector. A different condition, that the spin vector be orthogonal to the four-velocity, is sometimes given the same name, and it is not the corpus's condition.

**Under that other condition the sector would be almost empty.** With the spin along the motion at $\theta_{\mathrm{axr}}=\pi/2$ the vector is parallel to the velocity and the orthogonality would fail, so the other condition would exclude every sector element except $\theta_{\mathrm{axr}}=0$ and $\pi$. The sector's existence therefore depends on which condition is meant, and [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html) fixes which one the corpus uses.

### It Does Not Supply the Connection

**The lock fixes the values of the rapidity and the spin angle and leaves their gradients free.** The four brackets of the polar derivative are still four, and the field equation still constrains them jointly without closing them. On the sector they collapse by one, because the rapidity's gradient is the spin angle's gradient times $\pm\sec(\theta_{\mathrm{axr}}/2)$,

$$
\frac{\partial\theta_{\mathrm{rpd}}}{\partial R_\mu}
=\pm\sec\frac{\theta_{\mathrm{axr}}}{2}\,\frac{\partial\theta_{\mathrm{axr}}}{\partial R_\mu},
$$

with the sign the branch's, so the velocity's transport is tied to the spin's — but the spin's transport equation is still missing, and the sector does not supply it.

**That is the honest limit of the article's result.** The lock is a constraint on the state and not a dynamics. It reduces the number of independent fields and it does not close the system.

## What Is Established and What Is Interpretation

**Established.** The closed form of $B^{2}/\Rho^{2}$, checked on six configurations. The theorem that $\Sigma_{10}$ is exactly the orthogonal locus with $c_b^{2}c_a^{2}=1$, proved from that form. The dimension count of six. The kinematic table, checked against the word at three spin angles. The absence of a finite rapidity at the antipode, checked at three rapidities. The helicity formula in the aligned configuration, checked at three angles.

**Interpretation.** That the sector is a fluid with one internal angle. That the fully helical state's speed of $0.9428c$ is a property of the sector rather than an artefact of the coordinates. It is not a prediction, because no solution of the Dirac equation is known to lie on the sector. That the antipode's null velocity is the chart's degeneracy rather than a massless particle. Each is argued here and none is proved.

**Not claimed.** It is not claimed that any solution of the Dirac equation lies on the sector; the corpus has not constructed one. It is not claimed that the sector is stable or reachable. It is not claimed that the helicity statement is frame independent; it is stated in the aligned configuration and the general formula is given.

## Summary

On the spectrally degenerate sector $B^{2}=0$ with $N\neq0$ the two frames' axes are necessarily orthogonal, and the two angles satisfy $\cosh(\theta_{\mathrm{rpd}}/2)\cos(\theta_{\mathrm{axr}}/2)=\pm1$. The sector therefore has six real parameters against the generic eight, and its motion has one independent angle.

The Lorentz factor is $2\sec^{2}(\theta_{\mathrm{axr}}/2)-1$, so the speed is a function of the spin angle: rest at zero, $\gamma=3$ at a quarter turn, $\gamma=7$ at a third of a turn, and the speed of light at a half turn, where no finite rapidity solves the identity.

In the aligned configuration the spin's component along the motion is $\sin\theta_{\mathrm{axr}}$, so the fully helical state sits at $\gamma=3$ and $0.9428c$, and the maximally transverse states sit at the two ends.

The lock is a constraint on the state and not a dynamics: it ties the velocity's gradient to the spin's and leaves the spin's transport equation open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Sigma_{10}$ | The sector $N\neq0$, $B^{2}=0$ |
| $B^{2}=-\vec Q\cdot\vec Q$ | Square of the element's vector part |
| $\kappa=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | Cosine between the boost and rotor axes |
| $c_b,s_b$ | $\cosh$, $\sinh$ of half the rapidity |
| $c_a,s_a$ | $\cos$, $\sin$ of half the rotor angle |
| $\varepsilon=\Xi_t/\Rho$ | Scalar part relative to the modulus |
| $\Rho=r\,e^{i\theta_{\mathrm{pha}}}$ | Modulus of the norm |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$ | Lorentz factor |
| $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | Spin direction |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter, Part I. General theory," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin fluid and the role of the spin angle.
- David Hestenes, "Space–time structure of the Dirac theory," in *Clifford Algebras and their Applications in Mathematical Physics* (Reidel, 1986), for the rotor reading of the spin and the velocity.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the relativistic spin fluid's kinematics.
- The companion articles: [The Sign ε and the Rigidity Constraint on Σ₁₀](the-sign-epsilon-and-the-rigidity-constraint-on-sigma-10.html), [Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra](physical-interpretation-of-spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), [The Non-Uniqueness of the Spin Fluid](the-non-uniqueness-of-the-spin-fluid.html), [The Current Algebra](the-current-algebra.html).
