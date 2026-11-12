# __The Sign ε and the Rigidity Constraint on Σ₁₀__

## Introduction

**The sign $\varepsilon$ is a derived number and not a label, and the sector $\Sigma_{10}$ is exactly the locus where it is $\pm1$.** The number is the scalar part of the element of [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html) divided by the modulus of its norm. It is complex in general, it vanishes on a set of its own, and it takes the values $\pm1$ precisely on the spectrally degenerate sector. The second statement is a theorem and this article proves it.

**The level set $\lvert\varepsilon\rvert=1$ is strictly larger than the sector, and that is where a careless reading goes wrong.** $\lvert\varepsilon\rvert=1$ is one real equation and selects a seven-dimensional set; the sector is six-dimensional. The difference is a phase: on the level set $\varepsilon$ may be any point of the unit circle, and the sector is the two points of that circle where the phase is a multiple of $\pi$.

**The bridge between the two is one closed form.** The square of the element's vector part, divided by the square of the modulus, is

$$
\frac{B^{2}}{\Rho^{2}}=1-\lvert\varepsilon\rvert^{2}+2i\kappa\,c_bc_a\,s_bs_a,
\qquad
\kappa=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r},
$$

so $\lvert\varepsilon\rvert=1$ kills the real part and leaves the imaginary part standing. The sector needs both to vanish. That single display is the article's technical core and every other statement here is its consequence.

**The constraint has a name and the name is earned.** On the sector the two angles are tied by $\cosh(\theta_{\mathrm{rpd}}/2)\cos(\theta_{\mathrm{axr}}/2)=\varepsilon$. This is the rigidity constraint: the rapidity is a function of the rotor's angle and not an independent variable. What follows for the fluid — a speed locked to a spin angle — is the next article's subject, [Spin-Velocity Locking on the Degenerate Sector](spin-velocity-locking-on-the-degenerate-sector.html); this article treats the algebraic side, the range of the sign, and the sense in which the constraint *defines* the sector rather than following from it.

## The Definition

### The Number

**The sign is the scalar part of the element divided by the modulus of its norm.** With $\Xi_t=\mathrm{Sc}\,\tilde\Xi$ and $\Rho$ the principal square root of the quaternionic norm,

$$
\varepsilon:=\frac{\Xi_t}{\Rho},
\qquad
N(\tilde\Xi)=\Rho^{2}=r^{2}e^{2i\theta_{\mathrm{pha}}}.
$$

**It is computed from the word and it is not a parameter of the word.** The word has eight parameters; $\varepsilon$ is a function of four of them, the rapidity, the rotor's angle and the two axes' mutual orientation. So a reader who met $\varepsilon$ in the spinor literature as a branch index chosen by a representation should note the difference: here nothing is chosen.

### The Display

**Only the dot product of the two axes survives beside the two cosines, because the cross product cannot reach the centre.** With $\vec u_{\mathrm b}\vec u_{\mathrm r}=-\kappa+\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ and $\kappa=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$,

$$
\varepsilon
=\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}
-i\,\kappa\,\sinh\frac{\theta_{\mathrm{rpd}}}{2}\sin\frac{\theta_{\mathrm{axr}}}{2},
$$

*Proof.* Multiply $\tilde U_{\Psi,\mathrm b}=(c_b,is_b\vec u_{\mathrm b})$ by $\tilde u_{\mathrm r}=(c_a,s_a\vec u_{\mathrm r})$ and read the scalar slot. The product of the two vector parts is $is_bs_a(-\kappa+\vec u_{\mathrm b}\times\vec u_{\mathrm r})$, whose scalar term is $-i\kappa s_bs_a$; the cross product is a vector and contributes nothing to the centre. The two scalar products give $c_bc_a$. The modulus is central and does not affect the ratio.

**The paper's convention has been changed here, and the change is deliberate.** Earlier statements of the display used the letter $c$ for the dot product, which collided with the speed of light in the same article. The letter $\kappa$ is used from here on, in [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html) and in this article alike.

### The Range

**The number is complex, it is real on the orthogonal locus, and it vanishes on a set of its own.** Three statements and each needs its condition.

| locus | $\varepsilon$ | $\lvert\varepsilon\rvert$ |
| --- | --- | --- |
| generic | complex | not one |
| $\kappa=0$ | real, $c_bc_a$ | $\lvert c_bc_a\rvert$ |
| $\kappa=0$, $\theta_{\mathrm{axr}}=\pi$ | $0$ | $0$ |
| $\kappa=0$, $c_bc_a=\pm1$ | $\pm1$ | $1$ |

**The zeros are the sharpest of the three and they are usually missed.** At $\theta_{\mathrm{axr}}=\pi$ the rotor is a pure vector, $c_a=0$, and with orthogonal axes the imaginary term also vanishes, so $\varepsilon=0$ at every rapidity. Checked: at $\theta_{\mathrm{rpd}}=0.5$, $2$ and $5$ with $\theta_{\mathrm{axr}}=\pi$ and $\kappa=0$ the modulus is $6.3\times10^{-17}$, $9.5\times10^{-17}$ and $3.8\times10^{-16}$, and $B^{2}=+1$ in all three cases.

**So $\varepsilon$ is not a sign and cannot be one.** A quantity that vanishes cannot be a label with two values. It is a complex coordinate of the word, and the two values $\pm1$ are a locus inside its range and not the range itself. The corpus's phrase "the sign $\varepsilon$" is a name kept from the spinor literature and the article records the mismatch.

## The Closed Form

**The square of the vector part is the object that decides the sector, and it splits into the modulus of $\varepsilon$ and a phase term.**

*Proposition.* With $\vec Q$ the vector part of $\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ and $c_b,s_b,c_a,s_a$ the half-angle sines and cosines,

$$
\frac{B^{2}}{\Rho^{2}}
=1-\lvert\varepsilon\rvert^{2}+2i\kappa\,c_bc_a\,s_bs_a,
\qquad
\lvert\varepsilon\rvert^{2}=c_b^{2}c_a^{2}+\kappa^{2}s_b^{2}s_a^{2}.
$$

*Proof.* The product is $\varepsilon e_t+c_bs_a\vec u_{\mathrm r}+is_bc_a\vec u_{\mathrm b}+is_bs_a\vec u_{\mathrm b}\times\vec u_{\mathrm r}$, so

$$
\vec Q\cdot\vec Q
=c_b^{2}s_a^{2}-s_b^{2}c_a^{2}-s_b^{2}s_a^{2}\lvert\vec u_{\mathrm b}\times\vec u_{\mathrm r}\rvert^{2}+2i\kappa\,c_bs_as_bc_a,
$$

with $\lvert\vec u_{\mathrm b}\times\vec u_{\mathrm r}\rvert^{2}=1-\kappa^{2}$. The first three terms are $c_b^{2}s_a^{2}-s_b^{2}+\kappa^{2}s_b^{2}s_a^{2}$, and replacing $s_a^{2}$ by $1-c_a^{2}$ in the first two gives $1-c_b^{2}c_a^{2}$. So the real part is $1-c_b^{2}c_a^{2}+\kappa^{2}s_b^{2}s_a^{2}$, which is $1-\lvert\varepsilon\rvert^{2}$ by the second display.

**Checked on six random configurations.** With $\vec u_{\mathrm b}=\vec e_x$ and the rotor axis at cosine $\kappa$, the computed $B^{2}$ matches the display to every printed digit at all six triples of $(\theta_{\mathrm{rpd}},\theta_{\mathrm{axr}},\kappa)$. Two of them: $0.004741+0.137403i$ at $(0.971,0.935,0.302)$ and $0.992595+0.005292i$ at $(0.217,3.322,-0.269)$.

**The display reads as a two-step criterion.** The real part sees only $\lvert\varepsilon\rvert$; the imaginary part sees the orientation of the frames and the two angles' sines. So the sector's condition factors into a condition on the modulus and a condition on the phase, and that factoring is what separates the two loci.

## The Theorem

**The sector is the locus $\varepsilon=\pm1$.**

*Theorem.* For a word with $r>0$, $\tilde\Xi$ lies on $\Sigma_{10}$ if and only if $\kappa=0$ and $c_b^{2}c_a^{2}=1$.

*Proof.* $B^{2}=0$ needs the real and imaginary parts of the proposition's display to vanish separately.

- The imaginary part is $2\kappa c_bc_as_bs_a$. Since $c_b>0$, it vanishes when $\kappa=0$, when $s_a=0$ (that is $\theta_{\mathrm{axr}}\in\{0,\pi\}$), or when $s_b=0$ (that is $\theta_{\mathrm{rpd}}=0$).
- With $\theta_{\mathrm{axr}}\in\{0,\pi\}$ the modulus is $\lvert\varepsilon\rvert=c_b\lvert c_a\rvert=c_b$, so the real part is $1-c_b^{2}=-s_b^{2}$, vanishing only at $\theta_{\mathrm{rpd}}=0$.
- With $\theta_{\mathrm{rpd}}=0$ the modulus is $\lvert c_a\rvert$, so the real part is $1-c_a^{2}=s_a^{2}$, vanishing only at $\theta_{\mathrm{axr}}=0$.
- Those two cases meet at $\theta_{\mathrm{rpd}}=0$, $\theta_{\mathrm{axr}}=0$, which is the scalar line and belongs to the first case with $c_bc_a=1$.

So off the scalar line the imaginary part forces $\kappa=0$, and then the real part is $1-c_b^{2}c_a^{2}$ and the identity follows. Conversely, $\kappa=0$ with $c_b^{2}c_a^{2}=1$ makes both parts vanish.

**The theorem's two halves are one statement about $\varepsilon$.** With $\kappa=0$ the number is real and equals $c_bc_a$, so the condition is exactly $\varepsilon=\pm1$; and $\varepsilon=\pm1$ forces $\kappa=0$ by the imaginary part. Hence

$$
\Sigma_{10}=\{\tilde\Xi:N\neq0,\ \varepsilon=\pm1\},
$$

and the sector's name and the sign's two values are the same object.

**The scalar line is where the statement needs care and it is not an exception.** At $\theta_{\mathrm{rpd}}=0$ and $\theta_{\mathrm{axr}}=0$ the element is central, the two axes are free, and $\varepsilon=1$ for every choice of them. So the locus $\varepsilon=1$ contains points with $\kappa\neq0$, all of them on the scalar line, and the theorem's hypothesis $N\neq0$ is satisfied there. The restriction to $\kappa=0$ in the display above is therefore a restriction *off* the scalar line, and the article says so rather than excluding the line.

## Why $\lvert\varepsilon\rvert=1$ Is Not the Sector

**The modulus's condition is one real equation and the sector needs two.** $\lvert\varepsilon\rvert=1$ is one equation; the sector is two. The difference is visible in the proposition: $\lvert\varepsilon\rvert=1$ kills the real part of $B^{2}$ and leaves the imaginary part, so the level set is the locus where the vector part's square is purely imaginary.

**The counterexample, with numbers.** At $\theta_{\mathrm{rpd}}=2$, $\kappa=\tfrac12$ and $\theta_{\mathrm{axr}}=1.935631$, the display gives

$$
\lvert\varepsilon\rvert=1.000000,
\qquad
\frac{B^{2}}{\Rho^{2}}=0.468467+0.847037i,
$$

so the element is on the level set and off the sector by the whole imaginary part. The check is the article's, recomputed from the word, and it agrees with the polar article's $0.468+0.847i$ to the digits printed there.

**The dimension count says the same thing.** The level set has seven real dimensions, since it is one equation on the eight parameters; the sector has six. So the level set contains the sector as a codimension-one subset, and the subset is where the sign's phase is a multiple of $\pi$.

**The reading of the extra dimension is a phase.** On the level set $\lvert\varepsilon\rvert=1$ the number is a point of the unit circle; the sector is the two points $\pm1$. So the extra dimension is the circle's own, and the sector is the circle's intersection with the real axis.

**This is the correction that a naive reading of the polar form invites.** A reader who sees "$\varepsilon=\pm1$" and remembers "$\lvert\varepsilon\rvert=1$" will conflate them. The polar article states the distinction, the earlier literature on the corpus's own summary did not, and this article's theorem makes the distinction exact: the real values $\pm1$ are the sector, the unit modulus is only the sector's containing surface.

## The Rigidity Constraint

### What the Constraint Is

**The constraint is the identity, and its content is that the rapidity is not free.** On the sector

$$
\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}=\varepsilon,
\qquad \varepsilon=\pm1,
$$

so for every rotor angle there are at most two rapidities and for every rapidity at most two rotor angles. The word's two angles become one.

**The constraint is a definition of the sector and not a consequence of an equation.** It is equivalent to $B^{2}=0$ with $N\neq0$, which is the sector's definition. So a sentence that derives the locking from the field equation would be wrong: the locking is what it means for the element to be spectrally degenerate.

### What It Leaves Free

**Six parameters survive of eight, and four of them matter for the motion.** The scale and the phase are untouched. The boost axis is free. The rotor axis is free up to orthogonality to the boost axis, so two of its components survive. The rotor angle is free and the rapidity is its function.

**The count is the sector's dimension and the constraint's cost.** Two conditions removed and no more, so the locking is exactly the rigidity the sector can afford and not more.

### The Two Branches

**The identity has two branches, $c_a>0$ and $c_a<0$, and they cover the two halves of the rotor angle's range.** The corpus's range is $\theta_{\mathrm{axr}}\in[0,2\pi]$, so the branch with $c_a>0$ is $[0,\pi)$ and the branch with $c_a<0$ is $(\pi,2\pi]$; both reach the same rapidity, and the sign of $\varepsilon$ is the branch's label.

**The sheets are not related by any symmetry of the algebra that the article can exhibit.** They are two solutions of the same identity with opposite signs, and the section on what $\varepsilon$ is not returns to this.

### At the Antipodes

**At $\theta_{\mathrm{axr}}=\pi$ the identity has no solution and the sector's chart degenerates.** The cosine of the half angle vanishes while the hyperbolic cosine is at least one, so no rapidity satisfies the identity. The approach is a divergence: at that rotor angle the vector part's square is $1-c_b^{2}c_a^{2}=1$ at every rapidity, so the element moves further from the sector as the rapidity grows without bound.

**The antipode is where $\varepsilon$ vanishes and the sector ends.** The zero of $\varepsilon$ and the failure of the lock are the same locus seen from the two sides: the lock's equation has $\varepsilon$ on its right and a vanishing right-hand side is no lock at all.

## The Defective Unit

**The sector is the defective unit, and the rigidity constraint is the defect's cost.** On $\Sigma_{10}$ the two eigenvalues of left multiplication coincide while the element remains invertible, so the operator has no basis of eigenvectors: the action of $\vec Q$ has square $-B^{2}\mathrm{id}=0$, so it is a nilpotent shift and not a complex structure, and the one-parameter group is a scalar rate times a unipotent translation.

**The three readings of the defect are one reading.** No mode basis means no splitting into two propagation directions; a double eigenvalue of nonzero value means a reversible unit; a nilpotent vector part means the rate is all there is. The rigidity constraint is the statement that in the word the defect shows up as a tie between the two frame angles rather than as a degeneracy of an eigenvalue.

**What the scalar line is in this language.** At $\theta_{\mathrm{rpd}}=0$ and $\theta_{\mathrm{axr}}=0$ the element is central: a pure rate with no frame at all. It is the sector's one point where the word's two frames both collapse, and the sector encloses it as the point where the two branches of the identity meet.

**What the sector is not.** It is not a set of small elements, not a neighbourhood of the centre, and not a surface of constant density. It is a six-dimensional locus of units, and the constraint is its equation.

## What $\varepsilon$ Is Not

**It is not the sign of the energy.** In the standard spinor treatment the sign of the frequency is the sign of the eigenvalue of the Hamiltonian, and it is a property of a mode. Here the element is one object with no mode decomposition at a point; the sign's two values are the sector's two sheets, and they are not a particle–antiparticle label.

**It is not a conserved quantity.** It is a function of the word's parameters at an event, and the flow does not preserve the parameters: the rapidity and the rotor angle evolve, so $\varepsilon$ evolves. Only on the sector is it pinned to $\pm1$, and only because the sector itself is a locus.

**It is not a sign, as the zeros show.** A quantity that vanishes at $\theta_{\mathrm{axr}}=\pi$ with orthogonal axes has no two-valued range. The name is inherited and the article keeps it for the corpus's consistency while stating that the object is a complex coordinate.

**What it is.** The scalar part of the element relative to the modulus of its norm: the one number in the word that mixes the two frames, and therefore the one that detects a degeneracy of the spectrum.

## What Is Established and What Is Interpretation

**Established.** That $\varepsilon$ is the scalar part over the modulus and is a function of four parameters, displayed as two cosines and a dot product. That it is complex off the orthogonal locus, real on it, and zero at $\theta_{\mathrm{axr}}=\pi$ with $\kappa=0$, checked at three rapidities. That $B^{2}/\Rho^{2}=1-\lvert\varepsilon\rvert^{2}+2i\kappa c_bc_as_bs_a$, checked at six random configurations. That the sector is exactly the locus $\varepsilon=\pm1$, proved from that display. That $\lvert\varepsilon\rvert=1$ is a seven-dimensional level set containing the six-dimensional sector, with the numerical counterexample $0.468467+0.847037i$. That the rigidity constraint is the sector's defining identity and has two branches.

**Interpretation.** That the defect shows up as a tie between the frame angles. That the two sheets are not related by a symmetry. That $\varepsilon$'s inheritance from the spinor literature is a name and not a content. Each is argued here and none is proved.

**Not claimed.** It is not claimed that the sector is realised by a solution of the Dirac equation. It is not claimed that the two branches are physically distinct. It is not claimed that $\varepsilon$ is the only invariant that detects the degeneracy; it is the one the word supplies.

## Summary

The sign $\varepsilon$ is the element's scalar part divided by the modulus of its norm, a complex coordinate of the word and not a label. It is real on the orthogonal locus, complex off it, and it vanishes at a rotor angle of a half turn with orthogonal axes.

The square of the vector part obeys $B^{2}/\Rho^{2}=1-\lvert\varepsilon\rvert^{2}+2i\kappa c_bc_as_bs_a$, so the modulus of the sign controls the real part and the frames' orientation controls the imaginary part.

The sector $\Sigma_{10}$ is exactly the locus $\varepsilon=\pm1$, equivalently the orthogonal locus with $\cosh(\theta_{\mathrm{rpd}}/2)\cos(\theta_{\mathrm{axr}}/2)=\pm1$. The surface $\lvert\varepsilon\rvert=1$ is strictly larger: it is seven-dimensional against the sector's six, and on it the sign's phase is free while the sector is where that phase is a multiple of $\pi$.

The rigidity constraint is therefore the sector's definition and not a consequence of an equation: the sector is the defective unit, and the tie between the rapidity and the rotor angle is what the defect looks like in the word.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varepsilon=\Xi_t/\Rho$ | Sign: scalar part over the modulus of the norm |
| $\kappa=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | Cosine between the boost and rotor axes |
| $c_b,s_b$ | Half-angle hyperbolic cosine and sine of the rapidity |
| $c_a,s_a$ | Half-angle cosine and sine of the rotor angle |
| $B^{2}=\vec Q\cdot\vec Q$ | Square of the vector part |
| $\Rho=r\,e^{i\theta_{\mathrm{pha}}}$ | Modulus of the norm, $\Rho^{2}=N$ |
| $\Sigma_{10}$ | $N\neq0$, $B^{2}=0$: the defective unit |
| $\lvert\varepsilon\rvert=1$ | Seven-dimensional level set containing the sector |

## Further Reading

- Paul A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the sign of the frequency in the spinor treatment that the name inherits.
- David Hestenes, "Space–time structure of the Dirac theory," in *Clifford Algebras and their Applications in Mathematical Physics* (Reidel, 1986), for the spinor as a rotor and the role of the scalar part.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, vol. 1 (Cambridge University Press, 1984), for the two-component spinor and its flag, whose degeneracies are the sector's kin.
- The companion articles: [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), [Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra](physical-interpretation-of-spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), [Spin-Velocity Locking on the Degenerate Sector](spin-velocity-locking-on-the-degenerate-sector.html), [The Non-Uniqueness of the Spin Fluid](the-non-uniqueness-of-the-spin-fluid.html), [The Current Algebra](the-current-algebra.html).
