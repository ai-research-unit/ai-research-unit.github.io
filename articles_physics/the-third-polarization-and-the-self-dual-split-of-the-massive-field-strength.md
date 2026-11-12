# __The Third Polarization and the Self-Dual Split of the Massive Field Strength__

## Introduction

The self-dual and anti-self-dual split is the framework's home for integer spin. On a real field strength the Hodge dual acts as $-\,$left multiplication by the central imaginary, its projectors decompose the complexified vector part into two three-dimensional complex spaces, and the two halves are the two representations $(1,0)$ and $(0,1)$ of the Lorentz group — two pure spin-one multiplets with no scalar admixture. For the massless field the halves are the two helicities: $\vec E+ic\vec B$ carries helicity $+1$, $\vec E-ic\vec B$ carries helicity $-1$, and the longitudinal direction belongs to the propagation vector, where the gauge freedom removes it.

The companion article on the split closes with the promise of the massive case: there the gauge freedom is absent, the longitudinal polarization becomes physical, and the third state has to be counted as a genuine degree of freedom. This article keeps the promise. It asks two questions and answers both. **What is the third state, in the split's terms?** And: **what does the split see of it?**

**The answers, in one paragraph each.**

*The three states are the three helicities of one triplet, and the split's two halves are its helicity $\pm1$ directions only.* At a fixed wavevector the massive field has three amplitude directions: two transverse, which are the two circular polarizations and are helicity eigenstates, and one longitudinal, which is along the propagation vector and has helicity zero. The split diagonalizes helicity on the transverse plane, so it resolves the two circular states exactly and sees nothing of the third: both of its halves are transverse, and the longitudinal state is the axis they are transverse to.

*The split's purity is a massless property, and the mass is its measure.* For a massive mode the two chiral coordinates do not separate. Computing $\vec N=\vec E+ic\vec B$ and $\vec N^*=\vec E-ic\vec B$ from the massive dispersion relation gives

$$
\vec N=(1+ck/\omega)\,\vec E ,\qquad
\vec N^*=(1-ck/\omega)\,\vec E ,
$$

for the helicity state carried by $\vec E$, and the same two numbers with the roles exchanged for the opposite helicity. Both coordinates are nonzero for every massive mode, and their ratio is real. The vanishing of one of them, which is what "the field is self-dual" means, happens exactly at $ck=\omega$, that is, exactly at $k_m=0$. So the mass is the quantitative measure of the failure of duality purity, and a real massive field is never pure.

**What this article does not claim.** It does not claim that the split fails, or that the massive field needs a different carrier. The split is a decomposition of the complexified field strength, it is exact for every field, and it is the correct home of the integer-spin representations. What the article claims is narrower and sharper: the split resolves the two circular polarizations and does not resolve the third, so the three states are **not** a $2+1$ split of the two chiral halves. The third state lives in the direction the split leaves out, and any programme that treats self-duality as a condition on a massive field is imposing the vanishing of a combination that is not there.

The conventions are those of the two companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_t=1$, $\vec e_\eta^2=-e_t$ and central scalar imaginary $i$; the field strength is $\tilde F=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H\in\mathbb{B}_V$ with $\vec B=\mu\vec H$ and $c=1/\sqrt{\epsilon\mu}$; the Riemann–Silberstein vector is $\vec N=\vec E+ic\vec B$; the Hodge dual is $\star(\vec E,\vec B)=(c\vec B,-\vec E/c)$ with $\star^2=-1$ and $\star\tilde F=-i\tilde F$; the projectors are $\tilde\Pi_{sd,asd}=\tfrac12(1\pm i\star)$; and the mass is $k_m=mc/\hbar$ with the dispersion relation $\omega^2=c^2\vec k^2+c^2k_m^2$. Where the wavevector's magnitude is written $k$, it means $\lvert\vec k\rvert$.

## The Three States at a Wavevector

**The amplitude space.** A plane-wave solution of the Proca equation is determined by the amplitude of the potential, and the Lorenz condition relates its scalar and vector parts:

$$
\tilde A_\Phi=\Bigl(i\,a'_t\,e_t+\vec A_0\Bigr)\cos\theta_{\mathrm{pwp}},
\qquad
\theta_{\mathrm{pwp}}=k'_t r'_t-\vec k\cdot\vec r,
\qquad
a'_t=\frac{\vec k\cdot\vec A_0}{k'_t},
$$

with the dispersion relation $k'^2_t=\vec k^2+k_m^2$. The vector amplitude $\vec A_0$ has three real components, and the scalar amplitude is determined by them. So the solution space at a fixed wavevector is three-dimensional, and the three directions are the three polarizations. In frequency units, $\omega=ck'_t$ and the dispersion relation is $\omega^2=c^2k^2+c^2k_m^2$.

**The two transverse states and the longitudinal one.** Choose the circular basis of the plane transverse to $\hat k$,

$$
\varepsilon_{\mathrm{fop},\pm}=\frac{\hat e_1\pm i\hat e_2}{\sqrt2},
\qquad
\hat k\times\varepsilon_{\mathrm{fop},\pm}=\mp i\,\varepsilon_{\mathrm{fop},\pm},
$$

with $\hat e_1,\hat e_2$ orthonormal and both orthogonal to $\hat k$. These two are the helicity eigenstates: a rotation about $\hat k$ by an angle multiplies them by $e^{\mp i\varphi}$. The third direction is $\hat k$ itself, and it is the longitudinal state, with helicity zero. In the circular basis every vector amplitude decomposes as

$$
\vec A_0=A_+\,\varepsilon_{\mathrm{fop},+}+A_-\,\varepsilon_{\mathrm{fop},-}+A_L\,\hat k ,
$$

and all three coefficients are free: this is the whole difference from the massless case, where the Lorenz condition degenerates into the statement $\vec k\cdot\vec A_0=0$ and removes $A_L$.

**The fields of the three states.** With $\vec E=-\nabla a'_t-\partial_{r'_t}\vec A$ and $\vec B=\nabla\times\vec A$, and with the Lorenz condition imposed, the transverse amplitudes give

$$
\vec E=\omega A_\pm\,\varepsilon_{\mathrm{fop},\pm}\sin\theta_{\mathrm{pwp}},
\qquad
c\vec B=\mp\,i\,ck A_\pm\,\varepsilon_{\mathrm{fop},\pm}\sin\theta_{\mathrm{pwp}},
$$

so that $\vec B=-i\sigma(k/\omega)\vec E$ with $\sigma=\pm1$ the helicity, and the longitudinal amplitude gives

$$
\vec E=\frac{k_m^2}{\omega}\,A_L\,\hat k\,\sin\theta_{\mathrm{pwp}},
\qquad
\vec B=0 .
$$

The longitudinal state is a purely electric field in the wave frame, directed along the propagation vector, and the factor $k_m^2/\omega$ is what remains of $\omega-k^2/\omega$: the longitudinal field is small at high frequency and vanishes as the mass goes to zero. That vanishing is the massless limit's removal of the state, seen at the level of the field rather than the potential.

**Three invariants, one table.** The two invariants of the field are $I_1=\vec E^2-c^2\vec B^2$ and $I_2=\vec E\cdot\vec B$, and for the three states they take the values

| state | $\vec E$ | $c\vec B$ | $I_1$ | $I_2$ |
| --- | --- | --- | --- | --- |
| $\varepsilon_{\mathrm{fop},+}$ | $\omega A_+\varepsilon_+\sin\theta$ | $-i\,ckA_+\varepsilon_+\sin\theta$ | $c^2k_m^2A_+^2\sin^2\theta$ | $0$ |
| $\varepsilon_{\mathrm{fop},-}$ | $\omega A_-\varepsilon_-\sin\theta$ | $+i\,ckA_-\varepsilon_-\sin\theta$ | $c^2k_m^2A_-^2\sin^2\theta$ | $0$ |
| $\hat k$ | $A_Lk_m^2\hat k\sin\theta/\omega$ | $0$ | $A_L^2k_m^4\sin^2\theta/\omega^2$ | $0$ |

so that $I_1>0$ for every state and $I_2=0$ for every state. A Proca plane wave is therefore never null: $I_1$ vanishes only at $k_m=0$, and then only for the transverse states, whose amplitude is not required to vanish while the longitudinal one is. The field is of the electric type in the invariant classification, whatever its polarization.

## The Two Chiral Coordinates of a Massive Mode

**The computation.** The Riemann–Silberstein vector of a mode is $\vec N=\vec E+ic\vec B$, and its coefficient conjugate is $\vec N^*=\vec E-ic\vec B$. Write $\sigma=\pm1$ for the helicity, so that $\vec E$ is along $\varepsilon_{\mathrm{fop},\sigma}$ and $\vec B=-i\sigma(k/\omega)\vec E$, which is the Faraday relation with the circular-basis sign. Then

$$
ic\vec B=i\,(-i\sigma)\,c\frac{k}{\omega}\vec E=\sigma\frac{ck}{\omega}\vec E ,
$$

so that

$$
\boxed{\;\vec N=\Bigl(1+\sigma\frac{ck}{\omega}\Bigr)\vec E,\qquad
\vec N^*=\Bigl(1-\sigma\frac{ck}{\omega}\Bigr)\vec E\;}
$$

with the upper sign for $\sigma=+1$, where the two weights are $1+ck/\omega$ and $1-ck/\omega$. For the longitudinal state $\vec B=0$ and

$$
\vec N=\vec N^*=\vec E=\frac{k_m^2}{\omega}A_L\hat k\sin\theta_{\mathrm{pwp}} .
$$

**Three statements follow, and they are the article's technical content.**

*First, both coordinates are nonzero for every massive mode.* The two weights are $1-ck/\omega$ and $1+ck/\omega$, and $ck/\omega=k/\sqrt{k^2+k_m^2}<1$ for every $k_m>0$. Neither weight vanishes, so neither chiral coordinate of the field vanishes, so the massive mode is never self-dual and never anti-self-dual. The "impurity" is not an approximation: it is exact, and its size is the mass.

*Second, the two coordinates are parallel.* The weights are real, so $\vec N$ and $\vec N^*$ are both multiples of the same vector $\vec E$. Equivalently, $\vec N\cdot\vec N=I_1+2icI_2=I_1$ is real, so $\vec N$ has a definite phase and $\vec N^*$ is its conjugate with the same direction. The two chiral halves of a Proca plane wave are not independent complex vectors but one real direction with two real weights. That is the plane-wave form of $I_2=0$.

*Third, the mass measures the distance from purity.* Write the ratio of the two weights,

$$
\rho=\frac{1-ck/\omega}{1+ck/\omega}
=\frac{\omega-ck}{\omega+ck}
=\frac{c^2k_m^2}{(\omega+ck)^2},
$$

using $\omega^2-c^2k^2=c^2k_m^2$ in the last form. The ratio is positive and less than one, tends to zero as $k_m\to0$ at fixed $k$, and tends to one as $k\to0$ at fixed $k_m$. In the massless limit the smaller weight vanishes and the mode becomes pure: for $\sigma=+1$ the coordinate $\vec N^*$ goes to zero and the field is self-dual; for $\sigma=-1$ the coordinate $\vec N$ goes to zero and the field is anti-self-dual. That is exactly the companion article's statement, recovered as the endpoint of a one-parameter family. The parameter is the mass.

**The same three statements in the algebra's letters.** The two chiral coordinates are the two projections: on the complexified field strength the dual acts by $-i$ on $\vec N$ and by $+i$ on $\vec N^*$, which is what $\star\tilde F=-i\tilde F$ says on the self-dual side and $\tilde\Pi_{sd,asd}=\tfrac12(1\pm i\star)$ makes explicit. For a real mode the two coordinates are not independent: they are $\vec N^*=\lambda\vec N$ with the real $\lambda$, the reciprocal of the ratio above for the opposite helicity. So the mode's pair of coordinates is $(1,\lambda)$, and the statement "the mode is self-dual" is $\lambda=0$ while "it is anti-self-dual" is $\lambda=\infty$. Neither holds at any finite mass, and both are limits as $k_m\to0$. The massive mode is a definite mixture, with the mixing angle fixed by the mass and the wavevector and by nothing else — not by the amplitude, not by the polarization, since the two helicities carry reciprocal mixing ratios.

## The Third State in the Split

**The longitudinal state is the axis.** The two projectors are built from the Hodge dual, and the dual's eigenspaces at a given wavevector are spanned by the two circular directions $\varepsilon_{\mathrm{fop},\pm}$: those are the transverse vectors, and the two halves of the field strength are combinations of them. The longitudinal direction $\hat k$ is orthogonal to both. So in the split's own terms the three states are two plus an axis:

- the two circular states are the split's two halves, one each;
- the third state is the direction the two halves are transverse to, and neither projector has an image along it.

**The count is not $3=2+1$ in the split, and this is the point.** It is tempting to read the massive field's three states as two transverse plus one that the split should also carry. But the split decomposes the field strength, and the field strength of the longitudinal state is $\vec E\propto\hat k$ with $\vec B=0$: a field whose electric vector is along the propagation direction. Its two chiral coordinates coincide, $\vec N=\vec N^*$, so the split's two coordinates are equal rather than complementary, and the mode is fixed by neither. The correct statement is the one about helicity: the split diagonalizes the rotation about $\hat k$, the two circular states are its eigenstates with eigenvalues $\mp i$, and the third state is the rotation axis, whose eigenvalue is $+1$ — the direction left invariant by the rotation.

**What the split therefore classifies.** The split classifies the transverse polarization content of the field: it says which circular polarization a transverse mode carries, and it is the reason the two representations $(1,0)$ and $(0,1)$ are exactly the two helicities. It does not classify the longitudinal content, because the longitudinal content is not a two-form direction at all: it is the projection of the potential along $\hat k$, and its field strength is proportional to $k_m^2$. The split lives on $\mathbb{B}_V$, the field strength's carrier; the third state's origin is the scalar admixture of the potential, which lives on the four-vector carrier $\mathbb{B}_\Phi$.

**The two carriers, and why the count differs.** This is the structural reason the count of the massive states is not the count of the split's halves. The potential is a four-vector, and under rotations its representation is $1\oplus0$: three vector components and one scalar. The field strength is a two-form, and under rotations its representation is $1\oplus1$: two pure triplets. The mass is what makes the scalar admixture of the potential physical, and the third state is that admixture: it is the longitudinal member of the potential's triplet, and its field strength has the extra factor $k_m^2/\omega$ that betrays its origin. The split, acting on the two-form, has no place for it — not because the split is wrong, but because the third state is carried by the potential and not by the field strength.

## The Reality Obstruction, Quantified

The companion article states the obstruction in the massless case: a real field strength is never an eigenform of the dual, because $\vec E\pm ic\vec B=0$ separates into $\vec E=0$ and $\vec B=0$, six real equations on six real components whose only solution is zero. For the massive field the obstruction is stronger and it is quantitative.

**Stronger, because mass forbids nullness.** For the massless field a plane wave with $\vec E\perp\vec k$ and $\lvert\vec E\rvert=c\lvert\vec B\rvert$ is null, and nullness is the one place where a real field comes closest to purity; it is still not purity, but it is the boundary case. For the massive field even that is gone: $I_1=E^2k_m^2/\omega^2>0$ for every transverse mode, and $I_1=E^2>0$ for the longitudinal one. So a Proca plane wave is timelike in the invariant sense at every frequency, and the null set is empty for the plane-wave solutions. There is no boundary case to approach.

**Quantified, because the impurity has a size.** The ratio $\rho=(1-ck/\omega)/(1+ck/\omega)$ is the measure. It is $\rho=0$ exactly at $k_m=0$, it is $\rho=\tfrac13$ at $\omega=2ck$ (that is, $k_m^2=3k^2$), and it tends to one as $k\to0$. So the answer to "how self-dual is a massive mode" is: not at all, and the amount by which it fails is a function of the mass and the wavevector alone, independent of the amplitude and of the polarization (the two helicities have the reciprocal ratios $\rho$ and $1/\rho$, so the pair of values is fixed by the mass and the wavevector alone).

**What follows for any programme that imposes self-duality.** A condition $\tilde\Pi_{asd}\tilde F=0$ on a massive field is $\tfrac12(1-ck/\omega)\tilde F=0$, which for $k_m>0$ forces $\tilde F=0$: the condition has no non-trivial solution. So the massive field cannot be made self-dual by any choice of mode, and a scheme that requires it is requiring the field to vanish. The companion article's remark that such schemes take the field outside the material sector is the same statement from the other side: outside the material sector the field is complex and $\vec N=0$ is a condition on a complex object, not on a real one.

## The Rest Frame

**At $\vec k=0$ the split degenerates.** The rest frame has $\omega=ck_m$, so $ck/\omega=0$ and the two weights are both $1$: $\vec N=\vec N^*=\vec E$ for every state. The three states are then the three directions of $\vec A_0$, because $\vec k=0$ makes the distinction between transverse and longitudinal meaningless: there is no propagation direction to be transverse to. The rotation group acts on the three as a triplet, and that is the spin-one multiplet.

**Helicity is undefined in the rest frame.** Helicity is the projection of the spin on the momentum, and with $\vec k=0$ there is no axis to project on. So the two circular states and the longitudinal state are not distinguished by any rotation-invariant label in the rest frame: they are the three components of one irreducible multiplet, and the labels $+1,-1,0$ belong to a moving frame, where they are the eigenvalues of the rotation about $\hat k$.

**The boost is what makes the third state look different.** A boost along $\hat k$ from the rest frame carries the triplet into the triplet, and the state that was "the third component" becomes the longitudinal one; the two that were "the other two" become the circular ones. This is the little-group statement, and it is the reason the count of states is three in every frame while the *labels* change. What the split sees is the frame-dependent labelling, not the count: in the rest frame it sees nothing at all, because its weights are equal, and in the ultra-relativistic frame it sees the two transverse states almost purely and the longitudinal state not at all.

**A consistency check on the weights.** The weights $1\pm ck/\omega$ are functions of the boost's rapidity: with $\gamma=\omega/(ck_m)$ and $\gamma\beta=ck/(ck_m)$, $ck/\omega=\beta$, so the weights are $1\pm\beta$ and the ratio is $(1-\beta)/(1+\beta)=e^{-2\theta_{\mathrm{rpd}}}$ for the rapidity $\theta_{\mathrm{rpd}}$. The impurity of a mode under the split is therefore the Doppler factor of the frame in which the mode is moving, and it tends to zero for a mode moving at the speed of light — which a massive mode never does exactly.

## What This Says About the Programme

**The split is the helicity classification, and that is enough for the massless sector.** For the Maxwell field the two halves are the two helicities, the gauge freedom removes the third direction, and the split's two triplets are exactly the two physical states. Nothing in the companion article's treatment of the massless case needs revision.

**For the massive sector the split classifies two of the three states and it is blind to the third, and the blindness is structural.** The third state is the potential's scalar admixture made physical by the mass; the split acts on the field strength; and the field strength of the third state is proportional to $k_m^2$. So the third state is not a small correction to the split, it is a different carrier's content. The statement "spin one is pure" — the two-form carries no scalar — remains true and is exactly why the third state is invisible: the scalar is in the potential, and the two-form has projected it away.

**The consequence for the counting articles.** The corpus counts the Proca field's polarizations as three, the Maxwell field's as two, and it reads the count as the rank of the symbol of the gradient on the vector part. This article supplies the polarization-side reading of the same count: the three states are the three eigenvalues of the rotation about $\hat k$, the split resolves $\pm1$ and not $0$, and the mass is the parameter that makes the $0$ state physical without making it a two-form direction.

**What is not claimed.** The split is not deficient and does not need replacing. The massive field strength is still a pure vector of the algebra, it still carries the self-dual coordinate $\vec N$, and the projectors still act on it. What the article establishes is only that the sentence "the split separates the two helicities" does not extend to the third state, and that no amount of algebra will make it, because the third state is not there to be separated.

## Open Questions

1. **The off-shell splitting.** Everything here is on the plane-wave shell, where the Lorenz condition and the dispersion relation are both imposed. Off shell the two weights are not fixed by $\omega$ and $k$ alone, and the statement that the two chiral coordinates are parallel is a consequence of $I_2=0$, which is itself on shell. The off-shell decomposition, and whether the longitudinal direction can be defined without a wavevector, is open.
2. **The interacting case.** With a source, the Lorenz condition becomes the conservation of the current, and the longitudinal state is the one to which the equivalence theorem attaches. Whether the split's blindness to it has a counterpart in the high-energy behaviour of the longitudinal amplitude is a question for the electroweak articles, and it is not attempted here.
3. **The third state's own carrier.** The longitudinal state's field strength is a pure electric vector along $\hat k$. Whether it has a natural description as a section of a line bundle over the sphere of wavevectors — the helicity-zero direction — rather than as a limit of the two-form's coordinates, is not settled.

## Summary

A massive plane wave has three amplitude directions: two circular, with helicity $\pm1$, and one longitudinal, with helicity zero. The self-dual split resolves the two circular ones exactly — they are its two halves, the representations $(1,0)$ and $(0,1)$ — and it resolves nothing of the third, because both of its halves are transverse and the third is the axis they are transverse to. In the algebra the projectors act on a massive mode by rescaling rather than annihilating,

$$
\tilde\Pi_{sd,asd}\tilde F=\tfrac12\Bigl(1\pm\frac{ck}{\omega}\Bigr)\tilde F ,
$$

so the mode is in neither eigenspace, and the Riemann–Silberstein coordinates are $\vec N=(1+\sigma ck/\omega)\vec E$ and $\vec N^*=(1-\sigma ck/\omega)\vec E$: both nonzero, parallel, with a real ratio

$$
\rho=\frac{1-ck/\omega}{1+ck/\omega}=\frac{1-\beta}{1+\beta},
$$

which vanishes exactly at $k_m=0$ and equals one in the rest frame. The mass is therefore the measure of the failure of duality purity: a massive field is never self-dual, its plane waves are never null ($I_1=E^2k_m^2/\omega^2>0$, $I_2=0$), and a self-duality condition imposed on it forces it to vanish.

The origin of the count is the difference of carriers. The potential is a four-vector and restricts to $1\oplus0$; the field strength is a two-form and restricts to $1\oplus1$. The mass makes the potential's scalar admixture physical, and that admixture is the third state, whose field strength carries the factor $k_m^2/\omega$. The split, acting on the two-form, has projected the scalar away and cannot recover it. The companion article's "spin one is pure" and this article's "the third state is in the potential" are the two halves of one statement.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^2=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$, $\mathbb{B}_V$ | Material, informational, and vector sectors |
| $\tilde F=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ | Field-strength biquaternion, pure vector |
| $\vec B=\mu\vec H$, $c=1/\sqrt{\epsilon\mu}$ | Magnetic induction and speed of light in the medium |
| $\vec N=\vec E+ic\vec B$, $\vec N^*=\vec E-ic\vec B$ | Riemann–Silberstein coordinates of the two halves |
| $\star(\vec E,\vec B)=(c\vec B,-\vec E/c)$ | Hodge dual, $\star^2=-1$, $\star\tilde F=-i\tilde F$ |
| $\tilde\Pi_{sd,asd}=\tfrac12(1\pm i\star)$ | Projectors onto the self-dual and anti-self-dual halves |
| $\varepsilon_{\mathrm{fop},\pm}$ | Circular polarization vectors, $\hat k\times\varepsilon_\pm=\mp i\varepsilon_\pm$ |
| $A_+,A_-,A_L$ | Amplitudes of the two circular and the longitudinal states |
| $I_1=\vec E^2-c^2\vec B^2$, $I_2=\vec E\cdot\vec B$ | The two field invariants |
| $k_m=mc/\hbar$ | Mass wave number |
| $\omega^2=c^2k^2+c^2k_m^2$ | Dispersion relation; $k=\lvert\vec k\rvert$ |
| $\beta=ck/\omega$ | Frame speed of the mode; $\gamma=(1-\beta^2)^{-1/2}$ |
| $\rho=(1-\beta)/(1+\beta)$ | Ratio of the two chiral weights, the impurity measure |

## Further Reading

- [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html), for the split, the projectors and the massless helicities whose massive continuation this article gives.
- [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), for the dispersion relation, the Lorenz condition and the three polarizations.
- [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), for the polar reading of a plane wave, where the frame is constant and the scale carries the oscillation.
- [The Variational Principle and the Proca Equation in Biquaternionic Form](the-variational-principle-and-the-proca-equation-in-biquaternionic-form.html), for the stress tensor whose trace is the same measure of the mass.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html), for $\vec N$, the dual, and the two invariants.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html), for the massless case and the gauge freedom that removes the third state.
- [The Complex Potential of a Self-Dual Maxwell Field](the-complex-potential-of-a-self-dual-maxwell-field.html), for the programmes that impose duality purity and the change of carrier they require.
- [Canonical Quantization of the Biquaternion Proca Field](canonical-quantization-of-the-biquaternion-proca-field.html), for the polarization projector and the massless limit's change of constraint class.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* **46** (2013) 053001, for the complex-vector description and its duality structure.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time* (Cambridge, 1984), for the self-dual decomposition and the two three-dimensional complex representations.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the little group and the counting of the massive vector field's states.
- Alexandre Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs", *Journal de Physique et le Radium* **7** (1936) 347–353, for the third polarization and its mass dependence.
