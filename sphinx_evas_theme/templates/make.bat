@echo off
chcp 65001 > NUL 2>&1

setlocal
pushd %~dp0

set ENV_FAIL=0

echo *************** 依赖环境检查... *******************
where python > nul 2>&1
if not %errorlevel% equ 0 (
	echo python  ---------------------------- [NOK]
	set ENV_FAIL=1
) else (
	echo python  ---------------------------- [OK]
)
where perl > nul 2>&1
if not %errorlevel% equ 0 (
	echo perl    ---------------------------- [NOK]
	set ENV_FAIL=1
) else (
	echo perl    ---------------------------- [OK]

)
where latexmk > nul 2>&1
if not %errorlevel% equ 0 (
	echo latexmk ---------------------------- [NOK]
	set ENV_FAIL=1
) else (
	echo latexmk ---------------------------- [OK]

)
where xelatex > nul 2>&1
if not %errorlevel% equ 0 (
	echo xelatex ---------------------------- [NOK]
	set ENV_FAIL=1
) else (
	echo xelatex ---------------------------- [OK]

)
echo *************** 依赖环境检查完成... ***************

if not %ENV_FAIL% equ 0 (
	goto end
)

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -X utf8 -m sphinx build
)
set SOURCEDIR=source
set BUILDDIR=_build

if "%1" == "" goto all
if "%1" == "pdf" goto pdf
if "%1" == "all" goto all
if "%1" == "clean" goto clean

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O% --keep-going
goto end

:pdf
%SPHINXBUILD% -M latex %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O% --keep-going

cd %BUILDDIR%\latex
echo PDF 构建中，请稍等
cmd /c latexmk -r latexmkrc -pdf -f -dvi- -ps- -interaction=nonstopmode -g -quiet -dependents- -nodependents -rules- -rc-report- -dir-report- -outdir=..\pdf
echo PDF 文件保存在 _build\pdf 目录
goto end

:all
%SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O% --keep-going
goto pdf

:clean
if exist "%BUILDDIR%" (
    rmdir /s /q %BUILDDIR%
	echo 已清空 %BUILDDIR% 构建目录
) else (
    echo %BUILDDIR% 构建目录不存在，使用make命令构建
)
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
endlocal
popd
