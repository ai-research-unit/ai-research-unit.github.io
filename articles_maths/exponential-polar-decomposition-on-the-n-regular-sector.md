# __Exponential Polar Decomposition on the N-Regular Sector__

## Introduction

This article computes the exponential polar decomposition of a biquaternion of the **N-regular sector**, the set $N=\langle\tilde Q\rangle_{\natural}\neq0$. The word is the four-factor product

$$
\tilde Q=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\theta_{\mathrm{pha}}\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi]$, and two real unit axes. Every element of the sector has one, and it is unique up to the usual degeneracies of the axes. The article proves this from the Cartan decomposition, computes the closed forms, and reads the word against the spectral decomposition.

The existence of the word is a property of the group of invertibles alone. The second invariant, the vector form $B^2=Q_x^2+Q_y^2+Q_z^2$, decides only its shape. Off the wall $B^2\neq0$ the element has two distinct eigenvalues $\lambda_\pm=Q_t\pm iB$ and an eigenbasis, and the polar factors are diagonal in it exactly when the element is normal. On the wall the two eigenvalues coalesce, the eigenbasis disappears, and the unit factor is $\pm$unipotent: it is $\varepsilon(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$, its minimal polynomial is a square, and its two angles are locked by $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}=\varepsilon$. The word survives the passage to the wall, because it is a decomposition of the group and not of the element. The spectrum does not survive. That contrast is the spine of the article, and it is the reason the two cases are one theory and not two.

The article assumes *The Polar Decomposition of an N-Regular Biquaternion* for the modulus–unit theorem, *Biquaternion Elementary Functions* for the exponential and the logarithm, and *The Eigenbasis of a Spectrally Regular Biquaternion* for the eigenbasis. It does not treat the Peirce decomposition, the spinors or the spectral algebra of the sector. The numerical cases are in *Worked Examples of Exponential Polar Decomposition on the N-Regular Sector*.

**The plan.** The word, its two unit factors and the seven data are boxed and proved in §*The Result in Terms of the Coordinates*, which also gives the boxes in the coordinates of the wall. The domain is fixed in §*The Domain*, with the normal form that the wall imposes. The word and its component form are stated in §*The Decomposition*. The spectral reading occupies §*The Spectral Reading*, with the eigenbasis, the normal case and the non-normal case. §*The Unipotent Unit Factor* and §*The Two Strata* prove the rigidity on the wall: the scalar constraint, the orthogonal frame and the closed form. Existence and uniqueness are proved in §*Existence and Uniqueness*. The logarithm, the group law, the matrix picture, the exponential coordinates and the two walls follow. The summary collects the formulas of both cases in one table.

## The Result in Terms of the Coordinates

**Setting.** Let $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with complex coordinates, and put

$$
N=Q_t^2+Q_x^2+Q_y^2+Q_z^2,\qquad
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad
\lVert\tilde Q\rVert^2=|Q_t|^2+|Q_x|^2+|Q_y|^2+|Q_z|^2.
$$

On the sector $N\neq0$ and $B^2\neq0$. Here $\operatorname{Arg}$ is the principal argument in $(-\pi,\pi]$, $\lVert\cdot\rVert$ is the Euclidean norm of a real three-vector, $\operatorname{Im}$ acts componentwise, and $(j,k,l)$ is a cyclic permutation of $(x,y,z)$.

**Theorem (the word and its seven data).** Every $\tilde Q$ of the sector is

$$
\boxed{\;\tilde Q=r e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=r e^{i\theta_{\mathrm{pha}}}\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr)\;}
$$

with the two unit factors

$$
\boxed{\;\tilde U_{\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}\,e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b},\qquad
\tilde u_{\mathrm r}=\cos\frac{\theta_{\mathrm{axr}}}{2}\,e_t+\sin\frac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r}\;}
$$

and with the seven data determined by $Q_t,Q_x,Q_y,Q_z$. Write $\vec Q=(Q_x,Q_y,Q_z)$.

$$
\boxed{\;r=\sqrt{|N|},\qquad \Rho=r e^{i\theta_{\mathrm{pha}}}\;}
$$

$$
\boxed{\;\theta_{\mathrm{pha}}=\frac12\operatorname{Arg}N\;}
$$

$$
\boxed{\;\cosh\theta_{\mathrm{rpd}}=\frac{\lVert\tilde Q\rVert^2}{|N|},\qquad \theta_{\mathrm{rpd}}=\operatorname{arcosh}\frac{\lVert\tilde Q\rVert^2}{|N|}\;}
$$

$$
\boxed{\;C=\sqrt{\frac{\lVert\tilde Q\rVert^2+|N|}{2}},\qquad S=\sqrt{\frac{\lVert\tilde Q\rVert^2-|N|}{2}},\qquad \cosh\frac{\theta_{\mathrm{rpd}}}{2}=\frac{C}{\sqrt{|N|}},\qquad \sinh\frac{\theta_{\mathrm{rpd}}}{2}=\frac{S}{\sqrt{|N|}}\;}
$$

$$
\boxed{\;a_j=\frac{2}{|N|}\Bigl(\operatorname{Im}\bigl(\bar Q_tQ_j\bigr)-\operatorname{Im}\bigl(Q_k\bar Q_l\bigr)\Bigr),\qquad \vec a=(a_x,a_y,a_z),\qquad \vec u_{\mathrm b}=\frac{\vec a}{\lVert\vec a\rVert}\;}
$$

$$
\boxed{\;\tilde U_{\mathrm b}=\frac{C\,e_t+iS\,\vec u_{\mathrm b}}{\sqrt{|N|}}
=\frac{\sqrt{\lVert\tilde Q\rVert^2+|N|}\;e_t+i\sqrt{\lVert\tilde Q\rVert^2-|N|}\;\vec u_{\mathrm b}}{\sqrt{2|N|}}\;}
$$

$$
\boxed{\;\tilde u_{\mathrm r}=\frac{e^{-i\theta_{\mathrm{pha}}}}{|N|}\bigl(C-iS\,\vec u_{\mathrm b}\bigr)\tilde Q\;}
$$

$$
\boxed{\;\theta_{\mathrm{axr}}=2\arccos\frac{C\operatorname{Re}\bigl(e^{-i\theta_{\mathrm{pha}}}Q_t\bigr)-S\operatorname{Im}\bigl(e^{-i\theta_{\mathrm{pha}}}D\bigr)}{|N|},\qquad D=\vec u_{\mathrm b}\cdot\vec Q\;}
$$

$$
\boxed{\;\vec u_{\mathrm r}=\frac{e^{-i\theta_{\mathrm{pha}}}\bigl(C\vec Q-iS(Q_t\vec u_{\mathrm b}+\vec u_{\mathrm b}\times\vec Q)\bigr)}{\bigl\lVert C\vec Q-iS(Q_t\vec u_{\mathrm b}+\vec u_{\mathrm b}\times\vec Q)\bigr\rVert}\;}
$$

The boost axis is undefined when $\theta_{\mathrm{rpd}}=0$; the rotor axis is undefined when $\theta_{\mathrm{axr}}\in\{0,2\pi\}$. The vector $\mathrm{Vect}\tilde u_{\mathrm r}$ is the vector part of $\tilde u_{\mathrm r}$. At $\theta_{\mathrm{rpd}}=0$ the boost is $e_t$, and the box for $\tilde u_{\mathrm r}$ reduces to $\tilde u_{\mathrm r}=\tilde Q/\Rho$.

*Proof.*

**The modulus.** By the modulus–unit theorem, $\Rho$ is the principal square root of $N$. Write $\Rho=re^{i\theta_{\mathrm{pha}}}$ with $r>0$ and $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$. Then $r^2=|\Rho|^2=|N|$ and $2\theta_{\mathrm{pha}}\equiv\operatorname{Arg}N\pmod{2\pi}$. The range of $\theta_{\mathrm{pha}}$ selects the representative, so $r=\sqrt{|N|}$ and $\theta_{\mathrm{pha}}=\frac12\operatorname{Arg}N$.

**The product $\tilde Q\tilde Q^*$.** With $\tilde Q^*=\bar Q_t-\bar{\vec Q}$,

$$
\tilde Q\tilde Q^*
=(Q_t+\vec Q)(\bar Q_t-\bar{\vec Q})
=\bigl(|Q_t|^2+|\vec Q|^2\bigr)e_t+\bar Q_t\vec Q-Q_t\bar{\vec Q}-\vec Q\times\bar{\vec Q}.
$$

The scalar part is $\lVert\tilde Q\rVert^2=|Q_t|^2+|\vec Q|^2$. For pure quaternions $u,v$ one has $uv=-u\cdot v+u\times v$, with the bilinear dot product. Hence, componentwise,

$$
\bar Q_t\vec Q-Q_t\bar{\vec Q}=2i\operatorname{Im}\bigl(\bar Q_t\vec Q\bigr),
\qquad
\bigl(\vec Q\times\bar{\vec Q}\bigr)_j=2i\operatorname{Im}\bigl(Q_k\bar Q_l\bigr),
$$

and therefore

$$
\tilde Q\tilde Q^*=\lVert\tilde Q\rVert^2\,e_t+i|N|\vec a,
$$

with $\vec a$ the vector of the box.

**The boost.** The unit factor is $\tilde U=\tilde Q/\Rho$, so

$$
\tilde U\tilde U^*=\frac{\tilde Q\tilde Q^*}{|\Rho|^2}
=\frac{\lVert\tilde Q\rVert^2}{|N|}\,e_t+i\vec a.
$$

The word gives $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde u_{\mathrm r}$ $*$-unitary, hence

$$
\tilde U\tilde U^*=\tilde U_{\mathrm b}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^*\tilde U_{\mathrm b}^*=\tilde U_{\mathrm b}^2.
$$

With $\tilde U_{\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ and $\vec u_{\mathrm b}^2=-1$,

$$
\tilde U_{\mathrm b}^2=\cosh\theta_{\mathrm{rpd}}\,e_t+i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}.
$$

Comparing the scalar parts gives $\cosh\theta_{\mathrm{rpd}}=\lVert\tilde Q\rVert^2/|N|$ and $\theta_{\mathrm{rpd}}=\operatorname{arcosh}(\lVert\tilde Q\rVert^2/|N|)$; the argument is real because $\lVert\tilde Q\rVert^2\ge|N|$ by Cauchy–Schwarz. Comparing the vector parts gives $\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}=\vec a$, hence $\vec u_{\mathrm b}=\vec a/\lVert\vec a\rVert$ when $\theta_{\mathrm{rpd}}>0$. The box for $\tilde U_{\mathrm b}$ follows from $\cosh\frac{\theta_{\mathrm{rpd}}}{2}=\sqrt{(\lVert\tilde Q\rVert^2+|N|)/(2|N|)}$ and $\sinh\frac{\theta_{\mathrm{rpd}}}{2}=\sqrt{(\lVert\tilde Q\rVert^2-|N|)/(2|N|)}$.

**The rotor.** The boost is Hermitian of norm one, so $\tilde U_{\mathrm b}^{-1}=\tilde U_{\mathrm b}^{\natural}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}e_t-i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$. Therefore

$$
\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U
=\frac{1}{\Rho}\Bigl(\cosh\frac{\theta_{\mathrm{rpd}}}{2}e_t-i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)\tilde Q.
$$

Substituting the half-angle values, and using $\Rho=re^{i\theta_{\mathrm{pha}}}$ and $r^2=|N|$, gives the box for $\tilde u_{\mathrm r}$.

**The angles.** By the existence theorem, $\tilde u_{\mathrm r}$ is a unit real quaternion. Write $\tilde u_{\mathrm r}=\cos\frac{\theta_{\mathrm{axr}}}{2}e_t+\sin\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$ with $\theta_{\mathrm{axr}}\in[0,2\pi]$, so $\operatorname{Sc}\tilde u_{\mathrm r}=\cos\frac{\theta_{\mathrm{axr}}}{2}$ and $\mathrm{Vect}\tilde u_{\mathrm r}=\sin\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$ with $\sin\frac{\theta_{\mathrm{axr}}}{2}\ge0$. For a real unit vector $u$ and a complex vector $\tilde V$ with scalar part $\tilde V_t$, one has $u\tilde V=\tilde V_tu-u\cdot\tilde V+u\times\tilde V$. Applying this to the box for $\tilde u_{\mathrm r}$ gives, with $D=\vec u_{\mathrm b}\cdot\vec Q$,

$$
\operatorname{Sc}\tilde u_{\mathrm r}=\frac{e^{-i\theta_{\mathrm{pha}}}}{|N|}\bigl(CQ_t+iSD\bigr),
\qquad
\mathrm{Vect}\tilde u_{\mathrm r}=\frac{e^{-i\theta_{\mathrm{pha}}}}{|N|}\bigl(C\vec Q-iS(Q_t\vec u_{\mathrm b}+\vec u_{\mathrm b}\times\vec Q)\bigr).
$$

Taking the real part of the scalar part gives the box for $\theta_{\mathrm{axr}}$. Taking the norm of the vector part gives $\sin\frac{\theta_{\mathrm{axr}}}{2}=\lVert C\vec Q-iS(Q_t\vec u_{\mathrm b}+\vec u_{\mathrm b}\times\vec Q)\rVert/|N|$, and $\vec u_{\mathrm r}=\mathrm{Vect}\tilde u_{\mathrm r}/\sin\frac{\theta_{\mathrm{axr}}}{2}$ is the box for $\vec u_{\mathrm r}$.

**The assembly.** The boost box gives $\tilde U_{\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ and the rotor box gives $\tilde u_{\mathrm r}=\cos\frac{\theta_{\mathrm{axr}}}{2}e_t+\sin\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$; their product is $\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde U=\tilde Q/\Rho$, which is the word.

**Check.** For

$$
\tilde Q=\Bigl(1-\frac{i}{2}\Bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z,
$$

one has $N=1$ and $\lVert\tilde Q\rVert^2=3$, hence $r=1$, $\theta_{\mathrm{pha}}=0$, $\theta_{\mathrm{rpd}}=1.762747174$, $\vec a=2\sqrt2\,\vec e_x$ and $\vec u_{\mathrm b}=\vec e_x$. The boxes give

$$
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=\frac{1}{\sqrt2}e_t+\frac12(\vec e_x+\vec e_y),
\qquad
\theta_{\mathrm{axr}}=\frac{\pi}{2},
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}.
$$

### The Boxes at the Wall

The general boxes are stated for every invertible element. On the wall the normal form $\tilde Q=Q_t(e_t+\vec\Upsilon)$ evaluates them in closed shape, and the theorem below is that evaluation.

**Setting.** Use the normal form of §*The Domain*, $\tilde Q=Q_t(e_t+\vec\Upsilon)$, and write

$$
\vec\Upsilon=\vec A+i\vec B,\qquad \vec A,\vec B\in\mathbb R^3,\qquad a=\lVert\vec A\rVert.
$$

Since $\vec\Upsilon^2=0$, one has $\vec A\cdot\vec B=0$ and $\lVert\vec A\rVert=\lVert\vec B\rVert=a$. In terms of the coordinates, write $Q_t=q_t+iq'_t$ and $Q_j=q_j+iq'_j$ for $j=x,y,z$, with the eight coefficients real, and put $\vec q=(q_x,q_y,q_z)$ and $\vec q'=(q'_x,q'_y,q'_z)$. Then

$$
\vec A=\frac{q_t\,\vec q+q'_t\,\vec q'}{q_t^2+q_t'^2},\qquad
\vec B=\frac{q_t\,\vec q'-q'_t\,\vec q}{q_t^2+q_t'^2},
$$

since $Q_t^{-1}=(q_t-iq'_t)/(q_t^2+q_t'^2)$ and $\vec\Upsilon=\vec Q\,Q_t^{-1}$.

**Theorem (the word and its seven data).** On the Jordan part $a>0$, every $\tilde Q$ of the sector is

$$
\boxed{\;\tilde Q=Q_t(e_t+\vec\Upsilon)=r e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=r e^{i\theta_{\mathrm{pha}}}\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr)\;}
$$

with the two unit factors

$$
\boxed{\;\tilde U_{\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}\,e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b},\qquad
\tilde u_{\mathrm r}=\cos\frac{\theta_{\mathrm{axr}}}{2}\,e_t+\sin\frac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r}\;}
$$

and with the seven data determined by $Q_t,Q_x,Q_y,Q_z$. Here $\Rho$ is the principal square root of $Q_t^2$, that is, the root with non-negative real part and, on the imaginary axis, non-negative imaginary part.

$$
\boxed{\;r=|Q_t|,\qquad
\Rho=\begin{cases}Q_t,&\operatorname{Re}Q_t>0\ \text{or}\ \bigl(\operatorname{Re}Q_t=0,\ \operatorname{Im}Q_t>0\bigr),\\[2pt]-Q_t,&\text{otherwise},\end{cases}\qquad
\varepsilon=\frac{Q_t}{\Rho}=\pm1\;}
$$

$$
\boxed{\;\theta_{\mathrm{pha}}=\arg\Rho=\begin{cases}\arg Q_t,&\varepsilon=+1,\\[2pt]\arg(-Q_t),&\varepsilon=-1,\end{cases}\;}
$$

$$
\boxed{\;\theta_{\mathrm{rpd}}=2\operatorname{arsinh}a\;}
$$

$$
\boxed{\;\theta_{\mathrm{axr}}=\begin{cases}2\arctan a,&\varepsilon=+1,\\[2pt]2\pi-2\arctan a,&\varepsilon=-1.\end{cases}\;}
$$

$$
\boxed{\;\vec u_{\mathrm b}=\frac{\vec B+\vec A\times\vec B}{a\sqrt{1+a^2}},\qquad
\vec u_{\mathrm r}=\varepsilon\,\frac{\vec A}{a}\;}
$$

$$
\boxed{\;\tilde u_{\mathrm r}=\varepsilon\,\frac{e_t+\vec A}{\sqrt{1+a^2}},\qquad
\tilde U_{\mathrm b}=\sqrt{1+a^2}\,e_t+\frac{i}{\sqrt{1+a^2}}\bigl(\vec B+\vec A\times\vec B\bigr)\;}
$$

On the scalar line $a=0$ one has $\vec\Upsilon=0$, $\theta_{\mathrm{rpd}}=0$, and $\theta_{\mathrm{axr}}=0$ if $\varepsilon=+1$, $\theta_{\mathrm{axr}}=2\pi$ if $\varepsilon=-1$; both axes are arbitrary.

*Proof.*

**The modulus and the sign.** Since $N=Q_t^2$, the modulus satisfies $\Rho^2=Q_t^2$, hence $\Rho=\pm Q_t$. The principal branch selects the sign displayed, and $r=|\Rho|=|Q_t|$, $\varepsilon=Q_t/\Rho=\pm1$. Writing $\Rho=re^{i\theta_{\mathrm{pha}}}$ gives $\theta_{\mathrm{pha}}=\arg\Rho$, with the principal argument in $(-\pi,\pi]$; since $\Rho=\varepsilon Q_t$, this is the box for $\theta_{\mathrm{pha}}$.

**The structure of $\vec\Upsilon$.** With $\vec\Upsilon=\vec A+i\vec B$,

$$
\vec\Upsilon^2=\vec A^2-\vec B^2+2i\vec A\cdot\vec B
=\bigl(\lVert\vec B\rVert^2-\lVert\vec A\rVert^2\bigr)+2i\vec A\cdot\vec B,
$$

because $\vec A^2=-\lVert\vec A\rVert^2$ and $\vec B^2=-\lVert\vec B\rVert^2$ for real vectors. The vanishing of $\vec\Upsilon^2$ gives $\lVert\vec A\rVert=\lVert\vec B\rVert=a$ and $\vec A\cdot\vec B=0$.

**The product $\tilde U\tilde U^*$.** The unit factor is $\tilde U=\varepsilon(e_t+\vec\Upsilon)$ and its star conjugate is $\tilde U^*=\varepsilon(e_t-\bar{\vec\Upsilon})$. Hence

$$
\tilde U\tilde U^*=(e_t+\vec\Upsilon)(e_t-\bar{\vec\Upsilon})
=e_t+\vec\Upsilon-\bar{\vec\Upsilon}-\vec\Upsilon\bar{\vec\Upsilon}.
$$

Now $\vec\Upsilon-\bar{\vec\Upsilon}=2i\vec B$, and, using $\vec A\cdot\vec B=0$ and $\lVert\vec A\rVert=\lVert\vec B\rVert=a$,

$$
\vec\Upsilon\bar{\vec\Upsilon}
=(\vec A+i\vec B)(\vec A-i\vec B)
=-2a^2-2i\,\vec A\times\vec B.
$$

Therefore

$$
\tilde U\tilde U^*=(1+2a^2)e_t+2i\bigl(\vec B+\vec A\times\vec B\bigr).
$$

**The boost.** Since $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde u_{\mathrm r}$ $*$-unitary, $\tilde U\tilde U^*=\tilde U_{\mathrm b}^2$. With $\tilde U_{\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$,

$$
\tilde U_{\mathrm b}^2=\cosh\theta_{\mathrm{rpd}}\,e_t+i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}.
$$

Comparing the scalar parts gives $\cosh\theta_{\mathrm{rpd}}=1+2a^2=1+2\sinh^2\frac{\theta_{\mathrm{rpd}}}{2}$, so $\sinh\frac{\theta_{\mathrm{rpd}}}{2}=a$, $\cosh\frac{\theta_{\mathrm{rpd}}}{2}=\sqrt{1+a^2}$ and $\theta_{\mathrm{rpd}}=2\operatorname{arsinh}a$. Comparing the vector parts gives $\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}=2(\vec B+\vec A\times\vec B)$. Since $\vec A\cdot\vec B=0$,

$$
\lVert\vec B+\vec A\times\vec B\rVert^2=\lVert\vec B\rVert^2+\lVert\vec A\times\vec B\rVert^2=a^2+a^4=a^2(1+a^2),
$$

so $2\lVert\vec B+\vec A\times\vec B\rVert=2a\sqrt{1+a^2}=\sinh\theta_{\mathrm{rpd}}$. This gives the boxes for $\vec u_{\mathrm b}$ and $\tilde U_{\mathrm b}$.

**The rotor.** Put $c=\sqrt{1+a^2}$ and $w=\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}=(\vec B+\vec A\times\vec B)/c$, so that $\tilde U_{\mathrm b}=c\,e_t+iw$. The candidate

$$
\tilde u_{\mathrm r}=\varepsilon\,\frac{e_t+\vec A}{c}
$$

is a unit real quaternion, because $(e_t+\vec A)(e_t-\vec A)=e_t-\vec A^2=(1+a^2)e_t=c^2e_t$. Moreover, using $\vec B\vec A=-\vec A\times\vec B$ and $(\vec A\times\vec B)\vec A=a^2\vec B$,

$$
w(e_t+\vec A)=\frac{(\vec B+\vec A\times\vec B)(e_t+\vec A)}{c}=c\,\vec B,
$$

hence

$$
\tilde U_{\mathrm b}\tilde u_{\mathrm r}
=(c\,e_t+iw)\,\varepsilon\,\frac{e_t+\vec A}{c}
=\varepsilon\bigl(e_t+\vec A+i\vec B\bigr)
=\varepsilon(e_t+\vec\Upsilon)=\tilde U.
$$

By the uniqueness of the polar decomposition, this is the rotor, and the box for $\tilde u_{\mathrm r}$ follows.

**The angles.** From the box, $\operatorname{Sc}\tilde u_{\mathrm r}=\varepsilon/c$ and $\mathrm{Vect}\tilde u_{\mathrm r}=\varepsilon\vec A/c$. With $\theta_{\mathrm{axr}}\in[0,2\pi]$, $\cos\frac{\theta_{\mathrm{axr}}}{2}=\varepsilon/c$ and $\sin\frac{\theta_{\mathrm{axr}}}{2}=a/c\ge0$. For $\varepsilon=+1$ this gives $\frac{\theta_{\mathrm{axr}}}{2}=\arctan a$; for $\varepsilon=-1$ it gives $\frac{\theta_{\mathrm{axr}}}{2}=\pi-\arctan a$. Hence the box for $\theta_{\mathrm{axr}}$, and

$$
\vec u_{\mathrm r}=\frac{\mathrm{Vect}\tilde u_{\mathrm r}}{\sin\frac{\theta_{\mathrm{axr}}}{2}}
=\varepsilon\,\frac{\vec A}{a}.
$$

**The scalar line.** If $a=0$ then $\vec B=0$ and $\vec A=0$, so $\vec\Upsilon=0$ and $\tilde Q=Q_te_t$. Then $\theta_{\mathrm{rpd}}=0$, and the rotor is $\varepsilon e_t$, that is, $\theta_{\mathrm{axr}}=0$ for $\varepsilon=+1$ and $\theta_{\mathrm{axr}}=2\pi$ for $\varepsilon=-1$. Both axes are arbitrary.

**Check.** For

$$
\tilde Q=e_t+\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z,
$$

one has $\vec A=\vec e_y$, $\vec B=(\vec e_x+\vec e_z)/\sqrt2$, $a=1$, $Q_t=1$, $\varepsilon=1$. The boxes give

$$
\theta_{\mathrm{rpd}}=1.762747174,\qquad
\theta_{\mathrm{axr}}=\frac{\pi}{2},\qquad
\vec u_{\mathrm b}=\vec e_x,\qquad
\vec u_{\mathrm r}=\vec e_y,\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_y}{\sqrt2},\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x.
$$

## The Domain

### The Two Invariants

Let

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
\qquad
N=\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2,
\qquad
B^2=Q_x^2+Q_y^2+Q_z^2.
$$

The number $N$ is the reduced product $\tilde Q\tilde Q^{\natural}$, and $B^2$ is the quadratic form of the vector part. The two are complex numbers. The **spectrally regular sector** is

$$
\Sigma_{11}=\{\tilde Q\in\mathbb{B}:\ N\neq0,\ B^2\neq0\}.
$$

The name is the one of *The Spectrum*: the element is N-regular when $N\neq0$, and spectrally regular when $B^2\neq0$. The two conditions are independent, and their four combinations are the four sectors of the algebra. This article treats the two combinations with $N\neq0$: the compact notation below writes $11$ for the regular case and $10$ for the wall. The combinations with $N=0$ are the boundary, treated in §*The Two Walls*.

### Five Descriptions

The sector has five equivalent descriptions.

**Proposition (the descriptions of $\Sigma_{11}$).** For $\tilde Q\in\mathbb{B}$ the following are equivalent.

1. $N\neq0$ and $B^2\neq0$.
2. The two eigenvalues $\lambda_\pm=Q_t\pm iB$ are distinct and nonzero.
3. The minimal polynomial $X^2-2Q_tX+N$ is squarefree with nonzero constant term.
4. The element is invertible and its spectrum has two distinct points.
5. With $\Rho$ the principal square root of $N$ and $\tilde U=\tilde Q/\Rho$, the scalar part of $\tilde U$ is not $\pm1$.

*Proof.* The characteristic polynomial is $X^2-2Q_tX+N$. Its discriminant is $4(Q_t^2-N)=-4B^2$, so it is squarefree exactly when $B^2\neq0$, and its constant term is nonzero exactly when $N\neq0$. The eigenvalues are $Q_t\pm iB$, distinct and nonzero under the same two conditions. The element is invertible because $N\neq0$. A scalar has $B^2=0$, but $B^2=0$ also allows the non-scalar Jordan elements; the spectral condition is the distinctness, not the non-scalarity. For the last item, $\operatorname{Sc}\tilde U=Q_t/\Rho$, hence

$$
\bigl(\operatorname{Sc}\tilde U\bigr)^2=\frac{Q_t^2}{N},
\qquad
B^2=N-Q_t^2=N\Bigl(1-\bigl(\operatorname{Sc}\tilde U\bigr)^2\Bigr),
$$

so $B^2\neq0$ is equivalent to $\operatorname{Sc}\tilde U\notin\{1,-1\}$.

The last description separates the two nonzero-$N$ sectors: they are the two sides of the pair of hyperplanes $\operatorname{Sc}\tilde U=\pm1$ in the group of invertibles, and the wall is the union of the two hyperplanes.

### Geometry

The sector is the complement of the union $NB^2=0$ of the null cone and the spectral cone. It is open and dense in $\mathbb{B}$, of complex dimension $4$ and real dimension $8$. It is not a subgroup: $e_t$ has $B^2=0$ and lies outside, and the scalar line $\mathbb{C}^{\times}e_t$ lies entirely outside. It contains the pure vectors with $B^2\neq0$, such as $\vec e_x+\vec e_y$, for which $Q_t=0$ and the two eigenvalues are opposite. It also contains every Hermitian element with $B^2<0$ and $N\neq0$, such as $\sqrt2\,e_t+i\vec e_x$.

The sector is connected, and it is not simply connected; the loop $t\mapsto e_t+\varepsilon e^{2\pi it}\vec e_x$ winds around the spectral cone. The topology is not used below beyond the parameter count.

### The Normal Form at the Wall

**Proposition (the normal form).** Every $\tilde Q\in\Sigma_{10}$ has a unique writing

$$
\boxed{\tilde Q=Q_t\bigl(e_t+\vec\Upsilon\bigr)},
\qquad
\vec\Upsilon^2=0,
\qquad
Q_t\neq0,
$$

with $Q_t$ the scalar part and $\vec\Upsilon$ the vector part divided by $Q_t$.

*Proof.* Since $B^2=0$ the vector part is null, $\vec Q^2=-B^2=0$. Since $N=Q_t^2+B^2=Q_t^2$ and $N\neq0$, the scalar part is nonzero. Put $\vec\Upsilon=\vec Q/Q_t$; then $\vec\Upsilon^2=\vec Q^2/Q_t^2=0$, and $\tilde Q=Q_te_t+\vec Q=Q_t(e_t+\vec\Upsilon)$. The writing is unique because $Q_t$ is the scalar part.

The element is a scalar multiple of a unipotent element. The unipotent factor $e_t+\vec\Upsilon$ has norm one, because

$$
\langle e_t+\vec\Upsilon\rangle_{\natural}=1+\vec\Upsilon^2=1,
$$

and it is invertible, with inverse $e_t-\vec\Upsilon$.

### The Unit Factor at the Wall

The modulus is the principal square root of $N=Q_t^2$. Since $Q_t^2$ has the two square roots $\pm Q_t$, the modulus is $\Rho=\pm Q_t$, and the unit factor is

$$
\tilde U=\frac{\tilde Q}{\Rho}
=\frac{Q_t}{\Rho}\bigl(e_t+\vec\Upsilon\bigr)
=\varepsilon\bigl(e_t+\vec\Upsilon\bigr),
\qquad
\varepsilon=\frac{Q_t}{\Rho}=\pm1.
$$

The sign $\varepsilon$ is fixed by the branch of the modulus. It is $+1$ when $\Rho=Q_t$ and $-1$ when $\Rho=-Q_t$. The unit factor is therefore $\pm$unipotent, and the sign is the only trace of the scalar part that survives in it.

## The Decomposition

### The Word

**Definition.** An **exponential polar decomposition** of $\tilde Q$ is a writing

$$
\boxed{\;
\tilde Q=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=r\,e^{i\theta_{\mathrm{pha}}}\,
\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)
\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),\quad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr)
\;}
$$

with

$$
r>0,\qquad
\theta_{\mathrm{pha}}\in\Bigl(-\frac{\pi}{2},\frac{\pi}{2}\Bigr],\qquad
\theta_{\mathrm{rpd}}\ge0,\qquad
\theta_{\mathrm{axr}}\in[0,2\pi],
$$

and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ real unit vectors, called the **boost axis** and the **rotor axis**. The four factors are the **scale** $r$, the **phase** $e^{i\theta_{\mathrm{pha}}}$, the **boost** $\tilde U_{\mathrm b}$ and the **rotor** $\tilde u_{\mathrm r}$, both written in the box.

The scalars are central; the two exponentials are not. The order of the factors is part of the definition: the boost stands to the left of the rotor. The reverse order is another word, and the two are related by the Cartan involution, not by a commutation.

### The Four Factors

The factors have closed forms in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$.

| Factor | Exponent | Closed form | Range |
|---|---|---|---|
| scale | $\ln r$ | $r$ | $r>0$ |
| phase | $i\theta_{\mathrm{pha}}$ | $e^{i\theta_{\mathrm{pha}}}$ | $\theta_{\mathrm{pha}}\in(-\frac{\pi}{2},\frac{\pi}{2}]$ |
| boost | $i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ | $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\,e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b}$ | $\theta_{\mathrm{rpd}}\ge0$ |
| rotor | $\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$ | $\cos\frac{\theta_{\mathrm{axr}}}{2}\,e_t+\sin\frac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r}$ | $\theta_{\mathrm{axr}}\in[0,2\pi]$ |

The boost is Hermitian positive of norm one; the rotor is a unit real quaternion. The product $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ is the unit factor of $\tilde Q$, and

$$
\tilde Q=\Rho\,\tilde U,
\qquad
\Rho=r e^{i\theta_{\mathrm{pha}}}.
$$

The modulus $\Rho$ is the principal square root of $N$, in the branch with non-negative real part and, on the negative real axis, non-negative imaginary part. The scale and the phase are the polar coordinates of $\Rho$. The unit factor is recovered as $\tilde U=\tilde Q/\Rho$ and has norm one.

### The Component Form

Let

$$
c_{\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2},
\qquad
s_{\mathrm b}=\sinh\frac{\theta_{\mathrm{rpd}}}{2},
\qquad
c_{\mathrm r}=\cos\frac{\theta_{\mathrm{axr}}}{2},
\qquad
s_{\mathrm r}=\sin\frac{\theta_{\mathrm{axr}}}{2},
\qquad
c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}.
$$

Multiplying the two exponentials in the order of the word gives

$$
\boxed{\;
\tilde U=\bigl(c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}c\bigr)e_t
+i s_{\mathrm b}c_{\mathrm r}\,\vec u_{\mathrm b}
+c_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm r}
+i s_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}
\;}
$$

The four terms are the scalar term, corrected by the angle between the axes, the boost axis, the rotor axis and the cross term. The cross term is present exactly when both angles are nonzero and the axes are neither parallel nor antiparallel. It is the term that a sum of the two exponents cannot produce, because the sum contains only the two axes and their linear combinations.

The scalar part is

$$
\operatorname{Sc}\tilde U=c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}c,
$$

and the vector part is the remaining three terms. The norm of $\tilde U$ is one, so

$$
\bigl(\operatorname{Sc}\tilde U\bigr)^2+\vec U\cdot\vec U=1,
$$

and the eigenvalues of $\tilde U$ are

$$
\mu_\pm=\operatorname{Sc}\tilde U\pm i\sqrt{1-\bigl(\operatorname{Sc}\tilde U\bigr)^2}.
$$

### The Parameter Count

The data are

$$
\underbrace{1}_{\ln r}
+\underbrace{1}_{\theta_{\mathrm{pha}}}
+\underbrace{1+2}_{\theta_{\mathrm{rpd}},\vec u_{\mathrm b}}
+\underbrace{1+2}_{\theta_{\mathrm{axr}},\vec u_{\mathrm r}}
=8,
$$

the real dimension of the group of invertibles. The word is a coordinate system on that group, cut by the ranges of the two angles and of the phase. The two axes are points of $S^2$.


## The Spectral Reading

### The Eigenbasis

Let $\tilde Q\in\Sigma_{11}$, and fix a square root $B$ of $B^2$. Define

$$
\vec{Ζ}=-i\frac{\vec Q}{B},
\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec{Ζ}}{2},
\qquad
\lambda_\pm=Q_t\pm iB.
$$

**Proposition (the eigenbasis).** The element $\vec{Ζ}$ is a root of one,

$$
\vec{Ζ}^2=e_t,
$$

the two elements $\tilde\Pi_\pm$ are complementary idempotents,

$$
\tilde\Pi_\pm^2=\tilde\Pi_\pm,
\qquad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0,
\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
$$

and

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$

The eigenvalues are distinct and nonzero, and the idempotents are the spectral projections.

*Proof.* For a pure vector, $\vec Q^2=-\vec Q\cdot\vec Q=-B^2$. Hence

$$
\vec{Ζ}^2=\Bigl(-i\frac{\vec Q}{B}\Bigr)^2=(-i)^2\frac{\vec Q^2}{B^2}=(-1)\frac{-B^2}{B^2}=e_t.
$$

The idempotent identities follow from $\vec{Ζ}^2=e_t$ and the commutation of $\vec{Ζ}$ with itself. The spectral decomposition is checked by expanding the right-hand side:

$$
\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-
=\frac{\lambda_++\lambda_-}{2}e_t+\frac{\lambda_+-\lambda_-}{2}\vec{Ζ}
=Q_te_t+iB\vec{Ζ}
=Q_te_t+\vec Q.
$$


The two signs of $B$ exchange $\vec{Ζ}$ with $-\vec{Ζ}$, $\tilde\Pi_+$ with $\tilde\Pi_-$, and $\lambda_+$ with $\lambda_-$; the unordered pair is unchanged. The element is semisimple, its minimal polynomial is $X^2-2Q_tX+N$, and its centraliser is $\mathbb{C}[\tilde Q]\cong\mathbb{C}\oplus\mathbb{C}$.

### The Unit Factor on the Eigenlines

Since $\tilde U=\tilde Q/\Rho$ and $\Rho$ is central,

$$
\tilde U=\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-,
\qquad
\mu_\pm=\frac{\lambda_\pm}{\Rho}.
$$

The two eigenvalues of the unit factor satisfy

$$
\mu_+\mu_-=\frac{N}{\Rho^2}=1,
\qquad
\mu_++\mu_-=\frac{2Q_t}{\Rho}=2\operatorname{Sc}\tilde U,
\qquad
\mu_+\neq\mu_-.
$$

They are the roots of $X^2-2U_tX+1$, with $U_t=\operatorname{Sc}\tilde U$, hence

$$
\boxed{\mu_\pm=U_t\pm i\sqrt{1-U_t^2}}.
$$

The spectrum of $\tilde U$ therefore depends on $\tilde Q$ only through the single complex number $U_t=Q_t/\Rho$. The two eigenvalues are distinct because $B^2\neq0$, and their product is one.

The spectral data of the element and of the unit factor are related by

$$
\lambda_\pm=\Rho\mu_\pm,
\qquad
N=\Rho^2,
\qquad
Q_t=\Rho U_t,
\qquad
B^2=\Rho^2(1-U_t^2).
$$

The last identity is the spectral form of the defining condition: the sector $B^2\neq0$ is the locus $U_t^2\neq1$, and the spectral cone $B^2=0$ is the locus $U_t=\pm1$.

### The Normal Case

The eigenbasis is a polar basis when the element commutes with its Hermitian conjugate.

**Lemma.** For every $\tilde Q=Q_te_t+\vec Q$,

$$
[\tilde Q,\tilde Q^*]=-2\,\vec Q\times\overline{\vec Q}.
$$

*Proof.* The scalar parts are central and commute with everything. For pure vectors,

$$
\vec Q\,\overline{\vec Q}=-\vec Q\cdot\overline{\vec Q}+\vec Q\times\overline{\vec Q},
\qquad
\overline{\vec Q}\,\vec Q=-\vec Q\cdot\overline{\vec Q}-\vec Q\times\overline{\vec Q},
$$

so the commutator is $-2\vec Q\times\overline{\vec Q}$.

**Theorem (the normal dichotomy).** For $\tilde Q\in\Sigma_{11}$ with word as above, the following are equivalent.

1. $\tilde Q$ is normal, $[\tilde Q,\tilde Q^*]=0$.
2. $\vec Q\times\overline{\vec Q}=0$, that is, $\vec Q=\omega\vec u$ with $\omega\in\mathbb{C}$ and $\vec u$ a real unit vector.
3. The two polar factors $\tilde U_{\mathrm b}$ and $\tilde u_{\mathrm r}$ commute with $\tilde Q$.
4. The two axes are parallel or antiparallel, or one of the two angles vanishes.
5. The word is a single exponential.

In this case the common axis is $\pm i\vec{Ζ}$ whenever it is defined, and

$$
\boxed{\;
\tilde Q=r e^{i\theta_{\mathrm{pha}}}\exp\Bigl(\frac{\theta_{\mathrm{axr}}+i\theta_{\mathrm{rpd}}}{2}\vec u\Bigr),
\qquad
\vec u=\pm i\vec{Ζ},
\;}
$$

with the sign chosen so that $\theta_{\mathrm{rpd}}\ge0$. The eigenvalues of the unit factor are

$$
\boxed{\mu_\pm=e^{\mp\frac{\theta_{\mathrm{rpd}}}{2}}e^{\pm i\frac{\theta_{\mathrm{axr}}}{2}}},
$$

and the spectrum of $\tilde U$ determines the two angles,

$$
\theta_{\mathrm{rpd}}=\ln\Bigl\lvert\frac{\mu_-}{\mu_+}\Bigr\rvert,
\qquad
\theta_{\mathrm{axr}}=2\arg\mu_+\pmod{2\pi}.
$$

*Proof.* The equivalence of 1 and 2 is the lemma, with the rank-one condition on the complex vector $\vec Q$. If $\tilde Q$ is normal then $\tilde U$ is normal, because $\tilde U=\tilde Q/\Rho$ and $\Rho$ is central. The Hermitian factor $\tilde U_{\mathrm b}=(\tilde U\tilde U^*)^{1/2}$ is a function of $\tilde U\tilde U^*$, hence commutes with $\tilde U$, and $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ commutes with $\tilde U$ as well. Both commute with $\tilde Q=\Rho\tilde U$, which gives 3. Conversely, if the two factors commute with $\tilde Q$, they commute with $\tilde U$ and with each other, so

$$
\tilde Q\tilde Q^*=|\Rho|^2\tilde U_{\mathrm b}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^*\tilde U_{\mathrm b}
=|\Rho|^2\tilde U_{\mathrm b}^2
=\tilde Q^*\tilde Q,
$$

which gives 1. If 3 holds, both factors are functions of $\tilde U$, hence diagonal in its eigenbasis, so their axes are the two eigenlines, which are $\pm i\vec{Ζ}$; this gives 4. If 4 holds, the two exponents commute, so the product is the exponential of their sum, which gives 5. If 5 holds, $\tilde Q$ is a scalar multiple of the exponential of a complex multiple of a real pure vector, and such an exponential is normal; this gives 1.

For the formula, write $\tilde U_{\mathrm b}=\exp(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u)$ and $\tilde u_{\mathrm r}=\exp(\frac{\theta_{\mathrm{axr}}}{2}\vec u)$ on the common axis. Their product is $\exp(\frac{\theta_{\mathrm{axr}}+i\theta_{\mathrm{rpd}}}{2}\vec u)$ because the exponents commute. On the two eigenlines the product acts by $e^{-\theta_{\mathrm{rpd}}/2}e^{i\theta_{\mathrm{axr}}/2}$ and $e^{\theta_{\mathrm{rpd}}/2}e^{-i\theta_{\mathrm{axr}}/2}$; with the labelling of $\mu_\pm$ fixed by $\lambda_\pm$, and the sign of the common axis chosen accordingly, this is the displayed pair $e^{\mp\theta_{\mathrm{rpd}}/2}e^{\pm i\theta_{\mathrm{axr}}/2}$. The extraction of the angles follows from the moduli and the arguments.

The display is the **amalgamation** of the four factors into one exponential. The complex angle is $\frac{\theta_{\mathrm{axr}}+i\theta_{\mathrm{rpd}}}{2}$; the real part is the rotor angle and the imaginary part is the rapidity. The sign of the imaginary part is the sign convention of the boost: the other choice reverses the common axis.

**Remark (the axes in the normal case).** The common axis is $\pm i\vec{Ζ}$. Since $\vec{Ζ}=-i\vec Q/B$ and $\vec Q=\omega\vec u$, the axis is $\pm\vec u$: the real direction of the vector part. The eigenbasis and the polar frame are the same frame. The element is normal exactly when its vector part has a real direction; a complex vector part with two independent real directions is non-normal.

### The Non-Normal Case

In the general case the polar factors are not functions of $\tilde Q$, and the eigenbasis is not a polar basis.

**Proposition (the failure of the spectral reading).** Let $\tilde Q\in\Sigma_{11}$ be non-normal. Then

$$
[\tilde U_{\mathrm b},\tilde Q]\neq0,
\qquad
[\tilde u_{\mathrm r},\tilde Q]\neq0,
$$

and the axes are not the eigenlines. The eigenvalues $\mu_\pm$ still determine the unordered pair $\{\mu_+,\mu_-\}$, but they do not determine $\theta_{\mathrm{rpd}}$, $\theta_{\mathrm{axr}}$, $\vec u_{\mathrm b}$ or $\vec u_{\mathrm r}$.

*Proof.* The factors commute with $\tilde Q$ exactly when the element is normal, by the theorem. If they do not commute, they are not diagonal in the eigenbasis, so their axes cannot be the eigenlines. The eigenvalues of $\tilde U$ are functions of $U_t$ alone, by $\mu_\pm=U_t\pm i\sqrt{1-U_t^2}$; the word parameters also depend on the relative angle of the axes, through $\operatorname{Sc}\tilde U=c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}c$. There are different triples $(\theta_{\mathrm{rpd}},\theta_{\mathrm{axr}},c)$ with the same $U_t$, hence the same spectrum, and with different words.

The last sentence is the precise statement of the gap. In the normal case $c=\pm1$, and the pair $(\theta_{\mathrm{rpd}},\theta_{\mathrm{axr}})$ is recovered from the spectrum. In the non-normal case $c$ is a third unknown, and the spectrum is one complex equation for three real unknowns.

**Example.** Let $\tilde Q=\bigl(1-\frac{i}{2}\bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$. It is N-regular and spectrally regular, and non-normal, because

$$
\vec Q\times\overline{\vec Q}
=\Bigl(-\frac{i}{\sqrt2},\frac{i}{\sqrt2},i\Bigr)\neq0.
$$

Its word has

$$
\theta_{\mathrm{rpd}}=1.7627471740,
\qquad
\vec u_{\mathrm b}=\vec e_x,
\qquad
\theta_{\mathrm{axr}}=\frac{\pi}{2},
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2},
\qquad
c=\frac{1}{\sqrt2}.
$$

The eigenvalues of the unit factor have moduli $0.480533816$ and $2.081019$, and arguments $\pm0.674888846$. The normal-case formulas would give $\theta_{\mathrm{rpd}}=1.466$ and $\theta_{\mathrm{axr}}=1.350$, not the true $1.763$ and $1.571$. The spectrum is the same; the reading is not.

The example is case 5 of the worked examples. The gap is not a rounding effect: the ratio of the two moduli is $4.331$, whose logarithm is $1.466$, while the rapidity is $1.763$.

### What the Spectrum Determines

The comparison is a count of real data.

| Data | Real dimension | Determines |
|---|---|---|
| $N$, $B^2$ | $4$ | $r,\theta_{\mathrm{pha}},U_t$ |
| spectrum $\{\lambda_+,\lambda_-\}$ | $4$ | the same, in spectral form |
| eigenprojectors $\tilde\Pi_\pm$ | $4$ | the eigenlines; the polar axes only in the normal case |
| word $(r,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\theta_{\mathrm{axr}},\vec u_{\mathrm r})$ | $8$ | the element |

The spectrum and the eigenprojectors together determine the element. The polar word is another eight data. The two parametrizations share the four data $(r,\theta_{\mathrm{pha}},U_t)$; the spectrum determines the remaining data only in the normal case, where the eigenprojectors are the polar axes. In the non-normal case the eigenprojectors do not determine the polar axes, and the spectrum does not determine the two angles.

The spectral decomposition is a diagonalization over $\mathbb{C}$: it writes $\tilde Q$ as two complex multiples of two idempotents. The polar decomposition is a Cartan decomposition over $\mathbb{R}$: it writes $\tilde Q$ as a positive Hermitian factor times a $*$-unitary factor. The two agree on the scalar factor and on the eigenvalues of $\tilde Q$, and on nothing else in the non-normal case.

**Remark (the two decompositions are transverse).** The eigenbasis depends on the complex structure of the vector part; the polar frame depends on the Hermitian structure of the unit factor. The normal elements are the intersection: the elements for which the two frames coincide. The intersection is the normal set, $Q_t+\omega\vec u$ with $Q_t,\omega\in\mathbb{C}$ and $\vec u\in S^2$, of real dimension $2+2+2=6$; it is not open in the sector.


## The Unipotent Unit Factor

### The Scalar Constraint

**Theorem (the rigidity of the word).** Let $\tilde Q\in\Sigma_{10}$ with word as above. Then

$$
\operatorname{Sc}\tilde U=\varepsilon=\pm1,
\qquad
\bigl(\tilde U-\varepsilon e_t\bigr)^2=0,
$$

and the parameters satisfy

$$
\boxed{\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}=\varepsilon},
\qquad
\boxed{\sinh\frac{\theta_{\mathrm{rpd}}}{2}\sin\frac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0}.
$$

*Proof.* By the normal form, $\tilde U=\varepsilon(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$. Its scalar part is $\varepsilon$, and

$$
\bigl(\tilde U-\varepsilon e_t\bigr)^2
=\varepsilon^2\vec\Upsilon^2=0.
$$

The scalar part of the component form is $c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}c$. It equals the real number $\varepsilon$, so its imaginary part vanishes, which gives the second equation, and its real part gives the first.

The two equations are the whole constraint. The scalar part of the unit factor is a complex equation, and the unitarity of $\tilde U$ has already been used; the constraint is one complex equation on the six parameters of the unit factor, which is why the unipotent set has real dimension four.

### The Orthogonal Frame

**Theorem (the orthogonal frame).** On the Jordan part of $\Sigma_{10}$, the word has

$$
\theta_{\mathrm{rpd}}>0,
\qquad
\theta_{\mathrm{axr}}\notin\{0,\pi,2\pi\},
\qquad
\vec u_{\mathrm b}\perp\vec u_{\mathrm r},
$$

and the two angles are tied by

$$
\boxed{\Bigl\lvert\cos\frac{\theta_{\mathrm{axr}}}{2}\Bigr\rvert=\frac{1}{\cosh\frac{\theta_{\mathrm{rpd}}}{2}}},
\qquad
\varepsilon=\operatorname{sgn}\cos\frac{\theta_{\mathrm{axr}}}{2}.
$$

Conversely, every choice of $\theta_{\mathrm{axr}}\in(0,\pi)\cup(\pi,2\pi)$, of $\vec u_{\mathrm b}\in S^2$ and of $\vec u_{\mathrm r}$ in the great circle orthogonal to $\vec u_{\mathrm b}$, with $\theta_{\mathrm{rpd}}$ defined by the displayed relation, gives a word of an element of the Jordan part.

*Proof.* On the Jordan part $\vec\Upsilon\neq0$, so $\tilde U\neq\varepsilon e_t$. If $\theta_{\mathrm{rpd}}=0$ then $c_{\mathrm b}=1$ and the first constraint gives $c_{\mathrm r}=\pm1$, so $\theta_{\mathrm{axr}}\in\{0,2\pi\}$ and the component form is $\tilde U=\pm e_t$, a contradiction. Hence $\theta_{\mathrm{rpd}}>0$ and $s_{\mathrm b}>0$. If $\theta_{\mathrm{axr}}=0$ or $2\pi$ then $s_{\mathrm r}=0$ and the component form is again scalar. If $\theta_{\mathrm{axr}}=\pi$ then $c_{\mathrm r}=0$, and the first constraint gives $0=\pm1$, impossible. Hence $\theta_{\mathrm{axr}}\notin\{0,\pi,2\pi\}$ and $s_{\mathrm r}>0$. The second constraint then forces $c=0$. The first gives $|c_{\mathrm b}c_{\mathrm r}|=1$, which is the displayed relation, and the sign of $c_{\mathrm r}$ is the sign of $\varepsilon$. The converse is a direct substitution: with orthogonal axes and the relation, the scalar part is $\varepsilon$ and the vector part is null, so the unit factor is unipotent and the element lies in the Jordan part.

The frame is therefore orthogonal, and one of the two angles is a function of the other. The independent data of the unipotent factor are one angle and a frame: $\theta_{\mathrm{axr}}$ (one real number), $\vec u_{\mathrm b}$ (two), and $\vec u_{\mathrm r}$ in the orthogonal circle (one), which is four real dimensions, the dimension of the punctured nilpotent cone.

### The Closed Form

Substituting the constraints into the component form gives the shape of the whole sector.

**Theorem (the closed form).** Every $\tilde Q\in\Sigma_{10}$ is

$$
\boxed{\;
\tilde Q=Q_t\Bigl(e_t+
i\tanh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b}
+\tan\frac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r}
+i\tanh\frac{\theta_{\mathrm{rpd}}}{2}\tan\frac{\theta_{\mathrm{axr}}}{2}\;\vec u_{\mathrm b}\times\vec u_{\mathrm r}\Bigr)
\;}
$$

with $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}=\varepsilon$; on the Jordan part the two axes are orthogonal. Equivalently,

$$
\boxed{\;
\tilde Q=Q_t\Bigl(e_t+\vec\Upsilon\Bigr),
\qquad
\vec\Upsilon=i\tanh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b}
+\tan\frac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r}
+i\tanh\frac{\theta_{\mathrm{rpd}}}{2}\tan\frac{\theta_{\mathrm{axr}}}{2}\;\vec u_{\mathrm b}\times\vec u_{\mathrm r}.
\;}
$$

*Proof.* The scalar part of the unit factor is $\varepsilon$, so $c_{\mathrm r}=\varepsilon/c_{\mathrm b}$. On the Jordan part $s_{\mathrm r}>0$, and $\tan\frac{\theta_{\mathrm{axr}}}{2}=s_{\mathrm r}/c_{\mathrm r}=\varepsilon c_{\mathrm b}s_{\mathrm r}$, hence $s_{\mathrm r}=\varepsilon\tan\frac{\theta_{\mathrm{axr}}}{2}/c_{\mathrm b}$. The component form then gives

$$
i s_{\mathrm b}c_{\mathrm r}
=i\varepsilon\tanh\frac{\theta_{\mathrm{rpd}}}{2},
\qquad
c_{\mathrm b}s_{\mathrm r}
=\varepsilon\tan\frac{\theta_{\mathrm{axr}}}{2},
\qquad
i s_{\mathrm b}s_{\mathrm r}
=i\varepsilon\tanh\frac{\theta_{\mathrm{rpd}}}{2}\tan\frac{\theta_{\mathrm{axr}}}{2}.
$$

The vector part of the unit factor is $\varepsilon$ times the bracket, and $\tilde U=\varepsilon(e_t+\vec\Upsilon)$, so the bracket is $\vec\Upsilon$; hence $\tilde Q=Q_t(e_t+\vec\Upsilon)$. On the scalar line $\tan\frac{\theta_{\mathrm{axr}}}{2}=\tanh\frac{\theta_{\mathrm{rpd}}}{2}=0$, and the same display reduces to $Q_te_t$.

The formula is the exact shape of the sector. The complex number $Q_t$ carries the scale and the phase; the rest is a unipotent written in the frame. The vector part is automatically null: with the three orthogonal directions, its square is

$$
\vec\Upsilon^2=\tanh^2\frac{\theta_{\mathrm{rpd}}}{2}-\tan^2\frac{\theta_{\mathrm{axr}}}{2}
+\tanh^2\frac{\theta_{\mathrm{rpd}}}{2}\tan^2\frac{\theta_{\mathrm{axr}}}{2},
$$

which vanishes by $|\cos\frac{\theta_{\mathrm{axr}}}{2}|=1/\cosh\frac{\theta_{\mathrm{rpd}}}{2}$. The cross term carries the plus sign because its coefficient is imaginary.

**Remark (the scalar factor).** The unit factor depends only on $\theta_{\mathrm{axr}}$ and the frame, not on $Q_t$. Changing $Q_t$ by a nonzero complex number changes the scale and the phase, and possibly the sign $\varepsilon$, but leaves $\vec\Upsilon$ unchanged. The sector is the product of the scalar line $\mathbb{C}^{\times}$ with the punctured nilpotent cone; the frame and the two angles are functions of the second factor alone, and the sign is carried by the first.


## The Two Strata

### The Scalar Line

On the scalar line $\vec\Upsilon=0$, the element is $Q_te_t$, the unit factor is $\varepsilon e_t$, and

$$
\theta_{\mathrm{rpd}}=0,
\qquad
\theta_{\mathrm{axr}}\in\{0,2\pi\},
\qquad
\vec u_{\mathrm b},\vec u_{\mathrm r}\ \text{free}.
$$

The word is

$$
\tilde Q=r e^{i\theta_{\mathrm{pha}}}\,\varepsilon e_t
=Q_te_t.
$$

The sign $\varepsilon$ is fixed by the branch: if $\Rho=Q_t$ then $\varepsilon=+1$ and $\theta_{\mathrm{axr}}=0$; if $\Rho=-Q_t$ then $\varepsilon=-1$ and $\theta_{\mathrm{axr}}=2\pi$. The axes are undefined, because the boost and the rotor are central. The scalar line is the normal locus of the sector: a normal element with a single eigenvalue is a scalar, and every scalar is normal.

### The Jordan Part

On the Jordan part $\vec\Upsilon\neq0$, the element is defective: its minimal polynomial is $(X-Q_t)^2$, its geometric multiplicity is one, and it has no eigenbasis. The word has

$$
\theta_{\mathrm{rpd}}>0,
\qquad
\theta_{\mathrm{axr}}\in(0,\pi)\cup(\pi,2\pi),
\qquad
\vec u_{\mathrm b}\perp\vec u_{\mathrm r},
$$

and the two possible signs of $\cos\frac{\theta_{\mathrm{axr}}}{2}$ are the two values of $\varepsilon$. The word is

$$
\tilde Q=Q_t\Bigl(e_t+\vec\Upsilon(\theta_{\mathrm{axr}},\vec u_{\mathrm b},\vec u_{\mathrm r})\Bigr),
$$

with $\vec\Upsilon$ as in the closed form and $\theta_{\mathrm{rpd}}$ determined by $\theta_{\mathrm{axr}}$. The data are

$$
\underbrace{2}_{Q_t}
+\underbrace{1}_{\theta_{\mathrm{axr}}}
+\underbrace{2}_{\vec u_{\mathrm b}}
+\underbrace{1}_{\vec u_{\mathrm r}\perp\vec u_{\mathrm b}}
=6,
$$

the real dimension of the sector. The rapidity and the sign are functions of the angle.

The Jordan part is unbounded: as $\theta_{\mathrm{axr}}\to\pi$, $\theta_{\mathrm{rpd}}\to\infty$ and $|\vec\Upsilon|\to\infty$. The value $\theta_{\mathrm{axr}}=\pi$ is not attained, because it would force $c_{\mathrm r}=0$ and violate the scalar constraint.


## Existence and Uniqueness

**Theorem (the exponential polar decomposition).** Every $\tilde Q\in\Sigma_{11}$ has a unique writing

$$
\tilde Q=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
$$

with $r>0$, $\theta_{\mathrm{pha}}\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\tilde U_{\mathrm b}$ Hermitian positive of norm one, and $\tilde u_{\mathrm r}$ a unit real quaternion. Consequently it has the exponential word above; the axes are unique when $\theta_{\mathrm{rpd}}>0$ and $\theta_{\mathrm{axr}}\notin\{0,2\pi\}$.

*Proof.* The modulus $\Rho$ is the principal square root of $N$, and $\tilde U=\tilde Q/\Rho$ has norm one. The matrix image of $\tilde U$ lies in $SL(2,\mathbb{C})$. The global Cartan decomposition

$$
SL(2,\mathbb{C})=P\cdot K,
\qquad
P=\{\text{positive Hermitian of determinant }1\},
\qquad
K=SU(2),
$$

gives a unique factorization $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde U_{\mathrm b}\in P$ and $\tilde u_{\mathrm r}\in K$. A positive Hermitian determinant-one matrix is the exponential of a unique Hermitian traceless matrix, which is $i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ with $\theta_{\mathrm{rpd}}\ge0$ and a unit axis. A $*$-unitary determinant-one matrix is the exponential of an anti-Hermitian traceless matrix, which is $\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$ with $\theta_{\mathrm{axr}}\in[0,2\pi]$. The endpoint $\theta_{\mathrm{axr}}=2\pi$ is the central rotor $-e_t$, where the axis is undefined. The scale and the phase are the polar coordinates of $\Rho$, unique in the branch.

The proof uses only the invertibility of $\tilde Q$; the spectral condition $B^2\neq0$ enters only through the domain, not through the existence. This is why the theorem holds on the wall as it stands, with the same proof and the same ranges.

**The degeneracies.** The boost axis is undefined at $\theta_{\mathrm{rpd}}=0$, where the boost is the identity. The rotor axis is undefined at $\theta_{\mathrm{axr}}=0$, where the rotor is the identity, and at $\theta_{\mathrm{axr}}=2\pi$, where the rotor is $-e_t$ for every axis. These are the usual coordinate singularities of polar coordinates; the element is smooth there and the word is unique.

| Parameter | Range | Unique? |
|---|---|---|
| $r$ | $(0,\infty)$ | yes |
| $\theta_{\mathrm{pha}}$ | $(-\frac{\pi}{2},\frac{\pi}{2}]$ | yes: the branch |
| $\theta_{\mathrm{rpd}}$ | $[0,\infty)$ | yes |
| $\vec u_{\mathrm b}$ | $S^2$ | no: undefined at $\theta_{\mathrm{rpd}}=0$ |
| $\theta_{\mathrm{axr}}$ | $[0,2\pi]$ | yes |
| $\vec u_{\mathrm r}$ | $S^2$ | no: undefined at $\theta_{\mathrm{axr}}\in\{0,2\pi\}$ |

At a degeneracy the word is still unique as an element of the group, but the coordinate chart is singular. The singularity is not a failure of the decomposition; it is the price of the polar coordinates.

## The Logarithm

### The Cartan Logarithm

Write $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and put

$$
\tilde H=\operatorname{Log}\tilde U_{\mathrm b}=i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b},
\qquad
\tilde K=\operatorname{Log}\tilde u_{\mathrm r}=\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}.
$$

The pair $(\tilde H,\tilde K)$ is the **Cartan logarithm** of $\tilde U$. It is unique with the ranges of the theorem, except at the central rotor, and it satisfies

$$
\tilde U=\exp(\tilde H)\exp(\tilde K).
$$

The two exponents lie in the two summands of the Cartan decomposition of the Lie algebra,

$$
\mathbb{B}=\mathbb{R}e_t\ \oplus\ i\mathbb{R}e_t\ \oplus\ \mathfrak{p}\ \oplus\ \mathfrak{k},
\qquad
\mathfrak{p}=i\{\text{real pure vectors}\},
\qquad
\mathfrak{k}=\{\text{real pure vectors}\},
$$

of real dimensions $1+1+3+3=8$. The boost exponent is in $\mathfrak{p}$ and the rotor exponent in $\mathfrak{k}$.

### The Single Logarithm

A **single logarithm** of $\tilde Q$ is an element $\operatorname{Log}\tilde Q$ with $\exp(\operatorname{Log}\tilde Q)=\tilde Q$. Since $\mathbb{B}\cong M_2(\mathbb{C})$ and every invertible complex matrix has a logarithm, the exponential is surjective onto the invertibles. A single logarithm is related to the Cartan logarithm by

$$
\operatorname{Log}\tilde Q=\ln r+i\theta_{\mathrm{pha}}+\operatorname{Log}\bigl(\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr),
$$

where the last term is a logarithm inside $\mathfrak{gl}(2,\mathbb{C})$, not inside $\mathfrak{sl}(2,\mathbb{C})$; its trace may be a nonzero multiple of $2\pi i$.

The **formal exponent** is the sum of the four exponents,

$$
\tilde Q_{\log}=\ln r+i\theta_{\mathrm{pha}}+i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}+\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}.
$$

It is not the single logarithm in general. The **log defect** is the Baker–Campbell–Hausdorff correction, whose first term is

$$
\frac12[\tilde H,\tilde K]
=\frac{i\theta_{\mathrm{rpd}}\theta_{\mathrm{axr}}}{4}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}
\in\mathfrak{p}.
$$

The first correction is again a boost. The formal exponent is a logarithm exactly when this correction and all higher ones vanish. In the normal case the axes are parallel, the commutator vanishes, and the formal exponent is a logarithm. In the non-normal case the correction is nonzero, and the exponential of the formal exponent misses the element; the worked examples give defects $0.5$ and $0.4222$.

### The Fibre

The exponential is not injective. Its kernel contains the central periods $2\pi ik\,e_t$, the pure periods $2\pi\vec U$ for real unit vectors, and the mixed elements $\pi i\,e_t+\pi\vec U$. The fibre over an element is not a coset of the kernel, because the exponential is not a homomorphism.

The polar parameters do not cut the fibre of the exponential to one point: the four exponents sum to the formal exponent, which is not a logarithm. What they cut to one point, up to the axis degeneracies, is the fibre of the **word map**

$$
(r,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\theta_{\mathrm{axr}},\vec u_{\mathrm r})
\longmapsto
r e^{i\theta_{\mathrm{pha}}}\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)
\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr).
$$

The word is a section of that map, not of the exponential. It is a global coordinate system on the group of invertibles, and its domain is the complement of the null cone.

### The Exact Logarithm at the Wall

The special feature of the sector is that the true logarithm is not a transcendental object: the unipotent factor has a truncated logarithm.

**Theorem (the exact logarithm).** For $\tilde Q=Q_t(e_t+\vec\Upsilon)\in\Sigma_{10}$,

$$
\boxed{\operatorname{Log}\tilde Q=\log Q_t+\vec\Upsilon},
$$

where $\log Q_t$ is any logarithm of the nonzero complex number $Q_t$ and the principal choice is $\ln|Q_t|+i\arg Q_t$. The right-hand side is exact, with no series and no correction.

*Proof.* The exponential of a nilpotent element truncates:

$$
\exp(\vec\Upsilon)=e_t+\vec\Upsilon,
$$

because $\vec\Upsilon^2=0$. The scalar $Q_t$ commutes with $\vec\Upsilon$, so

$$
\exp(\log Q_t+\vec\Upsilon)=Q_t(e_t+\vec\Upsilon)=\tilde Q.
$$


The logarithm is the sum of the scalar logarithm and the nilpotent vector part. The period $2\pi ik\,e_t$ can be added to the scalar logarithm, and no other ambiguity is present on the Jordan part: the logarithm is unique modulo the central periods, because the nilpotent part is fixed by $\tilde Q$.

The operator form of this single exponent is in §*The Exponential at the Wall* of *One-Sided Operators on the N-Regular Sector* and of *Two-Sided Operators on the N-Regular Sector*: the exponential of the left multiplication is the shear $\exp(L_{\tilde Q})=e^{Q_t}(I+Q_tL_{\vec\Upsilon})$, and the two-sided operator is the null rotation $\mathrm{Sd}_{\tilde Q}=|Q_t|^2e^{A+B}$.

### The Formal Exponent and the Defect at the Wall

The **formal exponent** is the sum of the four exponents,

$$
\tilde Q_{\log}=\ln r+i\theta_{\mathrm{pha}}+i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}+\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}.
$$

It is not the logarithm. The true logarithm is

$$
\operatorname{Log}\tilde Q=\ln r+i\theta_{\mathrm{pha}}+i\pi\frac{1-\varepsilon}{2}+\vec\Upsilon,
$$

because $Q=\Rho\tilde U$ with $\operatorname{Log}\tilde U=\vec\Upsilon+i\pi\frac{1-\varepsilon}{2}$, so $\operatorname{Log}\tilde Q=\log\Rho+\operatorname{Log}\tilde U$; equivalently, $\log Q_t=\log\Rho+i\pi\frac{1-\varepsilon}{2}$ and the unipotent part adds $\vec\Upsilon$. The **log defect** is therefore explicit:

$$
\boxed{\;
\operatorname{Log}\tilde Q-\tilde Q_{\log}
=i\pi\frac{1-\varepsilon}{2}
+i\Bigl(\varepsilon\tanh\frac{\theta_{\mathrm{rpd}}}{2}-\frac{\theta_{\mathrm{rpd}}}{2}\Bigr)\vec u_{\mathrm b}
+\Bigl(\varepsilon\tan\frac{\theta_{\mathrm{axr}}}{2}-\frac{\theta_{\mathrm{axr}}}{2}\Bigr)\vec u_{\mathrm r}
+i\varepsilon\tanh\frac{\theta_{\mathrm{rpd}}}{2}\tan\frac{\theta_{\mathrm{axr}}}{2}\;\vec u_{\mathrm b}\times\vec u_{\mathrm r}.
\;}
$$

The **defect** is the norm of $\exp(\tilde Q_{\log})-\tilde Q$, not the norm of the log defect, because the exponential is not linear. The log defect shows the three corrections: the scalar period, the nonlinear terms $\varepsilon\tanh\frac{\theta_{\mathrm{rpd}}}{2}-\frac{\theta_{\mathrm{rpd}}}{2}$ and $\varepsilon\tan\frac{\theta_{\mathrm{axr}}}{2}-\frac{\theta_{\mathrm{axr}}}{2}$, and the cross term. The numerical defect is computed in the worked examples.

On the Jordan part the cross term is nonzero, because $\theta_{\mathrm{rpd}}>0$, $\theta_{\mathrm{axr}}\notin\{0,\pi,2\pi\}$ and the axes are orthogonal. The formal exponent is therefore not the logarithm. The cross term has the shape of the first correction of the Baker–Campbell–Hausdorff series,

$$
\frac12[\tilde H,\tilde K]
=\frac{i\theta_{\mathrm{rpd}}\theta_{\mathrm{axr}}}{4}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r},
$$

with the sign of $\varepsilon$; the exact log defect also contains the nonlinear terms $\varepsilon\tanh\frac{\theta_{\mathrm{rpd}}}{2}-\frac{\theta_{\mathrm{rpd}}}{2}$ and $\varepsilon\tan\frac{\theta_{\mathrm{axr}}}{2}-\frac{\theta_{\mathrm{axr}}}{2}$.

On the scalar line the cross term is absent, and the formal exponent is a logarithm: for $\varepsilon=+1$ it is $\ln r+i\theta_{\mathrm{pha}}$, and for $\varepsilon=-1$ it is $\ln r+i\theta_{\mathrm{pha}}+\pi\vec u_{\mathrm r}$, whose exponential is $-\Rho$ for every invertible $\vec u_{\mathrm r}$.

## The Group Law

The product of two words is

$$
\bigl(r_1e^{i\theta_{\mathrm{pha},1}}e^{\tilde H_1}e^{\tilde K_1}\bigr)
\bigl(r_2e^{i\theta_{\mathrm{pha},2}}e^{\tilde H_2}e^{\tilde K_2}\bigr)
=r_1r_2e^{i(\theta_{\mathrm{pha},1}+\theta_{\mathrm{pha},2})}e^{\tilde H_1}e^{\tilde K_1}e^{\tilde H_2}e^{\tilde K_2}.
$$

The central factors add. The non-central ones do not: the middle product $e^{\tilde K_1}e^{\tilde H_2}$ must be re-split as a boost times a rotor. The first correction is a commutator, so the rotor of the first word conjugates the boost of the second; the parameters of the product are not the sums of the parameters.

The brackets of the two summands close as a symmetric pair.

| Bracket | Lies in | Reading |
|---|---|---|
| $[\mathfrak{k},\mathfrak{k}]$ | $\mathfrak{k}$ | two rotors compose to a rotor |
| $[\mathfrak{p},\mathfrak{p}]$ | $\mathfrak{k}$ | two boosts compose to a boost times a rotor |
| $[\mathfrak{k},\mathfrak{p}]$ | $\mathfrak{p}$ | a rotor conjugates a boost to a boost |

The second row is the Thomas–Wigner rotation. The third is the statement that the boost set is a symmetric space and not a group: the commutator of an infinitesimal rotor and an infinitesimal boost is a boost, so the boost directions are stable under the adjoint action of the rotor, while the boost set itself is not closed under multiplication. The first row is the subgroup $SU(2)$ of the rotor.

| Data | Law |
|---|---|
| scale and phase | multiply |
| boost | conjugated by the rotor, not added |
| rotor | multiplies |
| exponent | does not add: the Baker–Campbell–Hausdorff correction |
| group | $\mathbb{B}^{\times}\cong\mathrm{GL}_2(\mathbb{C})$ |

### The Product at the Wall

The sector is closed under inversion:

$$
\tilde Q^{-1}=Q_t^{-1}\bigl(e_t-\vec\Upsilon\bigr).
$$

It is not closed under multiplication. The product of two elements is

$$
\tilde Q_1\tilde Q_2
=Q_{t1}Q_{t2}\bigl(e_t+\vec\Upsilon_1\bigr)\bigl(e_t+\vec\Upsilon_2\bigr)
=Q_{t1}Q_{t2}\bigl(e_t+\vec\Upsilon_1+\vec\Upsilon_2+\vec\Upsilon_1\vec\Upsilon_2\bigr).
$$

Let

$$
s=\vec\Upsilon_1\cdot\vec\Upsilon_2.
$$

The scalar part of the product is $Q_{t1}Q_{t2}(1-s)$, and the product has norm one, so its vector form is

$$
\boxed{B^2(\tilde Q_1\tilde Q_2)=Q_{t1}^2Q_{t2}^2\,s(2-s)}.
$$

The product lies in $\Sigma_{10}$ exactly when $s=0$ or $s=2$; otherwise it lies in $\Sigma_{11}$.

*Proof.* Write the product as $Q_{t1}Q_{t2}W$, with $W=(1+\vec\Upsilon_1)(1+\vec\Upsilon_2)$. The scalar part of $W$ is $1-\vec\Upsilon_1\cdot\vec\Upsilon_2=1-s$, because the dot part of $\vec\Upsilon_1\vec\Upsilon_2$ is $-\vec\Upsilon_1\cdot\vec\Upsilon_2$ and the cross part is a pure vector. The norm of $W$ is one, because it is the product of two unipotent elements of norm one. An element of norm one with scalar part $1-s$ has vector form $1-(1-s)^2=s(2-s)$; the central scalar $Q_{t1}Q_{t2}$ multiplies the vector form by $(Q_{t1}Q_{t2})^2$.

**Example.** Take $u_1=e_t+\vec e_x+i\vec e_y$ and $u_2=e_t+\vec e_y+i\vec e_z$. Then $s=i$, and

$$
u_1u_2=(1-i)e_t+\vec e_y+(1+i)\vec e_z,
$$

with $B^2=1+2i\neq0$. The product has left the sector. Take instead $u_1$ and $u_2=e_t+\vec e_x-i\vec e_y$; then $s=2$, and

$$
u_1u_2=-e_t+2\vec e_x-2i\vec e_z,
$$

with $B^2=0$; the product stays. The two cases are the two roots of $s(2-s)=0$.

## The Matrix Picture

The matrix model is

$$
\mathsf M(\tilde Q)=Q_tI-iQ_x\sigma_x-iQ_y\sigma_y-iQ_z\sigma_z.
$$

It is a $\mathbb{C}$-algebra homomorphism, so $\mathsf M(\exp\tilde X)=\exp(\mathsf M(\tilde X))$, and the polar word becomes the polar decomposition of $\mathrm{GL}_2(\mathbb{C})$,

$$
\mathsf M(\tilde Q)=r e^{i\theta_{\mathrm{pha}}}\,\mathsf M(\tilde U_{\mathrm b})\,\mathsf M(\tilde u_{\mathrm r}),
$$

with $\mathsf M(\tilde U_{\mathrm b})$ positive definite of determinant one and $\mathsf M(\tilde u_{\mathrm r})$ $*$-unitary of determinant one.

The spectral reading is the diagonalization of the matrix. The matrix $\mathsf M(\tilde Q)$ has the two distinct eigenvalues $\lambda_\pm$, and it is diagonalizable; the eigenbasis is a basis of $\mathbb{C}^2$ consisting of the two eigenvectors. The polar factors are the positive and $*$-unitary factors of the matrix polar decomposition. They are diagonal in that basis exactly when the matrix is normal, which is the matrix form of the theorem of §*The Normal Case*.

The four exponents sit in the two summands of

$$
\mathfrak{gl}_2(\mathbb{C})=\mathfrak{u}(2)\oplus\mathfrak{H},
\qquad
\mathfrak{u}(2)=\{X:X^\dagger=-X\},
\qquad
\mathfrak{H}=\{X:X^\dagger=X\},
$$

of real dimensions $4$ and $4$. The scale and the boost lie in $\mathfrak H$; the phase and the rotor lie in $\mathfrak u(2)$. The central real line is the scale, the central imaginary line is the phase, and the traceless parts are the boost and the rotor.

| Matrix object | Algebra object | Dimension | Factor |
|---|---|---|---|
| positive determinant-one matrix | Hermitian positive unit-norm element | $3$ | boost |
| $*$-unitary determinant-one matrix | unit real quaternion | $3$ | rotor |
| positive real scalar | scale | $1$ | $r$ |
| unit complex scalar | phase | $1$ | $e^{i\theta_{\mathrm{pha}}}$ |

The two scales of the matrix are $r e^{\theta_{\mathrm{rpd}}/2}$ and $r e^{-\theta_{\mathrm{rpd}}/2}$, each with multiplicity one in the regular sector. Their product is $r^2=|\Rho|^2$, and their ratio is $e^{\theta_{\mathrm{rpd}}}$. The determinant is $N=\Rho^2$, of modulus $r^2$.

### The Picture at the Wall

On the Jordan part, $\mathsf M(\vec\Upsilon)$ is a nonzero nilpotent matrix, so

$$
\mathsf M(\tilde Q)=Q_t\bigl(I+N\bigr),
\qquad
N=\mathsf M(\vec\Upsilon),
\qquad
N^2=0,
\qquad
N\neq0.
$$

The matrix is $Q_t$ times a single unipotent Jordan block. Its eigenvalue is $Q_t$, with algebraic multiplicity two and geometric multiplicity one; its determinant is $Q_t^2$; its two singular values are $r e^{\theta_{\mathrm{rpd}}/2}$ and $r e^{-\theta_{\mathrm{rpd}}/2}$. The polar factors are the positive and $*$-unitary factors of the block, and the $*$-unitary factor is the rotor. The sign $\varepsilon$ is the sign of the scalar part of the unit block.

The spectral reading is degenerate in the matrix picture: the matrix has no eigenbasis, the two eigenvalues coincide, and the diagonal form does not exist. The polar decomposition still exists, because it is the Cartan decomposition of $SL(2,\mathbb{C})$, which does not require diagonalizability. This is the matrix form of the contrast between the two cases.

## The Exponential Coordinates

The parameters $r,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\theta_{\mathrm{axr}}$ and the two axes are coordinates on the group of invertibles. Their ranges make the map a bijection up to the axis degeneracies. The coordinate lines are the four one-parameter families:

- the **scale line** $r\mapsto r e^{i\theta_{\mathrm{pha}}}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a half-line;
- the **phase circle** $\theta_{\mathrm{pha}}\mapsto r e^{i\theta_{\mathrm{pha}}}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a circle cut to a half-open interval by the branch;
- the **boost hyperbola** $\theta_{\mathrm{rpd}}\mapsto r e^{i\theta_{\mathrm{pha}}}\exp(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})\tilde u_{\mathrm r}$, a non-compact ray;
- the **rotor arc** $\theta_{\mathrm{axr}}\mapsto r e^{i\theta_{\mathrm{pha}}}\tilde U_{\mathrm b}\exp(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$, a great semicircle from $e_t$ to $-e_t$.

The positive cone $P$ is homeomorphic to $\mathbb{R}^3$ and the rotor group $K=SU(2)$ is $S^3$, so

$$
SL(2,\mathbb{C})\simeq\mathbb{R}^3\times S^3.
$$

The group of invertibles retracts onto $U(2)$, and $U(2)\cong U(1)\times SU(2)$ as a space, so

$$
\mathbb{B}^{\times}\simeq S^1\times S^3.
$$

The branch of the modulus makes $\tilde Q\mapsto(\Rho,\tilde U)$ a bijection onto $\mathbb{C}^{\times}\times SL(2,\mathbb{C})$, but not a homeomorphism: on the cut the phase jumps by $-1$ and the rotor changes sign. The fundamental group is $\mathbb{Z}$, carried by the phase.

The **conformal factor** is read in the coordinates. Under the two-sided operator $\tilde QX\tilde Q^*$, the quaternionic norm of $X$ is multiplied by

$$
r^4=\exp(4\ln r)=\bigl\lvert\langle\tilde Q\rangle_{\natural}\bigr\rvert^2,
$$

so lengths are multiplied by $r^2=|\langle\tilde Q\rangle_{\natural}|$. The scale exponent is a quarter of the logarithm of the conformal factor; the phase, the boost and the rotor are isometries of the form.

### The Coordinates at the Wall

The data of the sector are

$$
\underbrace{2}_{Q_t}
+\underbrace{1}_{\theta_{\mathrm{axr}}}
+\underbrace{2}_{\vec u_{\mathrm b}}
+\underbrace{1}_{\vec u_{\mathrm r}\perp\vec u_{\mathrm b}}
=6,
$$

the real dimension of the wall. The rapidity and the sign are determined by

$$
\cosh\frac{\theta_{\mathrm{rpd}}}{2}=\frac{1}{\lvert\cos\frac{\theta_{\mathrm{axr}}}{2}\rvert},
\qquad
\varepsilon=\operatorname{sgn}\cos\frac{\theta_{\mathrm{axr}}}{2}.
$$

The coordinate map is

$$
(Q_t,\theta_{\mathrm{axr}},\vec u_{\mathrm b},\vec u_{\mathrm r})
\longmapsto
Q_t\Bigl(e_t+\vec\Upsilon(\theta_{\mathrm{axr}},\vec u_{\mathrm b},\vec u_{\mathrm r})\Bigr),
$$

from $\mathbb{C}^{\times}\times\bigl((0,\pi)\cup(\pi,2\pi)\bigr)\times US^2$ to the Jordan part, where $US^2=\{(\vec u_{\mathrm b},\vec u_{\mathrm r}):\lvert\vec u_{\mathrm b}\rvert=\lvert\vec u_{\mathrm r}\rvert=1,\ \vec u_{\mathrm b}\perp\vec u_{\mathrm r}\}$ is the unit tangent bundle of the sphere. It is a bijection onto the Jordan part; the scalar line is the common limit $\theta_{\mathrm{axr}}\to0$ and $\theta_{\mathrm{axr}}\to2\pi$, where the frame is free.

The coordinate lines are three families:

- the **scalar line** $Q_t\mapsto Q_t(e_t+\vec\Upsilon)$, a complex plane with the origin removed;
- the **angle line** $\theta_{\mathrm{axr}}\mapsto Q_t(e_t+\vec\Upsilon(\theta_{\mathrm{axr}},\ldots))$, a non-compact curve from the scalar line to infinity, with $\theta_{\mathrm{rpd}}$ growing as $\theta_{\mathrm{axr}}\to\pi$;
- the **frame sphere** $(\vec u_{\mathrm b},\vec u_{\mathrm r})\mapsto Q_t(e_t+\vec\Upsilon)$, a circle bundle over $S^2$.

The sector retracts onto the scalar line, because the nilpotent part can be contracted to zero along $\vec\Upsilon\mapsto(1-t)\vec\Upsilon$, which stays null. Hence $\Sigma_{10}$ is connected and $\pi_1(\Sigma_{10})=\mathbb{Z}$, carried by the phase of $Q_t$.

## The Two Walls

The sector is the complement of the union of two cones.

| Wall | Equation | Stratum | What happens to the word |
|---|---|---|---|
| null cone | $N=0$ | $\Sigma_{01}\cup\Sigma_{00}$ | $r\to0$, $\theta_{\mathrm{rpd}}\to\infty$ |
| spectral cone | $B^2=0$ | $\Sigma_{10}\cup\Sigma_{00}$ | word finite, eigenbasis degenerates |

The two cones meet at $\Sigma_{00}$, the nilpotent stratum. The two walls behave differently, and the difference is the subject of this section.

### The Null Cone

On the null cone the modulus vanishes and no unit factor exists. A nonzero element of the cone is a zero divisor of rank one. As an element of the sector approaches the cone with $B^2$ bounded away from zero, the rapidity diverges and the scale collapses. The standard family is

$$
\tilde Q(\theta_{\mathrm{rpd}})=R e^{-\theta_{\mathrm{rpd}}/2}\,\omega\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)\tilde u_{\mathrm r},
\qquad
\theta_{\mathrm{rpd}}>0,
$$

with $R>0$, $|\omega|=1$ and unit axes. Every member is invertible, with modulus $R e^{-\theta_{\mathrm{rpd}}/2}$, and its word has rapidity $\theta_{\mathrm{rpd}}$. The limit is

$$
\tilde Q(\theta_{\mathrm{rpd}})\longrightarrow
\frac{R\omega}{2}\bigl(e_t+i\vec u_{\mathrm b}\bigr)\tilde u_{\mathrm r},
\qquad
\theta_{\mathrm{rpd}}\to\infty,
$$

a nonzero null element of rank one. It is nilpotent exactly when $\tilde u_{\mathrm r}$ anticommutes with $\vec u_{\mathrm b}$, and it has nonzero scalar part otherwise. The scale vanishes as $e^{-\theta_{\mathrm{rpd}}/2}$ and the boost diverges as $e^{\theta_{\mathrm{rpd}}/2}$; the product stays finite.

### The Spectral Cone

On the spectral cone the word does not diverge. Let $\tilde Q_k\to\tilde Q_0$ with $N_k\to N_0\neq0$ and $B_k^2\to0$. The modulus converges, the unit factor converges, and the Cartan factors converge, because the Cartan decomposition is continuous. Hence the polar data have a limit: the limiting word is the word of $\tilde Q_0$, which lies in $\Sigma_{10}$ and is treated in the companion article.

The eigenbasis does not survive. The root is

$$
\vec{Ζ}=-i\frac{\vec Q}{B},
$$

and $B\to0$ while $\vec Q\to\vec Q_0\neq0$ on the spectral cone, so $|\vec{Ζ}|\to\infty$. The idempotents

$$
\tilde\Pi_\pm=\frac{e_t\pm\vec{Ζ}}{2}
$$

diverge, and the spectral decomposition has no limit. The eigenvalues $\lambda_\pm=Q_t\pm iB$ coalesce, the minimal polynomial becomes a square, and the element becomes defective.

**Proposition (the word survives the spectral wall, the eigenbasis does not).** Let $\tilde Q_k\in\Sigma_{11}$ converge to $\tilde Q_0\in\Sigma_{10}$ with $N_0\neq0$ and $\vec Q_0\neq0$, so that the limit lies in the Jordan part. Then $\tilde U_k\to\tilde U_0$, $\tilde U_{\mathrm b,k}\to\tilde U_{\mathrm b,0}$ and $\tilde u_{\mathrm r,k}\to\tilde u_{\mathrm r,0}$, so the word converges to the word of $\tilde Q_0$. The root $\vec{Ζ}_k$ diverges in norm, and no spectral idempotent of $\tilde Q_k$ converges to a nonzero idempotent.

*Proof.* The modulus is continuous in $N$ away from zero, and the Cartan factors are continuous functions of $\tilde U$; this gives the convergence of the word. The root satisfies $|\vec{Ζ}_k|=|\vec Q_k|/|B_k|\to\infty$ because $\vec Q_k\to\vec Q_0\neq0$ and $B_k\to0$. An idempotent of the form $(e_t\pm\vec{Ζ}_k)/2$ is unbounded, so it has no finite limit.

At the scalar line the limit is different. If $\tilde Q_0=Q_0e_t$ is a nonzero scalar, then $\vec Q_0=0$, the root is $0/0$, and its limit depends on the path: the family $Q_k=1+\epsilon_k\vec e_x$ has $\vec{Ζ}_k=-i\vec e_x$, so the idempotents converge to nonzero idempotents of the ambient algebra even though the limit is scalar. The eigenvalues coalesce, but the eigenbasis need not diverge. The proposition is therefore stated for the Jordan part, which is the part of the wall that the sector meets transversally.

The contrast is the exact content of the difference between the two articles. The polar decomposition is a decomposition of the group of invertibles, and it is continuous across the spectral wall. The spectral decomposition is a decomposition of the element, and it degenerates there. The sector $\Sigma_{11}$ is the open set on which both exist; its wall $B^2=0$ is where only the polar one survives.

### The Wall From Inside

The sector is closed under inversion but not under multiplication. It is a complex hypersurface of $\mathbb{B}$, not an open set: its closure is the spectral cone $B^2=0$, and the points of that closure with $N=0$ form the nilpotent stratum $\Sigma_{00}$.

### The Nilpotent Stratum

As $Q_t\to0$ with $\vec\Upsilon$ fixed, the element tends to zero and the modulus tends to zero. The unit factor does not degenerate:

$$
\tilde U=\varepsilon\bigl(e_t+\vec\Upsilon\bigr)
$$

is independent of $Q_t$. The scale collapses, the phase follows the argument of $Q_t$, and the unipotent shape survives. This is the structural difference from the regular sector, where the rapidity diverges as the modulus vanishes. In $\Sigma_{10}$ the modulus is the scalar part, and the only thing that vanishes is the scalar.

A nonzero nilpotent of $\Sigma_{00}$ is reached by letting $Q_t\to0$ and $\vec\Upsilon\to\infty$ at the rate $Q_t\vec\Upsilon\to\vec N$ with $\vec N^2=0$. The unit factor diverges, the word parameters leave every bounded set, and the limit is the nilpotent. The sector is not compact, and the angle $\theta_{\mathrm{axr}}\to\pi$ is the direction in which it is unbounded.

### The Spectral Wall From Inside

Seen from $\Sigma_{11}$, the locus $B^2=0$ is a wall: the word converges to the word of the limit, as §*The Spectral Cone* proves, while the eigenbasis diverges and the spectral decomposition disappears. Seen from $\Sigma_{10}$, the same locus is the ambient space. The two descriptions are the two sides of one hypersurface: defective elements, no eigenbasis, and a polar word that is still defined.

| Approach | Locus | What happens |
|---|---|---|
| nilpotent stratum | $N=0$, $B^2=0$ | $Q_t\to0$; the unit factor survives if $\vec\Upsilon$ is fixed; the scale vanishes |
| spectral wall from $\Sigma_{11}$ | $B^2=0$, $N\neq0$ | the word converges; the eigenbasis diverges |

## Summary

### Main Formulas

The table collects the general formulas and the shapes they take on the wall.

| Object | Formula |
|---|---|
| domain | $N\neq0$, $B^2\neq0$ |
| word | $\tilde Q=r e^{i\theta_{\mathrm{pha}}}\exp(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})\exp(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$ |
| modulus | $\Rho=r e^{i\theta_{\mathrm{pha}}}=(N)^{1/2}$ in the branch |
| unit factor | $\tilde U=\tilde Q/\Rho=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| boost | $\tilde U_{\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ |
| rotor | $\tilde u_{\mathrm r}=\cos\frac{\theta_{\mathrm{axr}}}{2}e_t+\sin\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$ |
| component form | $\tilde U=(c_{\mathrm b}c_{\mathrm r}-is_{\mathrm b}s_{\mathrm r}c)e_t+is_{\mathrm b}c_{\mathrm r}\vec u_{\mathrm b}+c_{\mathrm b}s_{\mathrm r}\vec u_{\mathrm r}+is_{\mathrm b}s_{\mathrm r}\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ |
| eigenvalues | $\lambda_\pm=Q_t\pm iB$ |
| eigenbasis | $\vec{Ζ}=-i\vec Q/B$, $\tilde\Pi_\pm=\frac12(e_t\pm\vec{Ζ})$ |
| unit-factor eigenvalues | $\mu_\pm=\lambda_\pm/\Rho=U_t\pm i\sqrt{1-U_t^2}$ |
| normal case | $\mu_\pm=e^{\mp\theta_{\mathrm{rpd}}/2}e^{\pm i\theta_{\mathrm{axr}}/2}$, axes $\pm i\vec{Ζ}$ |
| normal criterion | $\vec Q\times\overline{\vec Q}=0$ |
| spectral wall | $B^2=0\iff U_t=\pm1$ |
| explicit data | §*The Result in Terms of the Coordinates*: boxes for $r,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\tilde U_{\mathrm b},\tilde u_{\mathrm r},\theta_{\mathrm{axr}},\vec u_{\mathrm r}$ |
| domain, wall | $N\neq0$, $B^2=0$ |
| normal form | $\tilde Q=Q_t(e_t+\vec\Upsilon)$, $\vec\Upsilon^2=0$ |
| unit factor, wall | $\tilde U=\varepsilon(e_t+\vec\Upsilon)$, $\varepsilon=Q_t/\Rho=\pm1$ |
| scalar constraint | $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}=\varepsilon$ |
| axis constraint | $\sinh\frac{\theta_{\mathrm{rpd}}}{2}\sin\frac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$ |
| Jordan part | $\theta_{\mathrm{rpd}}>0$, $\theta_{\mathrm{axr}}\notin\{0,\pi,2\pi\}$, $\vec u_{\mathrm b}\perp\vec u_{\mathrm r}$ |
| angle relation | $\bigl|\cos\frac{\theta_{\mathrm{axr}}}{2}\bigr|=1/\cosh\frac{\theta_{\mathrm{rpd}}}{2}$ |
| closed form, wall | $\tilde Q=Q_t\bigl(e_t+i\tanh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}+\tan\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}+i\tanh\frac{\theta_{\mathrm{rpd}}}{2}\tan\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm b}\times\vec u_{\mathrm r}\bigr)$ |
| exact logarithm | $\operatorname{Log}\tilde Q=\log Q_t+\vec\Upsilon$ |
| product criterion | $B^2(\tilde Q_1\tilde Q_2)=Q_{t1}^2Q_{t2}^2s(2-s)$, $s=\vec\Upsilon_1\cdot\vec\Upsilon_2$ |
| dimension, wall | $6$: $Q_t$ (2), angles (2), frame (3), angle relation (1) |

### The Comparison

| Property | Spectral reading | Polar reading |
|---|---|---|
| decomposition of | the element $\tilde Q$ | the unit factor $\tilde U$ |
| factors | two idempotents | positive Hermitian times $*$-unitary |
| coefficients | $\lambda_\pm$ | exponentials of $\theta_{\mathrm{rpd}},\theta_{\mathrm{axr}}$ |
| diagonal in the eigenbasis | always | exactly when normal |
| survives $B^2\to0$ | no on the Jordan part | yes |
| real dimension | $8$ | $8$ |
| shared data | $r,\theta_{\mathrm{pha}},U_t$ | $r,\theta_{\mathrm{pha}},U_t$ |
The last row is the statement of the section: the spectral reading is defined on the open sector, the polar reading is defined on the whole group of invertibles.

### What the Sector Shows

- The word exists for every element of the N-regular sector, off the wall and on it, and it is unique up to the axis degeneracies.
- The existence theorem uses only the invertibility of $\tilde Q$. The invariant $B^2$ enters through the domain and through the shape of the word, not through the existence.
- Off the wall the eigenbasis exists because the two eigenvalues are distinct. It is a spectral basis, not a polar basis. The polar factors are diagonal in it exactly for the normal elements, and those are exactly the elements whose two axes are parallel and whose word is a single exponential.
- In the non-normal case the spectrum determines the eigenvalues of the unit factor but not the rapidity, the rotor angle or the axes. The polar word carries four real data that the spectrum does not.
- On the wall the unit factor is $\pm$unipotent: its two eigenvalues coincide, its minimal polynomial is a square, and it has no eigenbasis. The word still exists, with four real data: the scalar part, one angle and a frame.
- On the wall the scalar part of the unit factor is $\pm1$. This one complex equation ties the two angles, $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}=\pm1$, and on the Jordan part it forces the two axes to be orthogonal.
- The true logarithm on the wall is exact and truncated, $\log Q_t+\vec\Upsilon$. The formal exponent is not a logarithm: the log defect is the cross term plus the nonlinear terms of the two angles.
- The word is continuous across the spectral wall; the eigenbasis is not. This is the precise sense in which the polar decomposition is a decomposition of the group and the spectral decomposition is a decomposition of the element.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $Q_t,Q_x,Q_y,Q_z$ | the four complex coordinates |
| $N=\langle\tilde Q\rangle_{\natural}$ | the reduced product $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $B^2$ | the vector form $Q_x^2+Q_y^2+Q_z^2$ |
| $\Sigma_{11}$ | the N-regular, spectrally regular sector |
| $\Rho=r e^{i\theta_{\mathrm{pha}}}$ | the modulus, principal square root of $N$ |
| $\tilde U=\tilde Q/\Rho$ | the unit factor |
| $\tilde U_{\mathrm b},\tilde u_{\mathrm r}$ | the Hermitian positive factor and the rotor, $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| $\theta_{\mathrm{rpd}}$ | the rapidity |
| $\theta_{\mathrm{axr}}$ | the rotor angle |
| $\vec u_{\mathrm b},\vec u_{\mathrm r}$ | the two axes |
| $c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | the cosine between the axes |
| $\vec{Ζ}=-i\vec Q/B$ | the root of one carried by the element |
| $\tilde\Pi_\pm=\frac12(e_t\pm\vec{Ζ})$ | the spectral idempotents |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\mu_\pm=\lambda_\pm/\Rho$ | the eigenvalues of the unit factor |
| $\tilde H,\tilde K$ | the Cartan pair |
| $\tilde Q_{\log}$ | the formal exponent |
| $\mathsf M(\tilde Q)$ | the matrix $Q_tI-iQ_x\sigma_x-iQ_y\sigma_y-iQ_z\sigma_z$ |
| $c_{\mathrm b},s_{\mathrm b},c_{\mathrm r},s_{\mathrm r}$ | the half-angle cosines and sines |
| $\lVert\tilde Q\rVert^2=|Q_t|^2+|\vec Q|^2$ | the Euclidean norm squared of the coordinates |
| $\vec a$ | the vector $\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$ |
| $C,S$ | the half-angle numerators, $\cosh\frac{\theta_{\mathrm{rpd}}}{2}=C/\sqrt{|N|}$, $\sinh\frac{\theta_{\mathrm{rpd}}}{2}=S/\sqrt{|N|}$ |
| $\mathrm{Vect}\tilde X$ | the vector part of $\tilde X$ |
| $\Sigma_{11}$ | the N-regular, spectrally regular sector |
| $\Sigma_{10}$ | the N-regular, spectrally degenerate sector |
| $\vec\Upsilon=\vec Q/Q_t$ | the nilpotent direction on the wall, $\vec\Upsilon^2=0$ |
| $\vec A=\operatorname{Re}\vec\Upsilon$, $\vec B=\operatorname{Im}\vec\Upsilon$ | the real and imaginary parts, $\vec A\cdot\vec B=0$ |
| $a=\lVert\vec A\rVert=\lVert\vec B\rVert$ | the common length on the wall |
| $\varepsilon=Q_t/\Rho=\pm1$ | the sign of the unit factor on the wall |
| $Q_\mu=q_\mu+iq'_\mu$ | the eight real coordinates |
| $\vec q=(q_x,q_y,q_z)$, $\vec q'=(q'_x,q'_y,q'_z)$ | the real and imaginary vector coordinates |
| $s=\vec\Upsilon_1\cdot\vec\Upsilon_2$ | the invariant of a product on the wall |

## Further Reading

- [Relations between Exponential Polar Decomposition and Eigenbasis on the N-Regular Sector](relations-between-exponential-polar-decomposition-and-eigenbasis-on-the-n-regular-sector.html), for the dictionary between the word and the eigenvalue data, and its limit on the Jordan part.
- [Worked Examples of Exponential Polar Decomposition on the N-Regular Sector](worked-examples-of-exponential-polar-decomposition-on-the-n-regular-sector.html), for the numerical cases off the wall and on it, the normal and non-normal comparison, and the defect tables.
- [The Polar Decomposition of an N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus–unit theorem and the group of invertibles.
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), for the eigenbasis, the Peirce corners and the spinors.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the normal forms and the two strata of the wall.
- [The Spectrum](the-spectrum.html), for the four sectors and the discriminants.
- [One-Sided Operators on the N-Regular Sector](the-one-sided-operator-exponential-on-the-n-regular-sector.html), for the operator form of the exact logarithm on the wall.
- [Two-Sided Operators on the N-Regular Sector](the-two-sided-exponential-on-the-n-regular-sector.html), for the two-sided operator form.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the logarithm, the kernel and the fibre.
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the Cartan decomposition and the Baker–Campbell–Hausdorff series.
- [Conventions in Mathematics](algebra-and-element-conventions.html), for the notation.
